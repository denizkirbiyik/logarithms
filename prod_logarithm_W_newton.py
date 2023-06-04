import decimal

inputZ = float(input("What value of the Principal Lambert W Function(Product Logarithm) would you like to compute? : "))
inf1 = int(input("What number should be substituted for infinity in the limit? : "))
iter1 = int(input("How many iterations of the algorithm do you want to compute? : "))
start = 5

def e_def(inf):
    e = ((1+(1/decimal.Decimal(inf)))**inf);
    return e
euler = e_def(inf1)

def newton_raphson(z, w):
    f = w - ((w*(euler**w))-decimal.Decimal(z))/((euler**w)*(w+1))
    return f
def lambert(input, guess, iter):
    in1 = input
    out1 = guess
    for i in range(iter):
        out1 = newton_raphson(in1, out1)
    return out1
print(lambert(inputZ, start, iter1))

