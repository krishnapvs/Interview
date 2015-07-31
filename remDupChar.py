'''Remove duplicate characters from a string. '''
def remDupChar(sent):
    temp=[]
    for i in sent:
        if i in temp:
            continue
        else:
            temp.append(i)
    return temp

a="This is a string, intended to be a sentence"
sent=[]
for i in a:
    sent.append(i)
sent=remDupChar(sent)
for i in sent:
    print i,

    
        
