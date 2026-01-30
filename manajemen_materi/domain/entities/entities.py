class Materi:
    def __init__(self, id, matakuliah, judul, deskripsi, tipe, file, link):
        self.id = id
        self.matakuliah = matakuliah
        self.judul = judul
        self.deskripsi = deskripsi
        self.tipe = tipe      # file | link | video
        self.file = file
        self.link = link
