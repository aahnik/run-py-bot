# run-py-bot
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

Run python code from your telegram chat!

[![GitHub license](https://img.shields.io/github/license/aahnik/run-py-bot)](https://github.com/aahnik/run-py-bot/blob/main/LICENSE)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Maintenance Yes](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://gitHub.com/aahnik/REPO/graphs/commit-activity)
[![telegram-chat](https://img.shields.io/badge/chat-@aahnikdaw-blue?logo=telegram)](https://telegram.me/aahnikdaw)
[![telegram-bot](https://img.shields.io/badge/bot-@runPython_bot-orange?logo=telegram)](https://telegram.me/runPython_bot)

![RunPythonBot](https://github.com/aahnik/run-py-bot/blob/main/docs/images/runPython_bot.png?raw=true)

<!-- A simple bot that runs python code. Free and Open Source. For more info visit http://bit.ly/runPython -->

## Find on Telegram 🔎

You can find this bot on Telegram as [@runPython_bot](https://telegram.me/runPython_bot).

This bot is deployed on [Python Anywhere](https://www.pythonanywhere.com/) free Beginner Account.
You may check whether the bot is alive or not, by clicking on the start command. If the bot responds, it is alive.

## Featured in 😍

1. Tweet by [Dev Community](https://twitter.com/ThePracticalDev/status/1325386583537803264)
2. Tweet by [The Python Dev](https://twitter.com/The_Python_DEV/status/1325237102058016768)
3. Dor Moshe's Newsletter [Python Trends #7 ](https://dormoshe.io/newsletters/ag/python/7?utm_source=twitter&utm_campaign=twitter) 

## Example Use 🔀

You may use pythonic expressions to easily calculate any complex problem. Or you may test your algorithms on the go.

> If you are viewing from a smartphone, click on the gif to view full screen ...

![runPython_bot](https://github.com/aahnik/run-py-bot/blob/main/docs/images/runPython_bot_gif.gif?raw=true)

## Deploy ⚡

You can easily *deploy this bot* on [Python Anywhere](https://www.pythonanywhere.com/) or your **local machine** by following the below steps:

> Note: While pasting on your machine terminal you should use `Ctrl+Shift+V` but make sure to use `Ctrl+V` to paste in the Python Anywhere bash console from the browser.

Create a free Python Anywhere account and open a Bash Console, which has everything pre-loaded.

If you are planning to deploy on your **own machine**, make sure to have `Python3+`, `pip`.

The following instructions will work smoothly on *Linux* and *Mac*. If you are on Windows, you may have to make slight modifications. Google is your best friend here.

- Clone this repository and move into it.

      git clone https://github.com/aahnik/run-py-bot.git && cd run-py-bot

- Now add the token in the first line of `token.txt`.Run `cat > token.txt` -> Paste the token -> Press `Ctrl+D`

- Create a virtual environment and install dependencies.

      python3.8 -m venv venv && source venv/bin/activate
      python3.8 -m pip install -r requirements.txt

- Activate the bot by running `python3.8 start.py`

- You may now close the Python Anywhere bash console window from your browser, but the bot will continue running.

Your bot is now up and running, Enjoy ! 😊

All the logs will have the timestamp in the time-zone specified in the `start.py` file.

To stop the bot, press `Ctrl+C`. You may update the code running in your server by `git fetch && git pull`.

## Limitations 😑

Currently, the bot is deployed on a Free Tier account of Python Anywhere.

For security and performance reasons, you **cannot** do the following with the bot:

- import any package
- run the `input()` function
- run the `open()` function
- Execute a piece of code which takes longer than *6 seconds* to execute.

You may overcome these limitations by changing the `config.py` file in the `bot` subdirectory and running the bot on your own server.

## The Shameless Plug 🤗 

This project has been authored by me [**Aahnik Daw**](https://github.com/aahnik).

You may connect with me by clicking on any of the icons below !

<a href = "https://twitter.com/AahnikD" > <img src = "https://github.com/aahnik/aahnik/blob/master/svg_assets/twitter.svg?raw=true" alt = "twitter" width=35> </a>
<a href = "https://medium.com/@aahnik" > <img src = "https://github.com/aahnik/aahnik/blob/master/svg_assets/medium.svg?raw=true" alt = "medium" width=35> </a>
<a href = "https://www.facebook.com/aahnik.daw" > <img src = "https://github.com/aahnik/aahnik/blob/master/svg_assets/facebook.svg?raw=true" alt = "facebook" width=35> </a>
<a href = "https://www.linkedin.com/in/aahnik-daw-067a011b3/" > <img src = "https://github.com/aahnik/aahnik/blob/master/svg_assets/linkedin.svg?raw=true" alt = "linkedin" width=35> </a>
<a href = "https://dev.to/aahnik" > <img src = "https://github.com/aahnik/aahnik/blob/master/svg_assets/dev_to.svg?raw=true" alt = "dev_to" width=35> </a>
<a href = "https://stackoverflow.com/users/13523305/aahnik-daw" > <img src = "https://github.com/aahnik/aahnik/blob/master/svg_assets/stackoverflow.svg?raw=true" alt = "stackoverflow" width=35> </a>
<a href = "https://telegram.me/AahnikD" > <img src = "https://github.com/aahnik/aahnik/blob/master/svg_assets/telegram.svg?raw=true" alt = "telegram" width=35> </a>
<a href = "https://www.youtube.com/channel/UCcEbN0d8iLTB6ZWBE_IDugg" > <img src = "https://github.com/aahnik/aahnik/blob/master/svg_assets/youtube.svg?raw=true" alt = "youtube" width=35> </a>


## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/gabrielesilinic"><img src="https://avatars0.githubusercontent.com/u/51238829?v=4" width="100px;" alt=""/><br /><sub><b>gabrielesilinic</b></sub></a><br /><a href="#security-gabrielesilinic" title="Security">🛡️</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

Contributions of any kind welcome! Please read [Contributing Guidelines](https://github.com/aahnik/run-py-bot/blob/main/.github/CONTRIBUTING.md) to get started.
