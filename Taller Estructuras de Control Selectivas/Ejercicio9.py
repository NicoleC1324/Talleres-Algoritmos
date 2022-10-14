N=int(input("Nombre cliente: "))
C=float(input("Total compra: "))
if N<50000:
    P=C
    D=0
    DR=0
if N>=50000 and N<100000:
    P=C-(C*0.05)
    D=C*0.5
    DR=5
if N>=100000 and N<700000:
    P=C-(C*0.11)
    D=C*0.11
    DR=11
if N>=700000 and N<1500000:
    P=C-(C*0.18)
    D=C*0.18
    DR=18
if N>1500000:
    P=C-(C*0.25)
    D=C*0.25
    DR=25
print("Cliente: ",N)
print("Total a pagar: ",P)
print("Valor descontado: ",D)
print("Descuento: ",DR)

