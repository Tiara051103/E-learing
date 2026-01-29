from ..sqlite_db.db_settings import get_connection
from ...domain.repositories.mahasiswa_repository import MahasiswaRepository

class MahasiswaRepositoryImpl(MahasiswaRepository):

    def get_all(self):
        conn = get_connection()
        rows = conn.execute(
            "SELECT id, nama FROM mahasiswa ORDER BY nama"
        ).fetchall()
        conn.close()
        return rows

    def add(self, nama):
        conn = get_connection()
        conn.execute(
            "INSERT INTO mahasiswa (nama) VALUES (?)",
            (nama,)
        )
        conn.commit()
        conn.close()
        
    def delete(self, id):
        with get_connection() as conn:
            conn.execute("DELETE FROM mahasiswa WHERE id=?", (id,))
