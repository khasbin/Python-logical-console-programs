def logic(inp):
    l = len(inp)
    x = int((l/2))
    a = int(inp[x])
    final = 1
    count = x
    if l%2 == 0:
        for i in range(0,l):
            if count > 0:
                count-=1
                final *= int(inp[i])*int(inp[l-1-i])
    else: 
        for i in range(0,l):
            if count > 0: 
                count -=1
                final *= int(inp[i])*int(inp[l-1-i])
        final = final +a
    
    return counter(final)
    
def counter(x):
    y = str(x)
    if len(y)>1:
        return logic(y)
    else:
        return int(y)
        

b = input("Enter the required number: ")
print(logic(b))