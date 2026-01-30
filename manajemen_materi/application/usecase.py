class MateriUseCase:
    def __init__(self, repo):
        self.repo = repo

    # GURU
    def lihat_semua(self):
        return self.repo.get_all()

    def tambah(self, data):
        self.repo.add(data)

    def edit(self, data):
        self.repo.update(data)

    def hapus(self, id):
        self.repo.delete(id)

    # SISWA
    def materi_per_matakuliah(self, mk):
        return self.repo.get_by_matakuliah(mk)

    def lihat_satu(self, id_materi):
        return self.repo.lihat_satu(id_materi)