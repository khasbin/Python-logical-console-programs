def shifting(inp):
    newlist = list(inp)
    for i,j in enumerate(newlist):
        if (i+1)%4 == 0:
            temp1 =  newlist[i-2]
            temp2 = newlist[i-3] 
            newlist[i-2] = newlist[i]
            newlist[i-3] = newlist[i-1]
            newlist[i-1] = temp2
            newlist[i]   = temp1
    
    return newlist

x = input("Enter the string: ")
print(shifting(x))
