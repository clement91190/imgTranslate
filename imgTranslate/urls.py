# -*-coding:Utf-8 -*
#from flask import request
from imgTranslate import app
import json


# Worker functions
@app.route('/analyse', methods=['POST', 'GET'])
def analyse():
    return json.dumps("tree")

