'''
This module is responsible for handling the execution of python code given by the telegram user.
'''
import logging
from subprocess import TimeoutExpired
import subprocess
import multiprocessing
from .config import BANNED, TIMEOUT, TIMEOUT_MESSAGE, RESTRICT_MESSAGE, IMP_TOKEN, IMPORTS_MAP


def contains_restricted(input_text):
    '''returns true if any restricted word is found'''
    if any(word in input_text for word in BANNED):
        # block usage of this words for security and performance issues
        return True
    return False


def preprocessor(input_text: str) -> str:
    '''
    this function is a preprocessor that replace lines according to IMP_MAP
    if the string is not finded the line will remain the same,
    this preprocessor has an intentional unflexible syntax and it not support spaces before
    the token or after the string
    '''
    code_lines = input_text.splitlines()
    ppdict_keys = IMPORTS_MAP.keys()
    for i in range(len(code_lines)):
        if IMP_TOKEN in code_lines[i][:len(IMP_TOKEN)]:
            if code_lines[i][len(IMP_TOKEN):] in ppdict_keys:
                code_lines[i] = IMPORTS_MAP[code_lines[i][len(IMP_TOKEN):]]
    return "\n".join(code_lines)


def run(update) -> str:
    '''
    This function takes an Telegram `update` object,
    passed by the `reply` function in the runPython_bot module,
    and returns the result after executing update.message.text.
    '''

    def execute_py(code):
        '''
        This function takes a string of python code
        and executes code in a subprocess of timeout 30s,
        Returns the standard out and standard error.

        Learn more about subprocesses from the official docs of Python
        https://docs.python.org/3/library/subprocess.html

        For a shorter intro read this stack overflow answer
        https://stackoverflow.com/questions/64606880/how-to-get-the-python-interactive-shell-output-of-a-python-code-in-a-variable
        '''

        proc = subprocess.Popen(['/usr/bin/python3.8', '-c', code],
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        try:
            stdout, stderr = proc.communicate(timeout=TIMEOUT)
            return stdout.decode('utf-8'), stderr.decode('utf-8')
        except TimeoutExpired:
            return '', TIMEOUT_MESSAGE
        except Exception as error:
            return '', f'Problem occured \n{error}'
        finally:
            proc.kill()

    def func(input_text: str):
        '''
        This function is a helper function which does some validation job before passing
        the code to execute_py.
        '''

        if contains_restricted(input_text):
            return RESTRICT_MESSAGE
        stdout, stderr = execute_py(preprocessor(input_text))
        if str(stdout) or str(stderr):
            out = f'{stdout} \n{stderr}'
            return out
        return None
    try:
        if update.message.text:
            input_text = update.message.text

            out = func(input_text)
            return out
        return 'update.message.text was None'
    except Exception as error:
        msg = 'Error in handling update.message.text'
        logging.log(level=40, msg=error)
        return msg


def eval_py(input_text: str):
    ''' Runs eval() on the input text on a seperate process and returns output or error.
    How to timout on a function call ? https://stackoverflow.com/a/14924210/13523305
    Return a value from multiprocess ? https://stackoverflow.com/a/10415215/13523305
    '''

    def evaluate(input_text, return_val):
        '''wrapper for eval()'''
        try:
            return_val[input_text] = str(eval(input_text))
        except Exception as error:
            return_val[
                input_text] = str(error)

    if contains_restricted(input_text):
        return RESTRICT_MESSAGE

    # using multiprocessing and getting value returned by target function
    manger = multiprocessing.Manager()
    return_val = manger.dict()  # enable target function to return a value

    process = multiprocessing.Process(
        target=evaluate, args=(input_text, return_val))
    process.start()
    process.join(6)  # allow the process to run for 6 seconds
    if process.is_alive():
        # kill the process if it is still alive
        process.kill()
        return TIMEOUT_MESSAGE
    output = return_val[input_text]
    return output
