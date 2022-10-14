e=int(input("Edad en meses: "))
s=input("H (hombre) o M (mujer): ")
h=float(input("Nivel de hemoglobina: "))
H="H"
M="M"
if (0<=e<=1 and 13<=h<=26):
    rango="Negativo"
elif (1<e<=6 and 10<=h<=18):
    rango="Negativo"
elif (6<e<=12 and 11<=h<=15):
    rango="Negativo"
elif (12<e<=60 and 11.5<=h<=15):
    rango="Negativo"
elif (60<e<=120 and 12.6<=h<=15.5):
    rango="Negativo"
elif (120<e<=180 and 13<=h<=15.5):
    rango="Negativo"
elif (e>180 and 12<=h<=16 and s==M):
    rango="Negativo"
elif (e>180 and 14<=h<=18 and s==H):
    rango="Negativo"
else:
    rango="Positivo"
print(rango)