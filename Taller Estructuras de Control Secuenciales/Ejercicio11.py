input("Nombre del trabajador: ")
phnt=float(input("Pago por hora normal trabajada: "))
hnt=int(input("Horas normales trabajadas: "))
het=int(input("Horas extras trabajadas: "))
phet=phnt+(phnt*0.25)
ph=phnt*hnt
sb=ph+phet
pf=sb*0.05
phh=sb*0.02
ca=sb*0.07
deduc=pf+phh+ca
asig=250000+173000+180000
st=sb+asig-deduc
sbded=sb-deduc
print("Sueldo base: ",sb)
print("Asignaciones: ",asig)
print("Deducciones: ",deduc)
print("Sueldo base menos deducciones: ",sbded)
print("Sueldo neto diciembre: ",st)
