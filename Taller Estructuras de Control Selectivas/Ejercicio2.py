S=float(input("Sueldo del trabajador: "))
if S<900000:
    a=S+(S*0.15)
else:
    a=S+(S*0.12)
print("Sueldo del trabajador con aumento: ",a)