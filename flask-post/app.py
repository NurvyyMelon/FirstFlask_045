from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    # Menampilkan form saat halaman pertama dibuka
    return render_template("index.html")


@app.route("/proses", methods=["POST"])
def proses():
    # Parsing parameter dari body request POST.
    # "nama" harus sama dengan atribut name pada TextField di index.html
    nama = request.form.get("nama", "").strip()

    if nama:
        hasil = f"Halo, {nama}!"
    else:
        hasil = "Nama tidak boleh kosong."

    return render_template("index.html", hasil=hasil, nama=nama)


if __name__ == "__main__":
    # debug=True hanya untuk tahap pengembangan
    app.run(debug=True)
