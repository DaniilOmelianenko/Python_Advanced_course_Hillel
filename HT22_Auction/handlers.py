# регистрация/логин
# список лотов
# торги
# websocket connection
import aiohttp_jinja2
from aiohttp.web import HTTPFound, View, Response, WebSocketResponse
from aiohttp_session import get_session
from forms import RegisterForm


class UserBet(View):

    @aiohttp_jinja2.template('userbet.html')
    async def get(self):
        session = await get_session(self.request)
        if 'username' in session and session['username']:
            raise HTTPFound('/trade')
        return {}

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
            'form': RegisterForm()
        }

    @aiohttp_jinja2.template('register.html')
    async def post(self):
        form = RegisterForm(formdata=await self.request.post())
        if form.validate():
            user_id = await form.save(self.request.app.db)
            session = await get_session(self.request)
            session['user_id'] = user_id
            return HTTPFound('/trade')
        return {
            'form': form
        }


class Login(View):
    @aiohttp_jinja2.template('login.html')
    async def get(self):
        return {}


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
