Algoritmo Ejercicio20
	Escribir "Precio al contado: "
	Leer pc
	Escribir "Precio cuota: "
	Leer t
	vt<-12*t
	rec<-vt-pc
	p<-((rec/pc)*100)/12
	Escribir "El porcentaje de recargo es: " p "%"
FinAlgoritmo
