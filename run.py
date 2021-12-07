import asyncio

from asgiref.wsgi import WsgiToAsgi
from hypercorn import Config
from hypercorn.asyncio import serve

from app import create_app
from app.db import init_db


async def start():
    await init_db()

    app = create_app()
    asgi_app = WsgiToAsgi(app)

    corn_config = Config()
    # corn_config.use_reloader = True
    # corn_config.debug = True
    await serve(asgi_app, corn_config)


asyncio.run(start())
