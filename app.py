## flask app for hello world

from flask import Flask,request
import pandas as pd
import numpy as np

app=Flask( __name__)

@app.route('/',methods=['GET'])
def hello():
    return 'Helo World'

if __name__=='__main__':
    app.run(host="0.0.0.0",port=5000)


