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

def bind():
    """Binary Search"""
    pass