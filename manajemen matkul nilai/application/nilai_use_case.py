from infrastructure.services.nilai_repository_impl import NilaiRepositoryImpl

class NilaiUseCase:
    def __init__(self):
        self.repo = NilaiRepositoryImpl()

    def list_mahasiswa(self):
        return self.repo.get_all_mahasiswa()

    def lihat_nilai_by_id(self, mahasiswa_id):
        return self.repo.get_by_mahasiswa_id(mahasiswa_id)

    def input_nilai(self, mahasiswa, matkul_id, nilai):
        nilai = float(nilai)
        if nilai < 0 or nilai > 100:
            raise ValueError("Nilai harus antara 0 - 100")
        self.repo.add(mahasiswa, int(matkul_id), nilai)
    
    def get_nilai(self, id):
        return self.repo.get_by_id(id)

    def update_nilai(self, id, nilai):
        nilai = float(nilai)
        if nilai < 0 or nilai > 100:
            raise ValueError("Nilai harus antara 0 - 100")
        self.repo.update(id, nilai)

    def hapus_nilai(self, id):
        self.repo.delete(id)

