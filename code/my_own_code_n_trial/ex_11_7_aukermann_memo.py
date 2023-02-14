known={(0,0):1, (0,1):2, (1,0):2}

def ack(m, n):
    """
    This is the answer solution !
    Don't worry about multiple if, because we use return
    """
    if (m,n) in known:
        return known[(m,n)]
    
    if m == 0:
        res = n + 1
        known[(m,n)] = res
        return res
    
    if m > 0 and n == 0:
        res = ack(m-1, 1)
        known[(m,n)] = res
        return res
    
    res = ack(m-1, ack(m, n-1))
    known[(m,n)] = res
    return res

print(ack(3,4))
print(ack(3,6))