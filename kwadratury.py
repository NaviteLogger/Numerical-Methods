# prostokąty
# kwadraty
# trójkąty
# simpson (parabole)
def prostokaty(f, a, b, n):
    """
    Oblicza całkę oznaczoną z funkcji f na przedziale [a, b] metodą prostokątów.
    
    :param f: Funkcja, której całkę chcemy obliczyć.
    :param a: Dolna granica całkowania.
    :param b: Górna granica całkowania.
    :param n: Liczba podziałów przedziału [a, b].
    :return: Przybliżona wartość całki oznaczonej.
    """
    h = (b - a) / n
    suma = 0
    for i in range(n):
        x = a + i * h
        suma += f(x) * h
    return suma

def kwadraty(f, a, b, n):
    """
    Oblicza całkę oznaczoną z funkcji f na przedziale [a, b] metodą kwadratów.
    
    :param f: Funkcja, której całkę chcemy obliczyć.
    :param a: Dolna granica całkowania.
    :param b: Górna granica całkowania.
    :param n: Liczba podziałów przedziału [a, b].
    :return: Przybliżona wartość całki oznaczonej.
    """
    h = (b - a) / n
    suma = 0
    for i in range(n):
        x1 = a + i * h
        x2 = a + (i + 1) * h
        suma += (f(x1) + f(x2)) * h / 2
    return suma

def trojkaty(f, a, b, n):
    """
    Oblicza całkę oznaczoną z funkcji f na przedziale [a, b] metodą trójkątów.
    
    :param f: Funkcja, której całkę chcemy obliczyć.
    :param a: Dolna granica całkowania.
    :param b: Górna granica całkowania.
    :param n: Liczba podziałów przedziału [a, b].
    :return: Przybliżona wartość całki oznaczonej.
    """
    h = (b - a) / n
    suma = 0
    for i in range(n):
        x1 = a + i * h
        x2 = a + (i + 1) * h
        suma += (f(x1) + f(x2)) * h / 2
    return suma

def simpson(f, a, b, n):
    """
    Oblicza całkę oznaczoną z funkcji f na przedziale [a, b] metodą Simpsona.
    
    :param f: Funkcja, której całkę chcemy obliczyć.
    :param a: Dolna granica całkowania.
    :param b: Górna granica całkowania.
    :param n: Liczba podziałów przedziału [a, b]. Musi być parzysta.
    :return: Przybliżona wartość całki oznaczonej.
    """
    if n % 2 == 1:
        raise ValueError("Liczba podziałów n musi być parzysta.")
    
    h = (b - a) / n
    suma = f(a) + f(b)
    
    for i in range(1, n, 2):
        suma += 4 * f(a + i * h)
    
    for i in range(2, n-1, 2):
        suma += 2 * f(a + i * h)
    
    return suma * h / 3