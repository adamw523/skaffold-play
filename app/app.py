import sys, time
from flask import Flask, render_template

from flask import Flask, render_template
from flask import send_file
from io import BytesIO
import qrcode

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/test")
def test():
    return render_template("test.html")


@app.route("/qrcode")
def qrcode_render():
    img = qrcode.make("Adam was")

    img_io = BytesIO()
    img.save(img_io, "jpeg", quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg', attachment_filename="qrcode.jpeg")
