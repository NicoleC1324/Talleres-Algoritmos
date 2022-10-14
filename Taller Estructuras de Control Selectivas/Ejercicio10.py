S=float(input("Sueldo bruto trabajador: "))
if S>=5000000:
    C=1
if S>=4300000 and S<5000000:
    C=2
if S>=3600000 and S<4300000:
    C=3
if S>=2000000 and S<3600000:
    C=4
if S>=900000 and S<2000000:
    C=5
if C==1:
    SA=S+(S*0.10)
if C==2:
    SA=S+(S*0.15)
if C==3:
    SA=S+(S*0.20)
if C==4:
    SA=S+(S*0.40)
if C==5:
    SA=S+(S*0.60)
print("Nuevo sueldo trabajador: ",SA)
print("Categoría: ",C)