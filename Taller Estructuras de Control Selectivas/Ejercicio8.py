P=int(input("Valor P: "))
Q=int(input("Valor Q: "))
v=(P,Q)
x=(P**3)+(Q**4)-(2*(P**2))
if x>600:
    print(v,"P y Q satisfacen la expresión: ")
else:
    print(v,"P y Q no satisfacen la expresión: ")