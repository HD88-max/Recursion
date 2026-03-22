def power_of_2(n):
    
    if n == 1:
        return True
    if n == 0 or n % 2 != 0:
        return False
    
    
    return power_of_2(n // 2)



num = int(input("Enter a number: "))

if power_of_2(num):
    print("Power of 2")
else:
    print("Not a power of 2")