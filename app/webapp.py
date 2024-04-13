from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Callable, Coroutine, Any

Template = TypeVar('Template')


class UIWidget(ABC, Generic[Template]):
    @abstractmethod
    def _get_template(self) -> Template:
        raise NotImplementedError

    @abstractmethod
    def get_async_endpoint(self) -> Callable[..., Coroutine[Any, Any, Template]]:
        raise NotImplementedError


class WebServer(ABC):
    @abstractmethod
    async def start_web_server(self):
        raise NotImplementedError

    @abstractmethod
    async def add_endpoint(self, path: str, endpoint: Callable[..., Coroutine]):
        raise NotImplementedError


async def validate():
    ...


class WebAppUI:
    def __init__(self, *widgets: UIWidget, title: str):
        self.widgets = widgets

    def _init_web_app(self):
        ...

    def start(self):
        ...
