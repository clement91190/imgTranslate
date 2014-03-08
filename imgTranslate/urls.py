# -*-coding:Utf-8 -*
#from flask import request
from imgTranslate import app
import json
from decaf.scripts.imagenet import DecafNet
import PIL
import numpy as np

net = DecafNet('../imagenet_pretrained/imagenet.decafnet.epoch90', '../imagenet_pretrained/imagenet.decafnet.meta')
img = PIL.Image.open('../image/apple.jpg')
img  = np.array(img.getdata(), dtype='uint8').reshape(img.size[0], img.size[1], 3)

# Worker functions

@app.route('/analyse', methods=['POST', 'GET'])
def analyse():
    scores = net.classify(img)
    str =  "{}".format(net.top_k_prediction(scores, 5))
    return json.dumps(str)

