from abc import ABC, abstractmethod

class MahasiswaRepository(ABC):

    @abstractmethod
    def get_all(self): pass

    @abstractmethod
    def add(self, nama): pass

    @abstractmethod
    def delete(self, id): pass
