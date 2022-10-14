x=float(input("Monto total compra: "))
if x>5000000:
    e=x*0.55
    b=x*0.30
    c=x*0.15
    i=c*0.20
    print("Fondos de la empresa: ",e)
    print("Total crédito: ",b)
    print("Total intereses crédito: ",c)
    print("Cantidad prestada por el banco: ",i)
else:
    e=x*0.70
    c=x*0.30
    i=c*0.20
    print("Fondos de la empresa: ",e)
    print("Total crédito: ",c)
    print("Total intereses crédito: ",i)