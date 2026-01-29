from flask import Blueprint, render_template, request, redirect, url_for, flash
from manajemen_matkul_nilai.application.matkul_use_case import MatkulUseCase
from manajemen_matkul_nilai.application.nilai_use_case import NilaiUseCase
from manajemen_matkul_nilai.application.mahasiswa_use_case import MahasiswaUseCase

akademik_bp = Blueprint(
    "akademik",
    __name__,
    url_prefix="/akademik"
)

matkul_uc = MatkulUseCase()
nilai_uc = NilaiUseCase()
mahasiswa_uc = MahasiswaUseCase()


@akademik_bp.route("/dashboard")
def dashboard_dosen():
    matkul = matkul_uc.list_matkul()
    mahasiswa = nilai_uc.list_mahasiswa()
    return render_template(
        "akademik/dosen/dashboard.html",
        matkul=matkul,
        mahasiswa=mahasiswa
    )


@akademik_bp.route("/mahasiswa/<int:id>")
def dashboard_mahasiswa(id):
    nilai = nilai_uc.lihat_nilai_by_id(id)
    return render_template(
        "akademik/mahasiswa/dashboard.html",
        nilai=nilai
    )

@akademik_bp.route("/matkul/tambah", methods=["GET", "POST"])
def tambah_matkul():
    if request.method == "POST":
        try:
            matkul_uc.tambah_matkul (
                request.form.get("kode"),
                request.form.get("nama"),
                request.form.get("sks")
            )
            flash("Mata kuliah berhasil ditambahkan", "success")
            return redirect(url_for("akademik.dashboard_dosen"))

        except Exception as e:
            print("ERROR TAMBAH MATKUL:", e)
            flash(str(e), "error")

    return render_template("akademik/dosen/tambah_matkul.html")


@akademik_bp.route("/nilai/input", methods=["GET", "POST"])
def input_nilai():
    matkul = matkul_uc.list_matkul()
    mahasiswa = nilai_uc.list_mahasiswa()

    if request.method == "POST":
        try:
            nilai_uc.input_nilai(
                request.form.get("mahasiswa"),
                request.form.get("matkul_id"),
                request.form.get("nilai")
            )
            flash("Nilai berhasil disimpan", "success")
            return redirect(url_for("akademik.dashboard_dosen"))
        except Exception as e:
            flash(str(e), "error")

    return render_template(
        "akademik/dosen/input_nilai.html",
        matkul=matkul,
        mahasiswa=mahasiswa
    )

@akademik_bp.route("/mahasiswa/tambah", methods=["GET", "POST"])
def tambah_mahasiswa():
    if request.method == "POST":
        try:
            mahasiswa_uc.tambah_mahasiswa(
                request.form.get("nama")
            )
            flash("Mahasiswa berhasil ditambahkan", "success")
            return redirect(url_for("akademik.dashboard_dosen"))

        except Exception as e:
            flash(str(e), "error")

    return render_template("akademik/dosen/tambah_mahasiswa.html")

@akademik_bp.route("/matkul/edit/<int:id>", methods=["GET", "POST"])
def edit_matkul(id):
    if request.method == "POST":
        try:
            matkul_uc.update_matkul(
                id,
                request.form.get("kode"),
                request.form.get("nama"),
                request.form.get("sks")
            )
            flash("Mata kuliah berhasil diperbarui", "success")
            return redirect(url_for("akademik.dashboard_dosen"))
        except Exception as e:
            flash(str(e), "error")

    matkul = matkul_uc.get_matkul(id)
    return render_template("akademik/dosen/edit_matkul.html", matkul=matkul)

@akademik_bp.route("/matkul/hapus/<int:id>")
def hapus_matkul(id):
    matkul_uc.hapus_matkul(id)
    flash("Mata kuliah berhasil dihapus", "success")
    return redirect(url_for("akademik.dashboard_dosen"))

@akademik_bp.route("/mahasiswa/hapus/<int:id>")
def hapus_mahasiswa(id):
    mahasiswa_uc.hapus_mahasiswa(id)
    flash("Mahasiswa berhasil dihapus", "success")
    return redirect(url_for("akademik.dashboard_dosen"))

@akademik_bp.route("/nilai/hapus/<int:id>")
def hapus_nilai(id):
    nilai_uc.hapus_nilai(id)
    flash("Nilai berhasil dihapus", "success")
    return redirect(url_for("akademik.dashboard_dosen"))

@akademik_bp.route("/nilai/edit/<int:id>", methods=["GET", "POST"])
def edit_nilai(id):
    if request.method == "POST":
        try:
            nilai_uc.update_nilai(
                id,
                request.form.get("nilai")
            )
            flash("Nilai berhasil diperbarui", "success")
            return redirect(url_for("akademik.dashboard_dosen"))
        except Exception as e:
            flash(str(e), "error")

    nilai = nilai_uc.get_nilai(id)
    return render_template(
        "akademik/dosen/edit_nilai.html",
        nilai=nilai
    )
