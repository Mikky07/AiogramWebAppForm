import uvicorn

from app.webapp import WebAppUI
from app.form import Form, Field


form = Form(
    Field(name='first', regex='?????'),
    title="Fill the form to continue:",
    widget_id='form_1_id'
)
webapp = WebAppUI(form, bot_token='')

app = webapp()

uvicorn.run(app)
