#kmp biasanya bagus buat string yang banyak characternya sama
def computeFail(pattern):
    fail = [0 for i in range(len(pattern))];

    m = len(pattern)
    j = 0
    i = 1

    while (i<m):
        if (pattern[j] == pattern[i]):
            fail[i] = j+1
            i = i + 1
            j = j + 1
        elif(j>0):
            j = fail[j-1]
        else :
            fail[i] = 0
            i = i + 1
    return fail

def kmpMatch(text, pattern):
    n = len(text)
    m = len(pattern)

    fail = computeFail(pattern)

    i = 0
    j = 0
    while (i < n):
        if (pattern[j] == text[i]):
            if (j == m-1):
                return i-m+1
            i+=1
            j+=1
        elif (j > 0):
            j = fail[j-1]
        else:
            i+=1
    return -1

def findIdxKMPMatch(arrOfText, pattern):
    #mengembalikan array of interger yang terdiri dari index ditemukan pattern
    idx = []
    pattern = pattern.lower()
    for i in range(len(arrOfText)):
        if (kmpMatch(arrOfText[i].lower(), pattern) >= 0):
            idx.append(i)
    return(idx)

##test
# string = load()
# idx = findIdxKMPMatch(string, "kasus")
# for i in idx:
#     print(string[i])

        

