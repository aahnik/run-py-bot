''' Script to start the bot '''
import logging
from quart import Quart


from run_py_bot import main, config

logging.basicConfig(level=logging.INFO)

app = Quart(__name__)


@app.route('/')
async def hello():
    return 'hello'


@app.route(f'/{config.API_TOKEN}')
async def info():
    info = await main.info()
    return str(info)

if __name__ == "__main__":
    app.run(host=config.WEBAPP_HOST, port=config.WEBAPP_PORT)
    main.webhook()
