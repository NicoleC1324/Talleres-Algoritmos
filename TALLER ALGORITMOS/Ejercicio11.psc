Algoritmo Inicio_calificación
	Escribir "Dígite sus tres calificaciones parciales: "
	Leer p1
	Leer p2
	Leer p3
	Escribir "Dígite su calificación examen final: "
	Leer e
	Escribir "Dígite su calificación de trabajo final: "
	Leer t
	p<-((p1+p2+p3)/3)*0.55
	ef<-e*0.3
	tf<-t*0.15
	cf<-p+ef+tf
	Escribir "Esta es su calificación final: " cf
	//55% del promedio de sus tres calificaciones parciales.
	//30% de la calificación del examen final.
	//15% de la calificación de un trabajo final.
FinAlgoritmo
