def sumaLiczb(*liczby):
    return sum(liczby)

def iloczynLiczb(*liczby):
    wynik = 1
    for i in liczby:
        wynik *= i

    return wynik

def indeksowanie(liczby):
    wynik = []
    for i in enumerate(liczby):
        wynik.append(i)

    return wynik