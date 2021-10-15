from flask import Flask, render_template, redirect, request, url_for, send_file
from cartoonize import cartoonize
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = 'static/images'

@app.route('/')
def index():
    # if request.method == "GET":
    #     if not os.path.exists(app.config["UPLOAD_FOLDER"]):
    #         os.mkdir(app.config["UPLOAD_FOLDER"])
    #     for img in os.listdir(app.config["UPLOAD_FOLDER"]):
    #         os.remove(os.path.join(app.config["UPLOAD_FOLDER"], img))
    #     return render_template("home.html")
    return render_template("index.html")

# @app.route('/file', methods = ["POST"])
# def file():
#     if request.method == "POST":
#         print(request.files["file"])
#         if request.files["file"]:
            
#             f = request.files["file"]
#             filename = secure_filename(f.filename)
#             f.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
#             cartoonize(os.path.join(app.config["UPLOAD_FOLDER"], filename), os.path.join(app.config["UPLOAD_FOLDER"]))           
#             return send_file(os.path.join(app.config["UPLOAD_FOLDER"], "test.png"), as_attachment = True)
#     return redirect(url_for('index'))
