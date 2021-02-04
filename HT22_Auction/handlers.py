# регистрация/логин
# список лотов
# торги
# websocket connection
import aiohttp_jinja2
from aiohttp.web import HTTPFound, View, Response, WebSocketResponse, Response, json_response
from aiohttp_session import get_session
from forms import LoginForm, RegisterForm


class Main(View):

    @aiohttp_jinja2.template('main.html')
    async def get(self):
        lots = await self.request.app.db['lots'].find().to_list(length=9999)
        return {'lots': lots}

    async def post(self):
        data = await self.request.post()
        # if 'username' in data:
        session = await get_session(self.request)
        session['username'] = data['username']
        return Response(text='Chat')
        # raise HTTPFound('/trade')


class Register(View):

    @aiohttp_jinja2.template('register.html')
    async def get(self):
        return {
            'form': RegisterForm(db=self.request.app.sync_db),
            'redirect': False
        }

    @aiohttp_jinja2.template('register.html')
    async def post(self):
        form = RegisterForm(
            formdata=await self.request.post(),
            db=self.request.app.sync_db
        )
        if form.validate():
            user_id = await form.save(self.request.app.db)
            session = await get_session(self.request)
            session['user_id'] = user_id
            return {'redirect': True, 'form': form}
            # return HTTPFound('/trade')
        return {
            'form': form,
            'redirect': False
        }


class Login(View):
    @aiohttp_jinja2.template('login.html')
    async def get(self):
        return {
            'form': LoginForm(db=self.request.app.sync_db)
        }

    @aiohttp_jinja2.template('login.html')
    async def post(self):
        form = LoginForm(
            formdata=await self.request.post(),
            db=self.request.app.sync_db
        )
        if form.validate():
            session = await get_session(self.request)
            session['user_id'] = form.user_id
            return {'redirect': True, 'form': form}
        return {
            'form': form,
            'redirect': False
        }


class Trade(View):

    @aiohttp_jinja2.template('trade.html')
    async def get(self):
        return {}

    @aiohttp_jinja2.template('trade.html')
    async def post(self):
        data = await self.request.post()
        # if 'username' in data:
        session = await get_session(self.request)
        session['username'] = data['username']
        return {'username': session['username']}


class Lot(View):
    async def post(self):
        data = await self.request.json()
        result = await self.request.app.db['lots'].insert_one({
            'name': data['name'],
            'price': data['price'],
        })
        return json_response({
            'id': str(result.inserted_id)
        })


class WebSocketView(View):
    async def get(self):
        ws = WebSocketResponse()
        await ws.prepare(self.request)
        self.request.app.wslist.append(ws)
        session = await get_session(self.request)

        async for bet in ws:
            for websocket_connection in self.request.app.wslist:
                await websocket_connection.send_str(f"{session['username']}: {bet.data}")

        self.request.app.wslist.remove(ws)
