x = ("AAAAXXXXQQEEEmmm")
a = (x.upper())
y = list(a)
length = len(a)
countlist = []
newlist = []
count = 1
for i in range(1, length):
    if y[i-1] == y[i]:
        count += 1
    else:
        newlist.append(y[i-1])
        countlist.append(count)
        count = 1
countlist.append(count)
newlist.append(y[length-1])
s = newlist
le = len(countlist)
finallist = []
for i in range(0, le):
    finallist.append(countlist[i])
    finallist.append(s[i])
    
finalval = "".join(map(str,finallist))
print(finalval)
    
        
        

