#sacar día, mes, año de hoy
from datetime import datetime
from mmap import ALLOCATIONGRANULARITY
hoy = datetime.now()
## de hoy
dia_actual=hoy.day
mes_actual=hoy.month
año_actual=hoy.year
#entradas
fecha_nacimiento=input("poner en formato dd/mm/yy: ")
(dia,mes,año)=fecha_nacimiento.split("/")
dia_nacimiento=int(dia)
mes_nacimiento=int(mes)
año_nacimiento=int(año)
#caja negra
edad=0
if(mes_actual>mes_nacimiento):
    edad=año_actual-año_nacimiento
elif(mes_actual<mes_nacimiento):
    edad=(año_actual-año_nacimiento)-1
elif(mes_actual==mes_nacimiento):
    if(dia_actual<dia_nacimiento):
        edad=(año_actual-año_nacimiento)-1
    elif(dia_actual>dia_nacimiento):
        edad=(año_actual-año_nacimiento)
    elif(dia_actual==dia_nacimiento):
        edad=(año_actual-año_nacimiento)
print("La edad es: ",edad)
#Signos
Signo=""
if(dia_nacimiento>=21 and mes_nacimiento<=11)or(dia_nacimiento>=21 and mes_nacimiento<=12):
    Signo = "Sagitario"
print("El signo es: ",Signo)
