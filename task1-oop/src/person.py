from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_role(self):
        pass
