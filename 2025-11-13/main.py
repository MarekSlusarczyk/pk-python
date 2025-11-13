import csv
import json
import pickle

# struktura do zapisu w pliku csv
data_csv = [
    ["imie", "nazwisko", "wiek", "jezyki"],
    ["Ala", "Makota", 20, ["C++", "C#", "Python", "Java"]]
]

# zapis (mode="w") do pliku za pomocą kontekst menedżera with z kodowaniem polskich znaków
with open("osoba.csv", mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data_csv)

data = {
    "imie": "Ala",
    "nazwisko": "Makota",
    "wiek": 20,
    "jezyki": ["C++", "C#", "Python", "Java"]
}

with open("osoba.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

with open("osoba.pkl", "wb") as f:
    pickle.dump(data, f)


# ODCZYT DANYCH

# odczyt danych (mode="r") z pliku csv przy użyciu kontekst menedżera with z kodowaniem polskich znaków
with open("osoba.csv", mode="r", newline="", encoding="utf-8") as f:
    # dane odczytywane jako dictionary
    odczyt = csv.DictReader(f)
    for wiersz in odczyt:
        print(f"{wiersz["imie"]} {wiersz["nazwisko"]} {wiersz["wiek"]}")
        jezyki = eval(wiersz["jezyki"]) # eval - funkcja oceniająca czy dany ciąg znaków może być przekonwertowany na obiekt pythona. W tym przypadku konwertująca string na obiekt list
        for i in jezyki:
            print(i)


#odczyt danych z pliku json
with open('osoba.json', 'r') as f:
    odczyt_json = json.load(f)

print(json.dumps(odczyt_json, indent=4))

#odczyt danych pickle

with open('osoba.pkl', 'rb') as f:
    dane_pkl = pickle.load(f)
    print(dane_pkl)