from typing import Callable, Coroutine, Any

from jinja2 import Template

from app.webapp_ui import UIWidget


class Field:
    def __init__(self, name: str, regex: str):
        self.name = name
        self.regex = regex


class Form(UIWidget[Template]):
    def __init__(
            self,
            *fields: Field,
            component_id: str,
            title: str
    ):
        self.fields = fields
        self.id = component_id
        self.title = title

    def get_template(self) -> Template:
        ...

    def get_async_endpoint(self) -> Callable[..., Coroutine[Any, Any, Template]]:
        ...
