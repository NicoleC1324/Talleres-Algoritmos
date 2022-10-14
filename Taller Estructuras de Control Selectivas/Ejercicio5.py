S=float(input("Salario vendedores: "))
D1=float(input("Ventas departamento 1: "))
D2=float(input("Ventas departamento 2: "))
D3=float(input("Ventas departamento 3: "))
VT=(D1+D2+D3)*0.33
if D1>VT:
    SD1=S+(S*0.20)
else:
    SD1=S
if D2>VT:
    SD1=S+(S*0.20)
else:
    SD2=S
if D3>VT:
    SD3=S+(S*0.20)
else:
    SD3=S
print("Sueldo vendedores departamento 1: ",SD1)
print("Sueldo vendedores departamento 2: ",SD2)
print("Sueldo vendedores departamento 3: ",SD3)