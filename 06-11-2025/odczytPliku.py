import csv
# odczyt (mode="r") z pliku za pomocą kontekst menedżera with z kodowaniem polskich znaków
with open("pracownicy.csv", mode="r", newline="", encoding="utf-8") as plik:
    # odczyt danych jako dictionary
    odczyt = csv.DictReader(plik)
    for wiersz in odczyt:
        print(f"----{wiersz["imie"]}----\nWiek: {wiersz["wiek"]}\nDział: {wiersz["dział"]}\nCzas pracy: {wiersz["czas_pracy"]}")


import json
with open("pracownicy.json", mode="r", newline="", encoding="utf-8") as plik:
    data = json.load(plik)
    for i in data:
        print(i[0], i[1], i[2], i[3])