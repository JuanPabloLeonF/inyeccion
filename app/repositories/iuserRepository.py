from abc import ABC, abstractmethod

class IUserRepository(ABC):

    @abstractmethod
    def getAll(self):
        pass