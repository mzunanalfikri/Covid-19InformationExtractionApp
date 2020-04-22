import re

def extractAmount(string, pattern):
    # reg = r"(?i)(?:\b" + pattern + "\D{0,20})(\s[0-9][0-9,.]*\s)[^.,]|([0-9][0-9,.]*)[^.,](?:\D{0,20}" + pattern + ")"
    # reg = r"(?:(?<!\S)(\d+(?:,\d+)?)(?!\S)\D*\b" + pattern + "|" + pattern + "\D*(?<!\S)(\d+(?:,\d+)?)(?!\S))"
    pattern = pattern.lower()
    reg = r"([0-9][0-9.,]*)(?:[\s*\D*]*" + pattern + ")|(?:" + pattern + "[\s*\D*]*)([0-9][0-9.,]*)"
    res = re.findall(reg, string)
    amount = ""
    if (len(res) == 1):
        if (res[0][0] != ""):
            amount = res[0][0]
        else :
            amount = res[0][1]
    return (amount)

def extractTimeStr(string):
    reg = r"(Senin|Selasa|Rabu|Kamis|Jumat|Sabtu)[\s\d\D]+(WIB|2020)|(0?[1-9]|[12][0-9]|3[01])[-/](0?[1-9]|1[012])[-/](\d{4}|\d{2})|[0-9]+[\s\D]+2020"
    res = re.search(reg, string)
    time =""
    if (res is None):
        time = ""
    else :
        time = res.group()
    return time

def extractTimeTeks(arrOfString):
    res =""
    for teks in arrOfString:
        res = extractTimeStr(teks)
        if (res != ""):
            return res
    return res

def resultExtraction(text, arrOfString, idx, pattern):
    #hasil : [[index, tanggal, jumlah]]
    result = []
    #cari tanggal di keselurihan berita
    tanggal_berita = extractTimeTeks(arrOfString)
    # tanggal_berita = ""
    for i in idx:
        tanggal_kalimat = extractTimeStr(arrOfString[i])
        if (tanggal_kalimat == ""):
            if (tanggal_berita == ""):
                tanggal_kalimat = "Tidak ada tanggal"
            else :
                tanggal_kalimat = tanggal_berita
        amount = extractAmount(arrOfString[i].lower().replace("covid-19", ""), pattern)
        result.append([i, tanggal_kalimat, amount])
    return result
        

