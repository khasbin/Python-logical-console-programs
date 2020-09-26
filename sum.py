def summed(inp):
    digitList = []
    sume = 0
    charList = list(inp)
    for i in charList:
        digitList.append(int(i))
    length = len(digitList)

    for i in range(length):
            if i == 0:
                sume = pow(digitList[0], digitList[length-1])
            else:
                sume += pow(digitList[i], digitList[i - 1])

    return sume


x = input("Enter the required numbers: ")

print(summed(x))
