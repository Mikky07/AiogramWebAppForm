from abc import ABC, abstractmethod
from typing import Callable, Coroutine

from app.web_server import StarletteWebServer


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


async def validate():
    ...


class WebAppUI:
    def __init__(
            self,
            *widgets: UIWidget,
            bot_token: str,
            web_server: type[WebServer] = StarletteWebServer,
    ):
        self.widgets = widgets
        self.bot_token = bot_token
        self.web_server = web_server()

    def _init_web_app(self):
        widget_ids = tuple(widget.widget_id for widget in self.widgets)
        for widget in self.widgets:
            if widget_ids.count(widget.widget_id) > 1:
                raise Exception("duplicate ids detected")
            self.web_server.add_endpoint(
                path=widget.widget_id,
                endpoint=widget.get_async_endpoint()
            )

    def __call__(self):
        self._init_web_app()
        app = self.web_server.get_app()
        return app
