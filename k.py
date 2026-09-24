
from flask import Flask
from pathlib import Path
from flask import render_template, url_for, request, redirect

BASE_DIR = Path(__file__).resolve().parent
SAVE_PATH = BASE_DIR / "saves"


# настрока сервера
app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template("index.html")

@app.route('/send/str', methods=["POST"])
def uplload_string():
    data = request.form.get("text_data")
    print(f"data -> {data}")

    with open(SAVE_PATH / "text" / "main.txt", mode="a", encoding="utf-8") as f:
        f.write(data + "\n")

    return redirect(url_for("main_page"))

@app.route("/send/file", methods=["POST"])
def upload_file():
    file = request.files
    if len(file) > 1:
        print("Можно прикрепить только один файл.")

    file_obj = file.get("file")
    file_name = file_obj.filename

    print(file_name)

    file_obj.save(SAVE_PATH / file_name)
    return redirect(url_for("main_page"))




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
