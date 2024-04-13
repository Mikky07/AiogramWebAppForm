from pathlib import Path
from typing import Callable, Coroutine, Any
from dataclasses import dataclass

from jinja2 import Environment, FileSystemLoader

from app.webapp import UIWidget


@dataclass
class Field:
    name: str
    regex: str


class Form(UIWidget[str]):
    def __init__(
            self,
            *fields: Field,
            component_id: str,
            title: str
    ):
        self.fields = fields
        self.id = component_id
        self.title = title
        self.templates_dir_path = Path('.') / 'templates'
        self.template_filename = 'form.html'

    def _get_template(self) -> str:
        loader = FileSystemLoader(searchpath=self.templates_dir_path)
        template_environment = Environment(loader=loader)
        template = template_environment.get_template(self.template_filename)
        rendered_template = template.render(title='test111')
        return rendered_template

    def get_async_endpoint(self) -> Callable[..., Coroutine[Any, Any, str]]:
        template_rendered = self._get_template()

        async def form_endpoint() -> str:
            return template_rendered

        return form_endpoint
