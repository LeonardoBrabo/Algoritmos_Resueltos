ACCION Fun_1.2.4 ES
	
	AMBIENTE

	op: Caracter;
	N: Entero;

	FUNCION Cripto(Numero: Entero) : Real

		AMBIENTE

		A: Entero;

		PROCEDIMIENTO Result() ES

			AMBIENTE

			Asumar,Sumar,Descom,B : Entero;

			PROCESO

			Asumar:=0; Sumar:=0; Descom:=0;
			Asumar:= Numero DIV A;
			Descom:= NUmero MOD A;
			Suma:= Suma + Asumar;
			MIENTRAS  Descom > 9 HACER   //Hasta que llegue al ultimo digito del numero
				B:= A DIV 10; A:= B;
				Asumar:= Descom DIV B;
				Descom:= DEscom MOD B;
				Suma:= Suma + Asumar;
			FM;
			Cripto:=(Suma + Descom) MOD 7;
		F_PROC;

		PROCESO
		A:=0;
		SI Numero < 0 ENTONCES
			Cripto:= -1;
		SINO
			SEGUN Numero HACER

				>= 100000 : A:= 100000; Result();
				>= 10000  : A:= 10000; Result();
				>= 1000   : A:= 1000; Result();
				>= 100    : A:= 100; Result();
				>= 10     : A:= 10; Result();
				<  9	  : Critpo:= Numero mod 7;
			OTROS
				ESC("Fuera de Rango");
			F_SEGUN;
	F_FUNCION;


	PROCESO

	REPETIR
		ESC("Este programa devuelve una clave segun el numero que ingrese, y si es negativo devuelve -1");
		ESC("Ingrese su numero para generar una clave:"); LEER(N);
		ESC("La clave para el numero es:",Cripto(N));
		ESC("Quiere Continuar? s/n"); LEER(op);
	HASTA QUE op = "n"

F_ACCION.



