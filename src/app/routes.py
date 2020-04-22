from app import app
from flask import render_template, request
from nltk import tokenize
from .algo.regex import *
from .algo.BooyerMore import *
from .algo.KMP import *
from .algo.extractor import *

@app.route('/', methods =['GET','POST'])
def match_app():
    contents = "Kosong"
    arr_teks = []
    idx = []
    input_algo = "-"
    input_pattern = ""
    isValid = -1
    result = []
    if (request.method == 'POST' ):
        input_file = request.files['fileInput']
        contents = input_file.read()
        #validasi input, asumsi valid jika panjang caracter > 10
        if ((len(request.values) >= 2) and (len(contents)>10)):
            isValid = 1
        else : 
            isValid = 0
        
        if (isValid == 1):
            # input_file = request.files['fileInput']         #dalam bentuk file
            input_pattern = request.form['patternInput']    #dalam bentuk string
            input_algo = request.form['algoInput']          #dalam bentuk string

            # print(input_algo)
            # contents = input_file.read()
            contents = contents.decode('utf-8')
            contents = contents.replace('\n', '')
            arr_teks = tokenize.sent_tokenize(contents)
            # print(string)
            if (input_algo == "KMP"):
                idx = findIdxKMPMatch(arr_teks, input_pattern)
            elif (input_algo == "BM"):
                idx = findIdxBMMatch(arr_teks, input_pattern)
            else :
                #regex
                idx = findIdxRegexMatch(arr_teks, input_pattern)
            # print(teks_input_html)
            result = resultExtraction(contents, arr_teks, idx, input_pattern)
            
    return render_template("match_app.htm", isValid = isValid, teks = contents, arr_teks = arr_teks, idx = idx, algo = input_algo, pattern = input_pattern, result = result)

def hasil():
    input_html = request.form['textInput']
    print(input_html)
    return render_template("match_app.htm")
    
@app.route('/dokumentasi')
def dokumentasi():
    return render_template("dokumentasi.htm")