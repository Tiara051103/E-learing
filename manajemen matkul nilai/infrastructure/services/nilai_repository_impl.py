from infrastructure.sqlite_db.db_settings import get_connection
from domain.repositories.nilai_repository import NilaiRepository

class NilaiRepositoryImpl(NilaiRepository):

    def get_all_mahasiswa(self):
        conn = get_connection()
        rows = conn.execute(
            "SELECT id, nama FROM mahasiswa ORDER BY nama"
        ).fetchall()
        conn.close()
        return rows

    def get_by_mahasiswa_id(self, mahasiswa_id):
     with get_connection() as conn:
        rows = conn.execute("""
            SELECT n.id, mk.nama, n.nilai
            FROM nilai n
            JOIN mata_kuliah mk ON n.matkul_id = mk.id
            WHERE n.mahasiswa = (
                SELECT nama FROM mahasiswa WHERE id = ?
            )
        """, (mahasiswa_id,)).fetchall()
     return rows

    def get_by_id(self, id):
        with get_connection() as conn:
            return conn.execute(
                "SELECT id, nilai FROM nilai WHERE id = ?",
                (id,)
            ).fetchone()
            
    
    def add(self, mahasiswa, matkul_id, nilai):
        conn = get_connection()
        conn.execute(
            "INSERT INTO nilai (mahasiswa, matkul_id, nilai) VALUES (?,?,?)",
            (mahasiswa, matkul_id, nilai)
        )
        conn.commit()
        conn.close()
        
    def update(self, id, nilai):
        with get_connection() as conn:
            conn.execute(
                "UPDATE nilai SET nilai = ? WHERE id = ?",
                (nilai, id)
            )

    def delete(self, id):
     with get_connection() as conn:
        conn.execute("DELETE FROM nilai WHERE id=?", (id,))
