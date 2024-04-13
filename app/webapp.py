from abc import ABC, abstractmethod
from typing import Callable, Coroutine


class UIWidget(ABC):
    @abstractmethod
    def get_async_endpoint(self) -> Callable[..., Coroutine]:
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
    def __init__(self, *widgets: UIWidget):
        self.widgets = widgets

    def _init_web_app(self):
        ...

    def start(self):
        ...
