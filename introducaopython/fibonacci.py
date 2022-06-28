print("fibonacci")

var = 1

while var > 0:
    var = int(input("digite o valor:"))

    # n + 1 = + n-1

    if var <=0:
        print("falso")
#repetir = falso
#brek

    a = 0
    b = 1
    c = a+b

    for n in range (a,var ):
        print (a)
        c = b + a
        a = b
        b = c
