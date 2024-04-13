from typing import Callable, Coroutine

from .webapp import WebServer


class WebServerImp(WebServer):
    def __init__(self):
        ...

    def add_endpoint(self, path: str, endpoint: Callable[..., Coroutine]):
        ...

    async def start_web_server(self):
        ...
