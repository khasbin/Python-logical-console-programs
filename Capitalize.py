def capitalize(inp):
    x = inp.split(" ")
    newlist =""
    for words in x:
        newlist += (words.capitalize())

    return (newlist)


a = input("Enter the required sentence: ")
print(capitalize(a))

