from dataclasses import dataclass

@dataclass
class Mahasiswa:
    id: int
    nama: str

@dataclass
class MataKuliah:
    id: int
    kode: str
    nama: str
    sks: int

@dataclass
class Nilai:
    id: int
    mahasiswa: str
    matkul: str
    nilai: float
