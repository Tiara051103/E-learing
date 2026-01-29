from ..sqlite_db.db_settings import get_connection
from ...domain.repositories.matkul_repository import MatkulRepository
from ...domain.entities.akademik_entities import MataKuliah



class MatkulRepositoryImpl(MatkulRepository):

   
    def get_all(self):
        with get_connection() as conn:
            rows = conn.execute(
                "SELECT id, kode, nama, sks FROM mata_kuliah"
            ).fetchall()

        return [
            MataKuliah(
                id=row[0],
                kode=row[1],
                nama=row[2],
                sks=row[3]
            )
            for row in rows
        ]


    def add(self, kode, nama, sks):
        with get_connection() as conn:
            conn.execute(
                "INSERT INTO mata_kuliah (kode, nama, sks) VALUES (?,?,?)",
                (kode, nama, sks)
            )

    def get_by_id(self, id):
        with get_connection() as conn:
            return conn.execute(
                "SELECT id, kode, nama, sks FROM mata_kuliah WHERE id=?",
                (id,)
            ).fetchone()

    def update(self, id, kode, nama, sks):
        with get_connection() as conn:
            conn.execute(
                """
                UPDATE mata_kuliah
                SET kode=?, nama=?, sks=?
                WHERE id=?
                """,
                (kode, nama, sks, id)
            )
    def delete(self, id):
        with get_connection() as conn:
            conn.execute("DELETE FROM mata_kuliah WHERE id=?", (id,))

