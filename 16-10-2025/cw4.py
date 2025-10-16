krotka = ('Fryderyk', 'Maksymilian', 'Robert', 'Aleksander', 'Jacek')
lista = ['Fryderyk', 'Maksymilian', 'Robert', 'Aleksander', 'Jacek']

print(krotka)
print(lista)

# krotka[0] = "Klemens" - nie da się przypisać
lista[0] = "Klemens"

# dodawanie elementów
# krotka[6] = 'Krzysztof' - do krotki nie da się dodać
lista.append('Krzysztof')

print(krotka)
print(lista)