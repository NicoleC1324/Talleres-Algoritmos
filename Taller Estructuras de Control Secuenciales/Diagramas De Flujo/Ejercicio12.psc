Algoritmo Ejercicio12
	Escribir "Calificaciones matemáticas: "
	Escribir "Calificación examen final: "
	Leer me
	Escribir "Calificación tarea 1: "
	Leer m1
	Escribir "Calificación tarea 2: "
	Leer m2
	Escribir "Calificación tarea 3: "
	Leer m3
	Escribir "Calificaciones física: "
	Escribir "Calificación examen final: "
	Leer fe
	Escribir "Calificación tarea 1: "
	Leer f1
	Escribir "Calificación tarea 2: "
	Leer f2
	Escribir "Calificaciones química: "
	Escribir "Calificación examen final: "
	Leer qe
	Escribir "Calificación tarea 1: "
	Leer q1
	Escribir "Calificación tarea 2: "
	Leer q2
	Escribir "Calificación tarea 3: "
	Leer q3
	mat<-(me*0.90)+(((m1+m2+m3)/3)*0.10)
	fis<-(fe*0.80)+(((f1+f2)/2)*0.20)
	qui<-(qe*0.85)+(((q1+q2+q3)/3)*0.15)
	pg<-(mat+fis+qui)/3
	Escribir "Promedio general: " pg
	Escribir "Promedio general matemáticas: " mat
	Escribir "Promedio general física: " fis
	Escribir "Promedio general química: " qui
FinAlgoritmo
