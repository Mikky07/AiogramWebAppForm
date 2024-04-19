import os
from enum import Enum
from pathlib import Path
from typing import Callable, Coroutine, Optional
from dataclasses import dataclass

from starlette.requests import Request
from starlette.templating import Jinja2Templates

from telegram_webapp_ui.webapp import UIWidget


class FieldTypes(Enum):
    TEXT = 'text'
    PASSWORD = 'password'
    COLOR = 'color'
    DATE = 'date'
    DATETIME_LOCAL = 'datetime-local'
    EMAIL = 'email'
    HIDDEN = 'hidden'
    MONTH = 'month'
    NUMBER = 'number'
    RANGE = 'range'
    TIME = 'time'
    URL = 'url'
    WEEK = 'week'
    TEL = 'tel'


@dataclass
class Field:
    name: str
    text: str
    label: Optional[str] = None
    regex: Optional[str] = None
    type: FieldTypes = FieldTypes.TEXT
    required: bool = False


@dataclass
class Button:
    text: str
    color: Optional[str] = None


class Form(UIWidget):
    def __init__(
            self,
            *fields: Field,
            widget_url: str,
            title: str,
            button: Optional[Button] = None
    ):
        super().__init__(widget_url)
        self.fields = fields
        self.title = title
        self.templates_dir_path = Path(os.path.relpath(__file__)).parent / 'templates'
        self.template_filename = 'form.html'
        self.button = button if button else Button('Submit')

    def get_async_endpoint(self) -> Callable[..., Coroutine]:
        templates = Jinja2Templates(str(self.templates_dir_path))

        async def form_endpoint(request: Request):
            return templates.TemplateResponse(
                request=request,
                name=self.template_filename,
                context={
                    'title': self.title,
                    'fields': enumerate(self.fields),
                    'button': self.button
                },
            )

        return form_endpoint
