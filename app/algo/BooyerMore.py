from .loader import *

def buildLast(pattern):
    #mencari last occurence character di pattern
    last = [-1 for i in range(128)]

    for i in range(len(pattern)):
        last[ord(pattern[i])] = i

    return last

def minInt(a, b):
    if (a<b ):
        return a
    else :
        return b

def boyerMooreMatch(text, pattern):
    last = buildLast(pattern)
    n = len(text)
    m = len(pattern)
    i = m-1

    if (i > n-1) :
        return -1
    
    j = m - 1
    while (i <= n-1):
        if (pattern[j] == text[i]):
            if (j == 0):
                return i
            else :
                i -= 1
                j -= 1
        else :
            lo = last[ord(text[i])] #last occurance
            i = i + m - minInt(j, 1+lo)
            j = m-1
    
    return -1

def findIdxBMMatch(arrOfText, pattern):
    #mengembalikan array of interger yang terdiri dari index ditemukan pattern
    idx = []
    pattern = pattern.lower()
    for i in range(len(arrOfText)):
        if (boyerMooreMatch(arrOfText[i].lower(), pattern) >= 0):
            idx.append(i)
    return(idx)

# ##test
# string = load()
# idx = findIdxBMMatch(string, "kasus")
# for i in idx:
#     print(string[i])

    