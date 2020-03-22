def recf(n):
    r = (4/(2*n-1)*(-1)**(1-n))
    if n == 0:
        r = 0
    elif n == 1:
        r = 4
    else:
        r = r + recf(n-1)
    return(r)


print(recf(1000))