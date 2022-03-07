from sys import stdin

list_Entrada = [1,1,1,1,1,1,5,5,6,4,7,4,2,3,2,21,3,54,7,8,5,3,2,1,1,1]
lista_Nueva = []

for i in list_Entrada:
    nuevo = i
    if i not in lista_Nueva:
        lista_Nueva.append(i)
        lista_Nueva.sort()

print(lista_Nueva)

