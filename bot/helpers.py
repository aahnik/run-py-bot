''' This module provides several helper functions to do variety of tasks '''

import logging


def check_length(text: str) -> str:
    ''' Telegram does not allow messages over 4096 characters. 
    Long messages don't look good. This function will truncate long messages.

    Args:
        text (str): the text to be checked.

    Returns:
        str: the modified text, no modification if length is allowed.
    '''

    text = str(text)
    if not text:
        return 'This should not happen'
    if len(text) > 1000:
        return text[:1000] + '\n... truncated <too long message>'
    else:
        return text


def parse_response(resp: dict) -> dict:
    ''' Parses the response dictionary obtained after running code, and makes a beautified string out of it.

    Args:
        resp (dict): the dictionary returned by run_python_rextester.

    Returns:
        dict: a dictionary containing the message and stats.
    '''

    output = {'message': '', 'stats': ''}
    try:
        if resp['Errors'] == 'Too many requests...':
            output['message'] = 'Try after some time. I may block you if you send too many messages at a very short interval. If you think you are innocent, please contact @AahnikDaw'
            output['stats'] = 'No information availaible'
        else:
            output['message'] = f'''{check_length(resp['Result'])  if resp['Result'] else 'No result' }
                        \n{check_length(resp['Errors'])  if resp['Errors'] else ''}
                        \n{check_length(resp['Warnings'])  if resp['Warnings'] else ''}'''.strip('\n')
            output['stats'] = resp['Stats']
        return output
    except Exception as err:
        logging.warning(err)
        return None


def results(text: str) -> list:
    ''' Returns a list of results for inline call to the bot.

    Args:
        text (str): the query text.

    Returns:
        list: list of results.
    '''

    result_list = [
        ('1', 'YouTube', ''),
        ('2', 'Dev Community',
         'https://dev.to/aahnik/start-chatting-with-python-on-telegram-29ci'),
        ('3', 'GitHub', 'https://github.com/aahnik/run-py-bot')
    ]
    return result_list
