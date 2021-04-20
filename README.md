<p align="center">
<img src="docs/images/Chatting%20with%20Python.png" alt="thumbnail" width=600px>
</p>

<h1 align="center"> run-py-bot </h1>

<p align="center">
Run python code from your telegram chat!
</p>

<p align="center"><a href="https://github.com/aahnik/run-py-bot/blob/main/LICENSE"><img src="https://img.shields.io/github/license/aahnik/run-py-bot" alt="GitHub license"></a>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg" alt="made-with-python"></a>
<a href="https://gitHub.com/aahnik/REPO/graphs/commit-activity"><img src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" alt="Maintenance Yes"></a>
<a href="https://telegram.me/aahnikdaw"><img src="https://img.shields.io/badge/chat-@aahnikdaw-blue?logo=telegram" alt="telegram-chat"></a>
<a href="https://telegram.me/runPython_bot"><img src="https://img.shields.io/badge/bot-@runPython_bot-orange?logo=telegram" alt="telegram-bot"></a>
<a href="https://youtu.be/nCuQ-7Rw0gM"><img src="https://img.shields.io/youtube/views/nCuQ-7Rw0gM?style=social" alt="badge-youtube"></a></p>



<!-- A simple bot that runs python code. Free and Open Source. For more info visit http://bit.ly/runPython -->


You can find this bot on Telegram as [@runPython_bot](https://telegram.me/runPython_bot).

You may check whether the bot is alive or not, by clicking on the start command. If the bot responds, it is alive.

## Featured in 😍

1. Tweet by [Dev Community](https://twitter.com/ThePracticalDev/status/1325386583537803264)
2. Tweet by [The Python Dev](https://twitter.com/The_Python_DEV/status/1325237102058016768)
3. Dor Moshe's [Newsletter](https://dormoshe.io/newsletters/ag/python/7?utm_source=twitter&utm_campaign=twitter)
4. My YouTube Video [Chatting with Python](https://youtu.be/nCuQ-7Rw0gM)

## Example Use 🔀

You may use pythonic expressions to easily calculate any complex problem. Or you may test your algorithms on the go.

<p align="center">
<img src="docs/images/run_python_bot_v0.1+.gif" alt="demo" >
</p>

## How to run 🤖

You can easily run your own instance of the bot.

You can run on any OS (windows/mac/linux). For better reliability, you may deploy to a VPS like Digital Ocean Droplet. You can even run on Android, using the Termux app.

Open your terminal and follow the instructions to run the bot.

> **Note:** Use python 3.8

- Make sure you have `git`, `python` and `pip`.

    ```bash
    # the following commands should not produce error
    git --version
    python --version # 3.8 is recommended
    pip --version
    ```

    > **Note:** In some systems `python` version 3 is availaible as `python3`

- First of all, clone the repository and move into the `run-py-bot` directory.

    ```shell
    git clone https://github.com/aahnik/run-py-bot.git && cd run-py-bot
    ```

- Create a python virtual enviroment and activate it.

    ```bash
    python -m venv .venv # create
    source .venv/bin/activate # activate (unix)
    # the command to activate virtual environment is different for Windows, google search
    ```

- Install the requirements.

    ```bash
    pip install -r requirements.txt
    ```

- Set `API_TOKEN` environment variable. Write the following into a file named `.env`.

    ```bash
    API_TOKEN=1234fsjksjfls23r4
    # use your own real token
    ```

    You can create a new bot and get token from [@BotFather](https://telegram.me/BotFather).

- Run the `start.py`, and you are good to go.

    ```shell
    python start.py
    ```

## Deploy to Heroku 🚀

You can click this button to deploy to Heroku.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/aahnik/run-py-bot)

For more details [read the guide](https://github.com/aahnik/run-py-bot/issues/18) about Heroku deployment.

## Changelog 🔖

See the [Releases](https://github.com/aahnik/run-py-bot/releases) tab for more info.

## Contributing ✨

Issues and PRs welcome!

If planning to contribute code, Read the docstrings in the code for details. You will find lots of helpful links to stack overflow and documentation of libraries used.

Here are some useful links:

1. [How to deploy a telegram bot to Heroku](https://github.com/aahnik/webhook-aiogram-heroku#webhook-aiogram-heroku)
2. [Telegram Bot API Documentaion](https://core.telegram.org/bots/api)
3. [Aiogram Examples](https://github.com/aiogram/aiogram/tree/dev-2.x/examples)
4. [The Heroku Procfile](https://devcenter.heroku.com/articles/procfile)
5. [What are webhooks](https://www.youtube.com/results?search_query=webhooks)
6. [How to use an API to run a piece of Python code](https://rextester.com/main)
