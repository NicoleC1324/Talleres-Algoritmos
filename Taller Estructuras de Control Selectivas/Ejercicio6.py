A=int(input("A: "))
B=int(input("B: "))
C=int(input("C: "))
D=int(input("D: "))
mil=(A*1000)+(B*100)
cen=(C*10)+D
if cen>=51:
    N=mil+100
else:
    N=mil
print("Resultado redondeado: ",N)