def suma(a,b):
    """
    la función suma recibe los parámetros a y b 
    devuelve la suma de mabos 
    
    >>> suma (5,10)
    15

    >>> suma(0,0)
    1

    >>> suma(-5, 7)
    2
    """
    return a+b
def palindromo(palabra):

    """
    La función palíndromo devuelve vertadero o True si la palabra recibida es un palíndromo
    donde un palíndromo es una palabra que se lee igual a l inversa como de forma normal
    >>> palindromo("somos")
    True

    >>> palindromo("radar")
    True

    >>> palindromo("holah")
    True
    
    >>> palindromo("Ana")
    True

    >>> palindromo("Atar a la rata")
    True

    """
    if palabra.lower().replace(" ","")==palabra[::-1].lower().replace(" ",""):#para evitar errores con mayúsculas y espacios si son frases palíndromas
        return True
    else:
        return False
    #para confirmar que la importación se hace desde este mismo fichero
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #donde se pone los test de las funciones  despues de los signos mayor S
#si queremos ver los detalles de l prueba pondremos python mi_script.py -v porque si le pones menos -v no nos muestra nada si esta correcto

