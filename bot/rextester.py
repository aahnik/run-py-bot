import logging
import aiohttp
import asyncio


async def run_python_rextester(code):
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
            will return None in case of failure
            '''


async def main(n):
    tasks = [run_python_rextester('print("ok")') for i in range(n)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main(n=10))
