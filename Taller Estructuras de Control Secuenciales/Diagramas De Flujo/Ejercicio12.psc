Algoritmo Ejercicio12
	Escribir "Calificaciones matem�ticas: "
	Escribir "Calificaci�n examen final: "
	Leer me
	Escribir "Calificaci�n tarea 1: "
	Leer m1
	Escribir "Calificaci�n tarea 2: "
	Leer m2
	Escribir "Calificaci�n tarea 3: "
	Leer m3
	Escribir "Calificaciones f�sica: "
	Escribir "Calificaci�n examen final: "
	Leer fe
	Escribir "Calificaci�n tarea 1: "
	Leer f1
	Escribir "Calificaci�n tarea 2: "
	Leer f2
	Escribir "Calificaciones qu�mica: "
	Escribir "Calificaci�n examen final: "
	Leer qe
	Escribir "Calificaci�n tarea 1: "
	Leer q1
	Escribir "Calificaci�n tarea 2: "
	Leer q2
	Escribir "Calificaci�n tarea 3: "
	Leer q3
	mat<-(me*0.90)+(((m1+m2+m3)/3)*0.10)
	fis<-(fe*0.80)+(((f1+f2)/2)*0.20)
	qui<-(qe*0.85)+(((q1+q2+q3)/3)*0.15)
	pg<-(mat+fis+qui)/3
	Escribir "Promedio general: " pg
	Escribir "Promedio general matem�ticas: " mat
	Escribir "Promedio general f�sica: " fis
	Escribir "Promedio general qu�mica: " qui
FinAlgoritmo
