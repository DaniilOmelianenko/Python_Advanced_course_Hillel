import aioreloader
import aiohttp_jinja2
from aiohttp_session import setup, SimpleCookieStorage, session_middleware
from jinja2 import FileSystemLoader
from aiohttp import web
from pymongo import MongoClient
import motor.motor_asyncio
from aiohttp_session.cookie_storage import EncryptedCookieStorage

from handlers import Login, Lot, Register, Trade, Main, WebSocketView

if __name__ == '__main__':
    app = web.Application()

    app.wslist = []
    client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://root:123qwe@localhost:27017/')
    sync_client = MongoClient('mongodb://root:123qwe@localhost:27017/')
    app.db = client['auction_db']
    app.sync_db = sync_client['auction_db']
    # setup(app, EncryptedCookieStorage(b'Thirty  two  length  bytes  key.'))
    # setup(app, SimpleCookieStorage(b'Thirty  two  length  bytes  key.'))
    # setup(app, SimpleCookieStorage(max_age=60*60*24*7))

    aiohttp_jinja2.setup(app, loader=FileSystemLoader('templates'))
    setup(app, SimpleCookieStorage())

    app.router.add_static('/static/', 'static')

    app.router.add_get('/register', Register)
    app.router.add_post('/register', Register)

    app.router.add_get('/login', Login)
    app.router.add_post('/login', Login)

    app.router.add_get('/', Main)
    app.router.add_post('/', Main)

    app.router.add_post('/create/lot', Lot)

    app.router.add_get('/lot/{lot_id:[a-fA-F0-9]{24}}', Trade)
    app.router.add_post('/lot/{lot_id:[a-fA-F0-9]{24}}', Trade)

    app.router.add_get('/ws', WebSocketView)

    aioreloader.start()
    web.run_app(app, port=1616)
