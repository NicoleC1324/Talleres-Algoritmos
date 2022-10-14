kmr=int(input("KM recorridos: "))
kma=int(input("KM adicionales: "))
if kmr<300:
    t=50000
if kmr>=300 and kmr<1000:
    t=70000+(kma*30000)
if kmr>=1000:
    t=150000+(kma*9000)
print("Total a pagar: ",t,"%")