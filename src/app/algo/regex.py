import re

def regexMatch(text, pattern):
    hasil = re.findall(pattern.lower(), text.lower())
    return (len(hasil) > 0)

def findIdxRegexMatch(arrOfText, pattern):
    #mengembalikan array of integer yang terdapat pattern
    idx = []
    pattern = pattern.lower()
    for i in range(len(arrOfText)):
        if (regexMatch(arrOfText[i].lower(), pattern)):
            idx.append(i)
    return(idx)

# string = load("../../test/berita1.txt")
# # print (string)
# idx = findIdxRegexMatch(string, "kasus")
# for i in idx:
#     print(string[i])

