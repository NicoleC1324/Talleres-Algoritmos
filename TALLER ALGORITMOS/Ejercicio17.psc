Algoritmo Inicio_alcanzar_velocidades
	Escribir "Velocidad 1 en km/h: "
	Leer v1
	Escribir "Velocidad 2 en km/h: "
	Leer v2
	Escribir "Distancia entre los vehículos en km: "
	Leer d
	t<-abs(d/(v1-v2))
	tmin<-t*60
	Escribir "Tiempo en el que alcanzará al vehículo: " tmin  " minutos"
	
FinAlgoritmo
