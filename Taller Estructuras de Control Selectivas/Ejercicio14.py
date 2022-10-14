la=float(input("Lectura anterior Kwh: "))
lac=float(input("Lectura actual Kwh: "))
dif=lac-la
if 0>dif<=100:
    t=dif*4600
if 101>=dif<=300:
    t=dif*80000
if 301>=dif<=500:
    t=dif*100000
if dif>500:
    t=dif*120000
print("Monto a pagar: ",t)