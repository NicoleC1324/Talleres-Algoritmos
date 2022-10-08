p1=float(input("Calificación parcial 1: "))
p2=float(input("Calificación parcial 2: "))
p3=float(input("Calificación parcial 3: "))
e=float(input("Califiación examen final: "))
t=float(input("Calificación de trabajo final:"))
p=((p1+p2+p3)/3)*0.55
ef=e*0.30
tf=t*0.15
cf=p+ef+tf
print("Esta es su calificación final: ",cf)