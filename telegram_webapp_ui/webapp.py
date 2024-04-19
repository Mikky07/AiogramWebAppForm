from typing import List, Union

from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles

from telegram_webapp_ui.abc import UIWidget


class WebAppUI:
    def __init__(
            self,
            *widgets: UIWidget,
            bot_token: str,
            base_url: str = "/webapp"
    ):
        self.widgets = widgets
        self.bot_token = bot_token
        self.base_url = base_url
        self.routes: List[Union[Route, Mount]] = []
        self.init_routes()

    def init_routes(self):
        widget_ids = tuple(widget.widget_url for widget in self.widgets)
        for widget in self.widgets:
            if widget_ids.count(widget.widget_url) > 1:
                raise Exception("Duplicate widget paths detected")
            route = Route(
                path=widget.widget_url,
                endpoint=widget.get_async_endpoint(),
            )
            self.routes.append(route)
        self.routes.append(
            Mount(
                '/statics',
                app=StaticFiles(packages=['telegram_webapp_ui']),
                name="statics"
            )
        )

    def mount(self, app: Starlette):
        webapp = Starlette(
            routes=self.routes,
            debug=True
        )
        app.mount(
            path=self.base_url,
            app=webapp
        )
