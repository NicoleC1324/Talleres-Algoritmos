T=int(input("Temperatura en °F: "))
if T>85:
    D="Natación"
if 70<T<=85:
    D="Tennis"
if 32<T<=70:
    D="Golf"
if 10<T<=32:
    D="Esquí"
if T<=10:
    D="Marcha"
print("El deporte apropiado es: ",D)
