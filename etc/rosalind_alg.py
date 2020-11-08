"""http://rosalind.info/problems/list-view/?location=algorithmic-heights"""

def fibo(n):
    """Fibonacci Numbers"""
    if n == 0: return 0
    elif n == 1: return 1
    def recurrence(n, Fn_2 = 0, Fn_1 = 1, Fn = 0):
        """Recurrence relation of for the Fibonacci sequence"""
        if n == 0: return Fn_1
        Fn = Fn_2 + Fn_1
        return recurrence(n-1, Fn_1, Fn)
    return recurrence(n-1)

def read_lbsv(lbsv):
    """Reading line-break-seperated values file"""
    values = []
    with open(lbsv, 'r') as f: values = f.read().strip().split('\n')
    return values

def write_lbsv(values):
    """Writing line-break-seperated values file"""
    lbsv = "o.lbsv"
    with open(lbsv, 'w') as f:
        for value in values: f.write(str(value) + '\n')
    return None

def bind(lbsv):
    """Binary Search"""
    values = read_lbsv(lbsv)
    n, _m, A, B = int(values[0]), int(values[1]), \
        list(map(int, values[2].split())), list(map(int, values[3].split()))
    idxes = []
    def binary_search(b, A, n, origin = 0):
        if n == origin or n == origin+1:
            if b == A[origin]: return origin+1
            elif b == A[n]: return n+1
            else: return -1        
        idx = (origin + n)//2
        median = A[idx]
        if b < median: idx = binary_search(b, A, idx, origin)
        elif b > median: idx = binary_search(b, A, n, idx)
        else: return idx+1
        return idx
    for b in B: idxes.append(binary_search(b, A, n))
    return idxes

def deg(lbsv):
    """Degree Array"""
    edge_lists = read_lbsv(lbsv)