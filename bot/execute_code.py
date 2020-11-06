'''
This module is responsible for handling the execution of python code given by the telegram user.
'''
import logging
from subprocess import TimeoutExpired
import subprocess
from .config import banned, timeout, timeout_message
import multiprocessing
import time


def run(update) -> str:
    '''
    This function takes an Telegram `update` object, passed by the `reply` function in runPython_bot module, and returns the result after executing update.message.text.
    '''

    def execute_py(code):
        '''
        This function takes a string of python code and executes it in a subprocess of timeout 30s, and returns the standard out and standard error.

        Learn more about subprocesses from the official docs of Python 
        https://docs.python.org/3/library/subprocess.html

        For a shorter intro read this stack overflow answer 
        https://stackoverflow.com/questions/64606880/how-to-get-the-python-interactive-shell-output-of-a-python-code-in-a-variable
        '''

        proc = subprocess.Popen(['/usr/bin/python3.8', '-c', code],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            stdout, stderr = proc.communicate(timeout=timeout)
            return stdout.decode('utf-8'), stderr.decode('utf-8')
        except TimeoutExpired:
            return '', timeout_message
        except Exception as e:
            return '', f'Problem occured \n{e}'
        finally:
            proc.kill()

    def func(input_text):
        '''
        This function is a helper function which does some validation job before passing the code to execute_py.
        '''

        if any(word in input_text for word in banned):
            # block usage of this words for security and performance issues
            out = f'☹️ SECURITY ISSUE: You have used a restricted word \n {banned}'
            return out
        stdout, stderr = execute_py(input_text)
        if str(stdout) or str(stderr):
            out = f'{stdout} \n{stderr}'
            return out
        return None
    try:
        if update.message.text:
            input_text = update.message.text

            out = func(input_text)
            if not out:
                return 'No output. No error \n > Try wrapping your expression with a `print` statement \n > Try writing your expression followed by /e command, which will feed your expression to the eval function of python'
            return out
        else:
            return 'update.message.text was None'
    except Exception as e:
        msg = 'Error in handling update.message.text'
        logging.log(level=40, msg=msg)
        return msg


def eval_py(input_text: str):

    def evaluate(input_text, return_val):
        try:
            return_val[input_text] = str(eval(input_text))
        except Exception as e:
            return_val[
                input_text] = f'''😔 /e feeds your expression to python's eval function, and the following error occured: \n\n{e}'''

    m = multiprocessing.Manager()
    return_val = m.dict()

    p = multiprocessing.Process(target=evaluate, args=(input_text, return_val))
    p.start()
    p.join(6)
    if p.is_alive():
        p.kill()
        return timeout_message
    else:
        output = return_val[input_text]
        return output
