from flask import Flask, render_template, redirect, request, url_for, send_file
#from cartoonize import cartoonize
from werkzeug.utils import secure_filename
import os
import cv2
import numpy as np

app = Flask(__name__, static_url_path=”/static”)

app.config["UPLOAD_FOLDER"] = 'static/images'

@app.route('/', methods = ["GET", "POST"])
def index():
    if request.method == "POST":
         if request.files["file"]:
                
            f = request.files["file"]
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            cartoonize(os.path.join(app.config["UPLOAD_FOLDER"], filename), os.path.join(app.config["UPLOAD_FOLDER"]))           
            return send_file(os.path.join(app.config["UPLOAD_FOLDER"], "test.png"), as_attachment = True)
    else:
        for img in os.listdir(app.config["UPLOAD_FOLDER"]):
            os.remove(os.path.join(app.config["UPLOAD_FOLDER"], img))
        return render_template("index.html")


def cartoonize(img, path):
    image = cv2.imread(img)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    gray = cv2.medianBlur(gray, 7) 
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 10)

    color = cv2.bilateralFilter(image, 12, 250, 250) 
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    grayImage = cv2.GaussianBlur(grayImage, (3, 3), 0)

    edgeImage = cv2.Laplacian(grayImage, -1, ksize=5)
    edgeImage = 255 - edgeImage

    ret, edgeImage = cv2.threshold(edgeImage, 150, 255, cv2.THRESH_BINARY)

    edgePreservingImage = cv2.edgePreservingFilter(image, flags=2, sigma_s=50, sigma_r=0.4)

    output =np.zeros(grayImage.shape)

    output = cv2.bitwise_and(edgePreservingImage, edgePreservingImage, mask=edgeImage)

    cartoon_image = cv2.stylization(image, sigma_s=150, sigma_r=0.25) 
    cv2.imwrite("./static/images/test.png", cartoon_image)
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

