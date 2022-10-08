ph=float(input("Pago por hora: "))
h=int(input("Número de horas trabajadas: "))
sb=ph*h
sbt=sb-(sb*0.20)
print("Salario base: ",sb)
print("Salario base con descuento: ",sbt)
