''' This module connects with the rextester api
'''

import logging
import aiohttp
import asyncio


async def run_python_rextester(code):
    ''' Asynchronous function to run a code using the rextester api and returns the result dictionary.
    '''

    if '\n' not in code:
        code = f'print(eval("""{code}"""))'

    base = 'https://rextester.com/rundotnet/api'

    payload = {
        'LanguageChoice': '5',  # for python
        'Program': code
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url=base, data=payload) as response:

            return await response.json()

            '''returns dictionary with keys
            Result=Output of a program 
            Warnings=Warnings, if any, as one string
            Errors=Errors, if any, as one string
            Stats=Execution stats as one string
            Files=files
            '''


async def main(n):
    tasks = [run_python_rextester('print("ok")') for i in range(n)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    ''' Testing the run_python_rextester '''

    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main(n=10))
