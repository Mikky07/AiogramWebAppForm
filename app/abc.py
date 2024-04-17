from abc import ABC, abstractmethod
from typing import Callable, Coroutine


class UIWidget(ABC):
    def __init__(self, widget_id: str):
        self.widget_id = widget_id

    @abstractmethod
    def get_async_endpoint(self) -> Callable[..., Coroutine]:
        raise NotImplementedError


class WebServer(ABC):
    @abstractmethod
    async def get_app(self):
        raise NotImplementedError

    @abstractmethod
    async def add_endpoint(self, path: str, endpoint: Callable[..., Coroutine]):
        raise NotImplementedError
