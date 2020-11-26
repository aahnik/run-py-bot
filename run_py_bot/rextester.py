''' This module connects with the rextester api
'''

import logging
import asyncio
import aiohttp


async def run_python_rextester(code):
    ''' Asynchronous function to run a code using the rextester api
    and returns the promise of result dictionary.

    Args:
        code (str) : the code to be executed

    Returns:
        promise: a dictionary with keys
            Result = Output of a program
            Warnings = Warnings, if any, as one string
            Errors = Errors, if any, as one string
            Stats = Execution stats as one string
            Files = files

    '''

    if '\n' not in code:
        code = f'print(eval("""{code}"""))'

    base = 'https://rextester.com/rundotnet/api'

    payload = {
        'LanguageChoice': '24',  # for python3
        'Program': code
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url=base, data=payload) as response:
            return await response.json()


async def main(times: int):
    ''' Runner for run_python_rextester

    Args:
        times (int): how many times to be run
    '''

    tasks = [run_python_rextester('print("ok")') for i in range(times)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    # Testing the run_python_rextester

    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main(times=10))
