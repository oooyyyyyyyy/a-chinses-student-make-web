import os

import requests

from flask import Flask, render_template, url_for, request, jsonify

import datetime

from time import sleep





app = Flask(__name__)




@app.route('/')

def index (name=None):

    time = datetime.datetime.now()

    time = time.strftime('%Y %m %d %H:%M:%S')

    return render_template('index.html',name=name,time=time)



if __name__ == '__main__':

    app.run(port=23333,debug=False)

