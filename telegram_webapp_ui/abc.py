from abc import ABC, abstractmethod
from typing import Callable, Coroutine


class UIWidget(ABC):
    def __init__(self, widget_url: str):
        self.widget_url = widget_url

    @abstractmethod
    def get_async_endpoint(self) -> Callable[..., Coroutine]:
        raise NotImplementedError
