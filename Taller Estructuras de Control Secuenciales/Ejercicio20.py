pc=float(input("Precio al contado: ")) 
t=float(input("Precio cuota: "))
vt=12*t
rec=vt-pc
p=((rec/pc)*100)/12
print("El porcentaje de recargo es: ",p,"%")