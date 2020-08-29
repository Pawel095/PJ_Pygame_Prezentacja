from abc import ABC, abstractmethod


class BaseSprite(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass
