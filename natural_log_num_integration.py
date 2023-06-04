import decimal

arg = int(input("What number do you want to take the natural logarithm of? : "))
dtr = int(input("The reciprocal of what number should be the length of dt? : "))
dt = 1/dtr

def func(t):
    tout = 1/t
    return tout

def integration(upper, dif, difr):
    log = 0
    for i in range(1, (upper-1)*difr):
        log += func(1 + i*dif)
    return log*dif
print(integration(arg, dt, dtr))