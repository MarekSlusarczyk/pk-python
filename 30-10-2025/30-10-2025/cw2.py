# Import funkcji sin z biblioteki math
from math import sin

print(sin(-0.5))

# import funkcji z innego katalogu
from innyKatalog.funkcje import sumaLiczb, iloczynLiczb, indeksowanie
print(sumaLiczb(1,2,3))
print(iloczynLiczb(1, 2, 3, 6))

lista = [2, 4, 5, 6]
print(indeksowanie(lista))
