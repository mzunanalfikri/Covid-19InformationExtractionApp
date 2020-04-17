from app import app
from flask import render_template, request
from .algo.BooyerMore import *
from .algo.loader import *
from .algo.KMP import *

@app.route('/', methods =['GET','POST'])
def match_app():
    contents = "Kosong"
    string = []
    idx = []
    if (request.method == 'POST'):
        input_file = request.files['fileInput']
        input_pattern = request.form['patternInput']
        contents = input_file.read()
        contents = contents.decode('utf-8')
        contents = contents.replace('\n', '')
        string = contents.split('.')
        print(string)
        idx = findIdxBMMatch(string, input_pattern)
        print(idx)
        # print(teks_input_html)
    
    return render_template("match_app.htm", teks = contents, string = string, idx = idx)

def hasil():
    input_html = request.form['textInput']
    print(input_html)
    return render_template("match_app.htm")
    
@app.route('/dokumentasi')
def dokumentasi():
    return render_template("dokumentasi.htm")