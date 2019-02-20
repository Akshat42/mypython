def compare(a,b,c):
    if(a>b and a>c):
        return a
    if(b>a and b>c):
        return b
    
    return c

print(compare(5,10,-100))