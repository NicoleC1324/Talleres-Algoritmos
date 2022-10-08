Algoritmo Ejercicio11
	Escribir "Nombre del trabajador: "
	Leer n
	Escribir "Pago por hora normal trabajada: "
	Leer phnt
	Escribir "Horas normales trabajadas: "
	Leer hnt
	Escribir "Horas extras trabajadas: "
	Leer het
	phet<-phnt+(phnt*0.25)
	ph<-phnt*hnt
	sb<-ph+phet
	pf<-sb*0.05
	phh<-sb*0.02
	ca<-sb*0.07
	deduc<-pf+phh+ca
	asig<-250000+173000+180000
	st<-sb+asig-deduc
	sbded<-sb-deduc
	Escribir "Sueldo base: " sb
	Escribir "Asignaciones: " asig
	Escribir "Deducciones: " deduc
	Escribir "Sueldo base menos deducciones: " sbded
	Escribir "Sueldo neto diciembre: " st
FinAlgoritmo
