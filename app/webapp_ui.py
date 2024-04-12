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


class WebAppUI:
    def __init__(self, *widgets: UIWidget, title: str):
        self.widgets = widgets

    def _init_web_app(self):
        ...

    def start(self):
        ...
