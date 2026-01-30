from infrastructure.services.mahasiswa_repository_impl import MahasiswaRepositoryImpl

class MahasiswaUseCase:

    def __init__(self):
        self.repo = MahasiswaRepositoryImpl()

    def list_mahasiswa(self):
        return self.repo.get_all()

    def tambah_mahasiswa(self, nama):
        if not nama:
            raise ValueError("Nama mahasiswa wajib diisi")
        self.repo.add(nama)

    def hapus_mahasiswa(self, id):
        self.repo.delete(id)
