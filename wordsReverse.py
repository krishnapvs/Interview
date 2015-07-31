def wordsReverse(S):
    temp = S.split(" ")
    temp.reverse()
    S=""
    for i in temp:
        S=S+ ' ' + i
    return S[1:]



a="This is a trial sentence"
print wordsReverse(a)
