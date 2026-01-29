class MateriRepositorySQLite:
    def __init__(self, conn):
        self.conn = conn

    def get_all(self):
        return self.conn.execute(
            "SELECT * FROM materi"
        ).fetchall()

    def get_by_matakuliah(self, mk):
        return self.conn.execute(
            "SELECT * FROM materi WHERE matakuliah = ?", (mk,)
        ).fetchall()

    def get_by_id(self, id):
        return self.conn.execute(
            "SELECT * FROM materi WHERE id = ?", (id,)
        ).fetchone()

    def add(self, data):
        self.conn.execute("""
            INSERT INTO materi 
            (matakuliah, judul, deskripsi, tipe, file, link)
            VALUES (?, ?, ?, ?, ?, ?)
        """, data)
        self.conn.commit()

    def update(self, data):
        self.conn.execute("""
            UPDATE materi SET
            matakuliah=?, judul=?, deskripsi=?, tipe=?, file=?, link=?
            WHERE id=?
        """, data)
        self.conn.commit()

    def delete(self, id):
        self.conn.execute(
            "DELETE FROM materi WHERE id=?", (id,)
        )
        self.conn.commit()

    def hapus(self, id_materi):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM materi WHERE id = ?", (id_materi,))
        self.conn.commit()

    def lihat_satu(self, id_materi):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM materi WHERE id = ?", (id_materi,))
        row = cur.fetchone()
        if row:
            return {
                "id": row[0],
                "matakuliah": row[1],
                "judul": row[2],
                "deskripsi": row[3],
                "tipe": row[4],
                "file": row[5],
                "link": row[6]
            }
        return None