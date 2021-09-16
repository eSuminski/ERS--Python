from abc import ABC, abstractmethod


class Login(ABC):

    @abstractmethod
    def login(self, username: str, password: str):
        pass

