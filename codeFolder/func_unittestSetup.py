
def add(x,y):
    return x+y

def mult(x,y):
    return x*y

def div(x,y):
    if (x==0) or (y==0):
        raise ValueError('Numerator and/or denominator must not be zero')
    else:
        return x/y