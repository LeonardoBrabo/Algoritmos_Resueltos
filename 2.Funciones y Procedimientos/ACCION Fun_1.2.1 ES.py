ACCION Fun_1.2.1 ES
	
	AMBIENTE

	Numero: Entero;

	FUNCION Cuadrado(N:Entero) : Entero
		
		Cuadrado:= N**2;
	F_FUNCION;

	PROCESO

	ESC("Este programa usa una funcion para devolver el cuadrado de un numero ingresado:")
	ESC("Ingrese un numero:"); LEER(Numero);
	ESC("El cuadrado de su numero es :", Cuadrado(Numero));

F_ACCION;
	
