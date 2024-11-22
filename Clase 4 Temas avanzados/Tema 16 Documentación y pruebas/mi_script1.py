def doblar(lista):

    """
    >>> l = [1,2,3,4,5]
    >>> doblar(l)
    [2, 4, 6, 8, 10]

    >>> l=[]
    >>> for i in range(10):
    ...     l.append(i)
    >>> doblar(l)
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    
    
    """
    return [n*2 for n in lista]

def sumar(a,b):

    """
    >>> sumar(10,"b")
    Traceback (most recent call last):
     ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    return a+b

   

    

if __name__ == "__main__":
    import doctest
    doctest.testmod() 