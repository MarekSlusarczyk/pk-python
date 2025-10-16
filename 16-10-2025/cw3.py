krotka = ('Fryderyk', 'Maksymilian', 'Robert', 'Aleksander', 'Jacek')
lista = ['Fryderyk', 'Maksymilian', 'Robert', 'Aleksander', 'Jacek']

print(krotka)
print(lista)

# krotka[0] = "Klemens" - nie da się przypisać
lista[0] = "Klemens"

print('')
print('Krotka:')
for i in krotka:
    print(i)

print('')
print('Lista:')
for i in lista:
    print(i)