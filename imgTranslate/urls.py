# -*-coding:Utf-8 -*
#from flask import request
from imgTranslate import app
import json
from decaf.scripts.imagenet import DecafNet
import PIL
import numpy as np
from wtforms import Form, FileField
from flask import render_template, request

net = DecafNet('../imagenet_pretrained/imagenet.decafnet.epoch90', '../imagenet_pretrained/imagenet.decafnet.meta')
img = PIL.Image.open('../image/apple.jpg')
img = np.array(img.getdata(), dtype='uint8').reshape(img.size[0], img.size[1], 3)


# Worker functions
@app.route('/analyse', methods=['POST', 'GET'])
def analyse():
    scores = net.classify(img)
    str = "{}".format(net.top_k_prediction(scores, 5))
    return json.dumps(str)


def analyse_pic(img):
    img = np.array(img.getdata(), dtype='uint8').reshape(img.size[0], img.size[1], 3)
    scores = net.classify(img, center_only=False)
    str = "{}".format(sorted(scores)[-5:])
    res = net.top_k_prediction(scores, 5)
    l = res[1]
    for s in l:
        str += '<p>' + s 

    return str
   

class ImageForm(Form):
    file = FileField('upload an image to test this !')

ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/testpost', methods=['POST', 'GET'])
def test():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            return analyse_pic(PIL.Image.open(file))
    return """
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
    <p><input type=file name=file>
    <input type=submit value=Upload>
    </form>
    """
