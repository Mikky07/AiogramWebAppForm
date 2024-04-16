from pathlib import Path
from typing import Callable, Coroutine
from dataclasses import dataclass

from starlette.requests import Request
from starlette.templating import Jinja2Templates

from app.webapp import UIWidget


@dataclass
class Field:
    name: str
    regex: str


class Form(UIWidget):
    def __init__(
            self,
            *fields: Field,
            widget_id: str,
            title: str
    ):
        super().__init__(widget_id)
        self.fields = fields
        self.id = widget_id
        self.title = title
        self.templates_dir_path = Path('.') / 'templates'
        self.template_filename = 'form.html'

    def get_async_endpoint(self) -> Callable[..., Coroutine]:
        templates = Jinja2Templates(str(self.templates_dir_path))

        async def form_endpoint(request: Request):
            return templates.TemplateResponse(request=request, name=self.template_filename)

        return form_endpoint
