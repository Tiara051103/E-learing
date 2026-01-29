from ..infrastructure.services.matkul_repository_impl import MatkulRepositoryImpl

class MatkulUseCase:

    def __init__(self):
        self.repo = MatkulRepositoryImpl()

    def list_matkul(self):
        return self.repo.get_all()

    def tambah_matkul(self, kode, nama, sks):
        if not kode or not nama or not sks:
            raise ValueError("Semua field wajib diisi")

        sks = int(sks)
        if sks <= 0:
            raise ValueError("SKS harus lebih dari 0")

        try:
            self.repo.add(kode, nama, sks)
        except Exception as e:
            msg = str(e)
            if "mata_kuliah.kode" in msg:
                raise ValueError("Kode mata kuliah sudah terdaftar")
            if "mata_kuliah.nama" in msg:
                raise ValueError("Nama mata kuliah sudah terdaftar")
            raise

    def get_matkul(self, id):
        return self.repo.get_by_id(id)

    def update_matkul(self, id, kode, nama, sks):
        try:
            self.repo.update(id, kode, nama, int(sks))
        except Exception as e:
            raise ValueError("Kode atau nama mata kuliah sudah digunakan")

    def hapus_matkul(self, id):
        self.repo.delete(id)
