Algoritmo Inicio_calificaci�n
	Escribir "D�gite sus tres calificaciones parciales: "
	Leer p1
	Leer p2
	Leer p3
	Escribir "D�gite su calificaci�n examen final: "
	Leer e
	Escribir "D�gite su calificaci�n de trabajo final: "
	Leer t
	p<-((p1+p2+p3)/3)*0.55
	ef<-e*0.3
	tf<-t*0.15
	cf<-p+ef+tf
	Escribir "Esta es su calificaci�n final: " cf
	//55% del promedio de sus tres calificaciones parciales.
	//30% de la calificaci�n del examen final.
	//15% de la calificaci�n de un trabajo final.
FinAlgoritmo
