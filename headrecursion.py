def headrec(n,num):


    if n > num:
        return
    
    headrec(n+1, num)

    print(n)


input1 = int(input("Enter n to print numbers 1 to n: "))

headrec(1, input1)