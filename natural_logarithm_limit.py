import decimal

arg = int(input("What number do you want to take the natural logarithm of? : "))
inf1 = int(input("What number should be substituted for infinity in the limit? : "))

def log(x, inf):
    return inf*decimal.Decimal((x)**(1/inf)-1)

print(log(arg, inf1))