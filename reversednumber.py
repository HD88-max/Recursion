def reversedNumber(number):

    if number > 0:
        
        last = number % 10

        if number // 10 > 0:
            current_number = reversedNumber((int)(number // 10))
            return last * pow(10,len(str(current_number))) + current_number
        
        return number
    
inputnumber = int(input("Enter your number: "))
print("Reversed: ",reversedNumber(inputnumber))