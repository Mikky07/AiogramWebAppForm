from typing import Callable, Coroutine

from starlette.applications import Starlette

from .webapp import WebServer


class WebServerImp(WebServer):
    def __init__(self):
        self.app = Starlette(debug=True)

    def add_endpoint(
            self,
            path: str,
            endpoint: Callable[..., Coroutine]
    ):
        self.app.add_route(
            path=path,
            route=endpoint,
            methods=['GET']
        )

    async def start_web_server(self):
        ...
