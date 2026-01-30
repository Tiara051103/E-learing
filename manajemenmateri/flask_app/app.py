from flask import Flask, render_template, request, redirect, send_from_directory
from infrastructure.sqlite_db.conek import get_connection
from infrastructure.sqlite_db.repositories.materi_repository_sqlite import MateriRepositorySQLite
from application.usecase import MateriUseCase
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")


@app.route("/dosen/materi", methods=["GET","POST"])
def dosen_materi():
    conn = get_connection()
    uc = MateriUseCase(MateriRepositorySQLite(conn))

    if request.method == "POST":
        file = request.files["file"]
        filename = ""

        if file and file.filename:
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))

        data = (
            request.form["matakuliah"],
            request.form["judul"],
            request.form["deskripsi"],
            request.form["tipe"],
            filename,
            request.form["link"]
        )

        uc.tambah(data)
        return redirect("/dosen/materi")

    materi = uc.lihat_semua()
    return render_template("dosen_materi.html", materi=materi)

@app.route("/siswa/matakuliah")
def siswa_matakuliah():
    uc = MateriUseCase(
        MateriRepositorySQLite(get_connection())
    )
    data = uc.lihat_semua()
    mk = sorted(set([m["matakuliah"] for m in data]))
    return render_template("siswa_matakuliah.html", matakuliah=mk)

@app.route("/siswa/materi/<mk>")
def siswa_materi(mk):
    uc = MateriUseCase(
        MateriRepositorySQLite(get_connection())
    )
    data = uc.materi_per_matakuliah(mk)
    return render_template("siswa_materi.html", materi=data)

@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/view/<filename>")
def view_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=False)
@app.route("/hapus-materi/<int:id_materi>", methods=["GET"])
def hapus_materi(id_materi):
    conn = get_connection()
    uc = MateriUseCase(MateriRepositorySQLite(conn))

    # Ambil data materi dulu
    materi = uc.lihat_satu(id_materi)  # Pastikan MateriUseCase ada method lihat_satu(id)

    if not materi:
        # Materi tidak ditemukan
        return "Materi tidak ditemukan!", 404

    # Hapus file fisik jika ada
    if materi["file"] and os.path.exists(os.path.join(UPLOAD_FOLDER, materi["file"])):
        os.remove(os.path.join(UPLOAD_FOLDER, materi["file"]))
        print(f"File {materi['file']} berhasil dihapus.")

    # Hapus data dari database
    uc.hapus(id_materi)

    # Redirect ke halaman daftar materi dosen
    return redirect("/dosen/materi")

