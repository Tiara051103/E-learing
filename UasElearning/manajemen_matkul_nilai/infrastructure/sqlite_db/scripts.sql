-- =========================
-- TABEL MAHASISWA
-- =========================
CREATE TABLE IF NOT EXISTS mahasiswa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT NOT NULL UNIQUE
);

-- =========================
-- TABEL MATA KULIAH
-- =========================
CREATE TABLE IF NOT EXISTS mata_kuliah (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kode TEXT NOT NULL UNIQUE,
    nama TEXT NOT NULL UNIQUE,
    sks INTEGER NOT NULL CHECK (sks > 0)
);

-- =========================
-- TABEL NILAI
-- =========================
CREATE TABLE IF NOT EXISTS nilai (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mahasiswa TEXT NOT NULL,
    matkul_id INTEGER NOT NULL,
    nilai REAL NOT NULL CHECK (nilai >= 0 AND nilai <= 100),

    FOREIGN KEY (mahasiswa) REFERENCES mahasiswa(nama),
    FOREIGN KEY (matkul_id) REFERENCES mata_kuliah(id)
);
