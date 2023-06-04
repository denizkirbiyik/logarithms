import decimal

inputZ = decimal.Decimal(input("What value of the Natural Logarithm would you like to compute? : "))
inf1 = int(input("What number should be substituted for infinity in the limit? : "))
iter1 = int(input("How many iterations of the algorithm do you want to compute? : "))
start = 5

def exp(x, inf):
    e = ((1+(x/decimal.Decimal(inf)))**inf);
    return e

def newton_raphson(z, x):
    f = exp(x, inf1)
    l = x + z/f - 1
    return l
def log(input, guess, iter):
    in1 = input
    out1 = guess
    for i in range(iter):
        out1 = newton_raphson(in1, out1)
    return out1
print(log(inputZ, start, iter1))

