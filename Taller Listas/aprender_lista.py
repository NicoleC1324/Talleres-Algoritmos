lista=[1,2,3,4,5,1]
lista2=["🐱","🐱","🐱","🐱","🐱","🤔"]
lista3=[1,3,6,7,8,9,0,11]
#agregar al final
lista.append(50)
print(lista)
#eliminar al final o en una posición dada
lista.pop()
print(lista)
lista.pop(0)
print(lista)
#agregar un elemento en una posición
lista.insert(0,"🤔")
lista.insert(4,"🤔")
print(lista)
#contar cuántos elementos hay
a=lista.count("🤔")
print(a)
#sacar la posición de un elemento
p=lista.index("🤔")
print(p)
#copiar la lista
copia=lista.copy()
print(copia)
print(lista)
#unir dos listas
lista.extend(lista2)
print(lista)
#ordenar una lista de manera asc
lista3.sort()
print(lista3)
#ordenar una lista de manera descendente
lista3.sort(reverse=True)
print(lista3)
#limpia la lista
lista3.clear()
print(lista3)
lista2.remove("🐱")
print(lista2)
lista2.reverse()
print(lista2)