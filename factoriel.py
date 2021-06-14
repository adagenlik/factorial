def factorialcalculate(number):
    factor=1
    i=1
    while(i<=number):
        factor=factor*i
        i=i+1
    print(number,"Factoriel is =",factor)
    print(len(str(factor)),"digits")

x=int(input("Write Your Number:"))
factorialcalculate(x)