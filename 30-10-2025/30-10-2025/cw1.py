def pizza(dodatek1 = "sos", dodatek2 = "ser", dodatek3 = "szynka", dodatek4 = "pieczarki"):
    print(f"Zamówiono pizzę:\nDodatek 1: {dodatek1}\nDodatek 2: {dodatek2}\nDodatek 3: {dodatek3}\nDodatek 4: {dodatek4}")


# dodatek1 = input("Podaj nazwę dodatku pierwszego (domyślnie sos): ")
# dodatek2 = input("Podaj nazwę dodatku drugiego (domyślnie ser): ")
# dodatek3 = input("Podaj nazwę dodatku trzeciego (domyślnie szynka): ")
# dodatek4 = input("Podaj nazwę dodatku czwartego (domyślnie pieczarki): ")

pizza(dodatek2="rukola", dodatek3="pomidor")


def liczby(*args):
    krotka = tuple()
    for index, value in enumerate(args):
        # print(f"{index}: {value}")
        # krotka[index] = index * value
        krotka = krotka + (index * value, )

    return krotka

print("Liczby pomnożone przez indeksy zwrócone jako krotka: ")
print(liczby(4, 5, 8, 9))


def logowaniePracownika(**infoOPracowniku):
    print(f"Nazywasz się: {infoOPracowniku['imie']} {infoOPracowniku['nazwisko']}, masz {infoOPracowniku['wiek']} lat, twój wzrost to {infoOPracowniku['wzrost']} cm")

print("Logowanie pracownika:")
logowaniePracownika(imie="Jan", nazwisko="Kowalski", wiek=30, wzrost=179)
