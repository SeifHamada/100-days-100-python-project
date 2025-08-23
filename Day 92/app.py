from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import cv2
import numpy as np
from sklearn.cluster import KMeans
from collections import Counter

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(int(rgb[0]), int(rgb[1]), int(rgb[2]))


def get_top_colors(image_path, n_colors=10):

    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img = cv2.resize(img, (200, 200), interpolation=cv2.INTER_AREA)

    pixels = img.reshape((-1, 3))

    kmeans = KMeans(n_clusters=n_colors, random_state=42)
    labels = kmeans.fit_predict(pixels)

    counts = Counter(labels)
    center_colors = kmeans.cluster_centers_

    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [rgb_to_hex(color) for color in ordered_colors]

    return hex_colors


@app.route("/", methods=["GET", "POST"])
def index():
    colors = None
    if request.method == "POST":
        if "file" not in request.files:
            return "No file part"
        file = request.files["file"]
        if file.filename == "":
            return "No selected file"
        if file:
            filename = secure_filename(file.filename)
            path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(path)

            colors = get_top_colors(path, n_colors=10)

    return render_template("index.html", colors=colors)


if __name__ == "__main__":
    app.run(debug=True)
