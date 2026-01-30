from abc import ABC, abstractmethod

class NilaiRepository(ABC):

    @abstractmethod
    def get_all_mahasiswa(self): pass

    @abstractmethod
    def get_by_mahasiswa_id(self, mahasiswa_id): pass

    @abstractmethod
    def add(self, mahasiswa, matkul_id, nilai): pass
    
    @abstractmethod
    def get_by_id(self, id): pass

    @abstractmethod
    def delete(self, id): pass
