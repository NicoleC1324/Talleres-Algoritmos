Algoritmo Inicio_alcanzar_velocidades
	Escribir "Velocidad 1 en km/h: "
	Leer v1
	Escribir "Velocidad 2 en km/h: "
	Leer v2
	Escribir "Distancia entre los veh�culos en km: "
	Leer d
	t<-abs(d/(v1-v2))
	tmin<-t*60
	Escribir "Tiempo en el que alcanzar� al veh�culo: " tmin  " minutos"
	
FinAlgoritmo
