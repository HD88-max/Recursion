def reversedString(string):


    if len(string) == 1:
        return string[0]
    
    firstchar = string[0]
    
    return reversedString(string[1:]) + firstchar

inputstring = input("Input string: ")
print(reversedString(inputstring))