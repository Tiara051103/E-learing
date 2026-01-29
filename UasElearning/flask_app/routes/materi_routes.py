from flask import Blueprint, render_template, request, redirect, send_from_directory
from werkzeug.utils import secure_filename
import os

from manajemen_materi.infrastructure.sqlite_db.conek import get_connection
from manajemen_materi.infrastructure.sqlite_db.repositories.materi_repository_sqlite import (
    MateriRepositorySQLite
)
from manajemen_materi.application.usecase import MateriUseCase


materi_bp = Blueprint("materi", __name__, url_prefix="/materi")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'manajemen_materi', 'uploads')

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@materi_bp.route("/")
def index():
    return render_template(
        "pages/manajemen_materi/index.html",
        title="Manajemen Materi"
    )

@materi_bp.route("/dosen", methods=["GET", "POST"])
def dosen_materi():
    conn = get_connection()
    uc = MateriUseCase(MateriRepositorySQLite(conn))

    if request.method == "POST":
        file = request.files.get("file")
        filename = None  # default None

        if file and file.filename:
            # simpan nama file yang aman
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))

        # gunakan .get() untuk field opsional agar tidak error
        data = (
            request.form.get("matakuliah", ""),
            request.form.get("judul", ""),
            request.form.get("deskripsi", ""),
            request.form.get("tipe", ""),
            filename,  # ini yang akan menjadi m.file
            request.form.get("link", "")
        )

        uc.tambah(data)
        return redirect("/materi/dosen")

    materi = uc.lihat_semua()
    return render_template(
        "pages/manajemen_materi/dosen_materi.html",
        materi=materi
    )


@materi_bp.route("/siswa/matakuliah")
def siswa_matakuliah():
    uc = MateriUseCase(MateriRepositorySQLite(get_connection()))
    data = uc.lihat_semua()
    mk = sorted(set([m["matakuliah"] for m in data]))
    return render_template("pages/manajemen_materi/siswa_matakuliah.html", matakuliah=mk)


@materi_bp.route("/siswa/materi/<mk>")
def siswa_materi(mk):
    uc = MateriUseCase(MateriRepositorySQLite(get_connection()))
    data = uc.materi_per_matakuliah(mk)
    return render_template("pages/manajemen_materi/siswa_materi.html", materi=data)


@materi_bp.route("/download/<filename>")
def download(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

@materi_bp.route("/view/<filename>")
def view_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=False)


@materi_bp.route("/hapus/<int:id_materi>")
def hapus_materi(id_materi):
    uc = MateriUseCase(MateriRepositorySQLite(get_connection()))
    materi = uc.lihat_satu(id_materi)

    if not materi:
        return "Materi tidak ditemukan", 404

    if materi["file"]:
        path = os.path.join(UPLOAD_FOLDER, materi["file"])
        if os.path.exists(path):
            os.remove(path)

    uc.hapus(id_materi)
    return redirect("/materi/dosen")
