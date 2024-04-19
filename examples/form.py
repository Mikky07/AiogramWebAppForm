import uvicorn
from starlette.applications import Starlette

from telegram_webapp_ui.webapp import WebAppUI
from telegram_webapp_ui.form import Form, Field, FieldTypes, Button

app = Starlette()

form = Form(
    Field(name='password', text='first', regex='?????'),
    Field(name='username', text='second', regex='?????', type=FieldTypes.TEL),
    Field(name='date', text='password', regex='?????', type=FieldTypes.PASSWORD),
    Field(name='test_name', text='тестовое поле', required=True, type=FieldTypes.TIME),
    button=Button('отправить!'),
    title="Form 1",
    widget_url='/form_1'
)
webapp = WebAppUI(form, bot_token='')

webapp.mount(app)

uvicorn.run(app)
