B=int(float("Dinero invertido: "))
P=int(float("Porcentaje de interés dado por el banco: "))
Int=(B*(P/100))/12
T=B+Int
if T>100000:
    print("Total en la cuenta: ",T)
else:
    print("Total en la cuenta: ",B)