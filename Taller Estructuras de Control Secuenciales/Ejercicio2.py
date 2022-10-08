inv=float(input("Ingrese la inversión inicial: "))
invx=int(input("Ingrese el número de meses que desea invertir: "))
ganancia=(inv*0.02)+inv
gan=(inv*0.02)
ganx=(inv*(0.02*invx))
gananual=(inv*(0.02*invx))+inv
print("Ganancias netas tras un mes: ",gan)
print("Ganancias totales tras un mes: ",ganancia)
print("Ganancias netas tras x meses: ",ganx)
print("Ganancias totales tras x meses: ",gananual)