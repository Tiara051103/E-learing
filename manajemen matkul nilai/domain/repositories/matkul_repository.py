from abc import ABC, abstractmethod

class MatkulRepository(ABC):

    @abstractmethod
    def get_all(self): 
        pass

    @abstractmethod
    def add(self, kode, nama, sks):
        pass
    
    @abstractmethod
    def get_by_id(self, id): pass

    @abstractmethod
    def update(self, id, kode, nama, sks): pass

    @abstractmethod
    def delete(self, id): pass
