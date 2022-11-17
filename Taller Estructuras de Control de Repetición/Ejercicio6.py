c=int(0)
a=int(input("Digite dividendo: "))
d=int(input("Digite divisor: "))
a=a-d
while(a>=0):
    c=c+1
    a=a-d
print("El resultado de la division es:"+str(c))