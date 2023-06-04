import decimal

inputZ = decimal.Decimal(input("What value of the Principal Lambert W Function(Product Logarithm) would you like to compute? : "))
inf1 = int(input("What number should be substituted for infinity in the limit? : "))
iter1 = int(input("How many iterations of the algorithm do you want to compute? : "))
start = 5

def exp(x, inf):
    e_x = ((1+(x/decimal.Decimal(inf)))**inf);
    return e_x

def halley(in1, inZ, inf2):
    f = exp(in1, inf2)
    x = in1
    xf = x - (2*f*(x*f-inZ)*(x+1))/(f*(2*f*((x+1)**2)-x*f+inZ*f*(x+2)))
    return xf

def compf(input, infty, guess, iter):
    W = guess
    for i in range(iter):
        W = halley(W, input, infty)
    return W
print(compf(inputZ, inf1, start, iter1))
