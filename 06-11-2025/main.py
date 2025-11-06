# def iloczynLiczb(*liczby):
#     """
#     Funkcja służąca do uzyskania iloczynu liczb
#     *liczby - argumenty pozycyjne typu integer - argumenty liczbowe przekazane w formie krotki
#
#     wynik - zwracana zmienna przechowująca wynik mnożenia liczb
#     """
#     wynik = 1
#     for i in liczby:
#         wynik *= i
#
#     return wynik
#
# # wyświetlanie docstringa
# print(iloczynLiczb.__doc__)
#
# # wyświetlanie docstringa z nagłówkiem za pomocą funkcji help()
# help(iloczynLiczb)






#import modułu csv, pozwalającego na zapis plików w formacie csv
import csv

# dane pracowników
dane = [
    ["imie", "wiek", "dział", "czas_pracy"],
    ["Anna", 29, "FR", 3.5],
    ["Piotr", 42, "FK", 12],
    ["Katarzyna", 35, "FZ", 8],
    ["Michał", 26, "FR", 1.2],
    ["Ewa", 31, "FK", 6],
    ["Tomasz", 45, "FZ", 15],
    ["Magdalena", 38, "FR", 10],
    ["Robert", 50, "FK", 20]
]

# zapis (mode="w") do pliku za pomocą kontekst menedżera with z kodowaniem polskich znaków
with open("pracownicy.csv", mode="w", newline="", encoding="utf-8") as plik:
    writer = csv.writer(plik)
    writer.writerows(dane)

