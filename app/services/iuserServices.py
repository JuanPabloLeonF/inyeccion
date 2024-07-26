from abc import ABC, abstractmethod

class IUserServices(ABC):

    @abstractmethod
    def getAll(self):
        pass
