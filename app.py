from flask import Flask
from algo.KMP import *
from algo.Booyer-More import *

app = Flask(__name__)

@app.route('/')
def halo() :
    return "Halo Kamu!"

if __name__ == '__main__':
    app.run()
