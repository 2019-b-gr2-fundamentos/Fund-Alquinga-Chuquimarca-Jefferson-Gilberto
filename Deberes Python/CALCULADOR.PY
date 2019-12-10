#Importamos las librerias "math" y "cmath"
import math
import cmath

#Creamos el menu y los submenus que nos perimita escoger las operaciones a realizar
print("Desea realizar alguna operacion\n1.SI\n2.NO")
op=["SI","NO",]
elegir=input()
print("")
while elegir not in op or elegir==" ":
	print("Opcion incorrecta intente nuevamente")
	print("Desea realizar alguna operacion\n1.SI\n2.NO")
	elegir=input()
	print("")

#Menu de todas los funciones que se puedan realizar
	ii=1
	while ii<=1:
		if elegir=="SI":
			print("Que funcion desea realizar\n1.Funcion Aritmetica\n2.Funcion Trigonometrica")
			print("3.Funcion Logaritmica y exponencial\n4.Tranformaciones\n5.Salir al menu principal")
			op1=["1","2","3","4","5"]
			fun=input("Opcion: ")
			print("")
			while fun not in op1 or fun=="":
				print("Opcion incorrecta intente nuevamente")
				print("Que funcion desea realizar\n1.Funcion Aritmetica\n2.Funcion Trigonometrica")
				print("3.Funcion Logaritmica y exponencial\n4.Tranformaciones\n5.Salir al menu principal")
				fun=input("Opcion: ")
				print("")
			break

#Menu de algunas las operaciones de la funcion aritmetica
		iii=2
		while iii<=2:
			if fun=="1":
				op2=["1","2","3","4","5","6","7"]
				print("¿Que operacion desea realizar?\n1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\n5.Potenciacion\n6.Raices\n7.Salir al menu")
				operacion=input("Opcion: ")
				print(" ")
				while operacion not in op2 or operacion=="":
					print("Opcion incorrecta intente nuevamente.\n")
					print("¿Que operacion desea realizar?\n1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\n5.Potenciacion\n6.Raices\n7.Salir al menu")
					operacion = input("Opcion: ")
					print(" ")
				if operacion=="1":
					def suma():
						print("Operacion Suma")
						sumador1=input("Ingrese el 1° numero: ")
						num1=sumador1.isdigit()
						while num1 == False:
							print("ingrese un valor numerico. \n")
							sumador1 = input()
							num1 = sumador1.isdigit()
						sumador2  =input("Ingrese el 2° numero: ")
						num2 = sumador2.isdigit()
						while num2 == False:
							print("ingrese un valor numerico. \n")
							sumador2 = input()
							num2 = sumador2.isdigit()
						print("El resultado es:  ",int(sumador1)+int(sumador2))
					suma()
					print(" ")
				if operacion=="2":
					def resta():
						print("Operacion Resta")
						minuendo=input("Ingrese el minuendo: ")
						num1=minuendo.isdigit()
						while num1==False:
							print("ingrese un valor numerico. \n")
							minuendo=input()
							num1=minuendo.isdigit()
						sustraendo=input("Ingrese el sustraendo: ")
						num2=sustraendo.isdigit()
						while num2== False:
							print("ingrese un valor numerico. \n")
							sustraendo=input()
							num2=sustraendo.isdigit()
						print("El resultado es:  ",int(minuendo)-int(sustraendo))
					resta()
					print(" ")
				if operacion=="3":
					def multiplicacion():
						print("Operacion multiplicacion")
						factor1=input("Ingrese el 1° factor: ")
						num1=factor1.isdigit()
						while num1==False:
							print("ingrese un valor numerico. \n")
							factor1=input()
							num1=factor1.isdigit()
						factor2=input("Ingrese el 2° factor: ")
						num2 = factor2.isdigit()
						while num2 == False:
							print("ingrese un valor numerico. \n")
							factor2 = input()
							num2 = factor2.isdigit()
						print("El resultado es:  ",int(factor1)*int(factor2))
					multiplicacion()
					print(" ")
				if operacion=="4":
					def division():
						print("Operacion Division")
						dividendo=input("Ingrese el dividendo: ")
						num1=dividendo.isdigit()
						while num1 == False:
							print("ingrese un valor numerico. \n")
							dividendo=input()
							num1= dividendo.isdigit()
						divisor=input("Ingrese el divisor: ")
						num2=divisor.isdigit()
						while num2 == False:
							print("ingrese un valor numerico. \n")
							divisor= input(0)
							num2=divisor.isdigit()
						print("El resultado es:  ",int(dividendo)/int(divisor))
					division()
					print(" ")
				if operacion=="5":
					def potenciacion():
						print("Operacion Potenciacion")
						base=input("Ingrese la base: ")
						num1=base.isdigit()
						while num1== False:
							print("ingrese un valor numerico. \n")
							base=input()
							num1=base.isdigit()
						exponente=input("Ingrese el exponente: ")
						num2=exponente.isdigit()
						while num2==False:
							print("ingrese un valor numerico. \n")
							exponente=input()
							num2=exponente.isdigit()
							print("El resultado es:  ",int(base)**int(exponente))
					potenciacion()
					print(" ")
				if operacion=="6":
					def raices():
						print("Opcion Raiz")
						valor=input("Ingrese el radical: ")
						num1=valor.isdigit()
						while num1==False:
							print("ingrese un valor numerico. \n")
							valor=input("Ingrese el radical: ")
						print("El resultado es: ", math.sqrt(int(valor)))
					raices()
					print("")
				if operacion=="7":
					break

#Menu de algunas de las funciones trigonometricas		
			if fun=="2":
				op3=["1","2","3","4","5","6","7","8","9","10","11"]
				print("Escoja lo que desea buscar.\n1.Seno\n2.Coseno\n3.Tangente\n4.Cotangente\n5.Cosecante\n6.Secante\n7.Hopitenusa\n8.arcseno")
				print("9.arccoseno\n10.arctangente\n11.Salir")
				Trigonome=input("Opcion: ")
				print("")
				while Trigonome not in op3 or Trigonome=="":
					print("Opcion incorrecta intente nuevamente.\n")
					print("Escoja lo que desea buscar.\n1.Seno\n2.Coseno\n3.Tangente\n4.Cotangente\n5.Cosecante\n6.Secante\n7.Hipotenusa\n8.arcseno")
					print("9.arccoseno\n10.arctangente\n11.Salir")
					Trigonome=input("Opcion: ")
					print("")
				if Trigonome=="1":
					print("Funcion Seno")
					angulo=0
					def seno(angulo):
						angulo=input("Ingrese el angulo: ")
						num1=angulo.isdigit()
						ang=math.radians(int(angulo))
						while num1==False:
							print("ingrese un valor numerico. \n")
							angulo=input("Ingrese el angulo: ")
							num1=angulo.isdigit()
							ang=math.radians(angulo)
						print("El seno del angulo de ",angulo," es: ",math.sin(ang))
					seno(angulo)
					print("")
				if Trigonome=="2":
					print("Funcion Coseno")
					angulo1=0
					def coseno(angulo1):
						angulo1=input("Ingrese el angulo: ")
						num1=angulo1.isdigit()
						ang=math.radians(int(angulo1))
						while num1==False:
							print("ingrese un valor numerico. \n")
							angulo1=input("Ingrese el angulo: ")
							num1=angulo1.isdigit()
							ang=math.radians(angulo1)
						print("El coseno del angulo de ",angulo1," es: ",math.cos(ang))
					coseno(angulo1)
					print("")
				if Trigonome=="3":
					print("Funcion Coseno")
					angulo1=0
					def tangente(angulo1):
						angulo1=input("Ingrese el angulo: ")
						num1=angulo1.isdigit()
						ang=math.radians(int(angulo1))
						while num1==False:
							print("ingrese un valor numerico. \n")
							angulo1=input("Ingrese el angulo: ")
							num1=angulo1.isdigit()
							ang=math.radians(angulo1)
						print("La tangente del angulo de ",angulo1," es: ",math.tan(ang))
					tangente(angulo1)
					print("")
				if Trigonome=="4":
					print("Funcion Cotangente")
					angulo1=0
					def cotangente(angulo1):
						angulo1=input("Ingrese el angulo: ")
						num1=angulo1.isdigit()
						ang=math.radians(int(angulo1))
						while num1==False:
							print("ingrese un valor numerico. \n")
							angulo1=input("Ingrese el angulo: ")
							num1=angulo1.isdigit()
							ang=math.radians(angulo1)
						print("La cotangente del angulo de ",angulo1," es: ",1/(math.tan(ang)))
					cotangente(angulo1)
					print("")
				if Trigonome=="5":
					print("Funcion Cosecante")
					angulo1=0
					def cosecante(angulo1):
						angulo1=input("Ingrese el angulo: ")
						num1=angulo1.isdigit()
						ang=math.radians(int(angulo1))
						while num1==False:
							print("ingrese un valor numerico. \n")
							angulo1=input("Ingrese el angulo: ")
							num1=angulo1.isdigit()
							ang=math.radians(angulo1)
						print("La secante del angulo de ",angulo1," es: ",1/(math.sin(ang)))
					cosecante(angulo1)
					print("")
				if Trigonome=="6":
					print("Funcion Secante")
					angulo1=0
					def secante(angulo1):
						angulo1=input("Ingrese el angulo: ")
						num1=angulo1.isdigit()
						ang=math.radians(int(angulo1))
						while num1==False:
							print("ingrese un valor numerico. \n")
							angulo1=input("Ingrese el angulo: ")
							num1=angulo1.isdigit()
							ang=math.radians(angulo1)
						print("La secante del angulo de ",angulo1," es: ",1/(math.cos(ang)))
					secante(angulo1)
					print("")
				if Trigonome=="7":
					def hipotenusa():
						print("Hipotenusa")
						catetomayor=input("Ingrese el cateto mayor: ")
						num1=catetomayor.isdigit()
						while num1==False:
							print("ingrese un valor numerico. \n")
							catetomayor=input("Ingrese el cateto mayor: ")
							num1=catetomayor.isdigit()
						catetomenor=input("Ingrese el cateto menor: ")
						num2=catetomenor.isdigit()
						while num2==False:
							print("ingrese un valor numerico. \n")
							catetomenor=input("Ingrese el cateto menor: ")
							num2=catetomenor.isdigit()
						print("La hipotenusa es: ",math.hypot(int(catetomayor),int(catetomenor)))
					hipotenusa()
					print("")
				if Trigonome=="8":
					def arcseno():
						print("Funcion arcseno")
						arc=float(input("Ingrese el arcseno: "))
						print("El angulo de ",arc," es: ",math.degrees(math.asin(arc))," grados")
					arcseno()
					print("")
				if Trigonome=="9":
					def arccoseno():
						print("Funcion arcseno")
						arc=float(input("Ingrese el arcseno: "))
						print("El angulo de ",arc," es: ",math.degrees(math.acos(arc))," grados")
					arccoseno()
					print("")
				if Trigonome=="10":
					def arctangente():
						print("Funcion arcseno")
						arc=float(input("Ingrese el arcseno: "))
						print("El angulo de ",arc," es: ",math.degrees(math.atan(arc))," grados")
					arctangente()
					print("")
				if Trigonome=="11":
					break

#Menu de las funciones logaritmicas
			if fun=="3":
				op5=["1","2","3"]
				print("Escoja lo que desea realizar.\n1.Logaritmo\n2.Logaritmo 10\n3.Salir al menu")
				log=input("Opcion: ")
				print("")
				while log not in op5 or log=="":
					print("Opcion incorrecta intente nuevamente.\n")
					print("Escoja lo que desea buscar.\n1.Logaritmo\n2.Logaritmo 10\n3.Salir al menu")
					log=input("Opcion: ")
					print("")
				if log=="1":
					def logaritmo():
						print("Funcion logaritmica")
						dato=input("Ingrese el valor a calcular: ")
						num1=dato.isdigit()
						while num1==False:
							print("Opcion incorrecta intente nuevamente.\n")
							dato=input("Ingrese el valor a calcular: ")
							num1=dato.isdigit()
						print("El logaritmo es: ",math.log(int(dato)))
					logaritmo()
				if log=="2":
					def logaritmo_10():
						print("Funcion logaritmica")
						dato=input("Ingrese el valor a calcular: ")
						num1=dato.isdigit()
						while num1==False:
							print("Opcion incorrecta intente nuevamente.\n")
							dato=input("Ingrese el valor a calcular: ")
							num1=dato.isdigit()
						print("El logaritmo es: ",math.log10(int(dato)))
					logaritmo_10()
				if log=="3":
					break

#Menu de tranformaciones de grados
			if fun=="4":
				op6=["1","2","3","4","5","6","7"]
				print("Escoja la tranformacion.\n1.Celcius a Kelvin\n2.Celcius a Farenheith \n3.Kelvin a Farenheith \n4.Kelvin a Celcius")
				print("5.Farenheith a Celcius\n6.Farenheith a Kelvin\n7.Salir")
				trans=input("Opcion: ")
				print("")
				while trans not in op6 or trans=="":
					print("Opcion incorrecta intente nuevamente.\n")
					print("Escoja la tranformacion.\n1.Celcius a Kelvin\n2.Celcius a Farenheith \n3.Kelvin a Farenheith \n4.Kelvin a Celcius")
					print("5.Farenheith a Celcius\n6.Farenheith a Kelvin\n7.Salir")
					trans=input("Opcion: ")
					print("")
				if trans=="1":
					def celcius_kelvin():
						print("Transformacion de grados Celcius a Kelvin")
						grados_c=input("Ingrese los grados celcius: ")
						num1=grados_c.isdigit()
						while num1==False:
							print("Opcion incorrecta intente nuevamente.\n")
							grados_c=input("Ingrese los grados celcius: ")
							num1=grados_c.isdigit()
						print("Los grados de Celcius a Kelvin es igual a: ", int(grados_c)+273.15)
					celcius_kelvin()
				if trans=="2":
					def celcius_farenheith():
						print("Transformacion de grados Celcius a Farenheith")
						grados_c=input("Ingrese los grados celcius: ")
						num1=grados_c.isdigit()
						while num1==False:
							print("Opcion incorrecta intente nuevamente.\n")
							grados_c=input("Ingrese los grados celcius: ")
							num1=grados_c.isdigit()
						print("Los grados de Celcius a Farenheith es igual a: ", (9*(int(grados_c))/5)+32)
					celcius_farenheith()
				if trans=="3":
					def kelvin_celcius():
						print("Transformacion de grados Kelvin a Celcius")
						grados_k=input("Ingrese los grados Kelvin: ")
						num1=grados_k.isdigit()
						while num1==False:
							print("Opcion incorrecta intente nuevamente.\n")
							grados_k=input("Ingrese los grados Kelvin: ")
							num1=grados_k.isdigit()
						print("Los grados de Kelvin a Celcius es igual a: ", (grados_k)-273.15)
					kelvin_celcius()
				if trans=="4":
					def celcius_farenheith():
						print("Transformacion de grados Kelvin a Farenheith")
						grados_k=input("Ingrese los grados Kelvin: ")
						num1=grados_k.isdigit()
						while num1==False:
							print("Opcion incorrecta intente nuevamente.\n")
							grados_k=input("Ingrese los grados Kelvin: ")
							num1=grados_k.isdigit()
						print("Los grados de Kelvin a Farenheith es igual a: ", (9*(int(grados_k)-273.15)/5)+32)
					kelvin_farenheith()
				if trans=="5":
					def farenheith_celcius():
						print("Transformacion de grados Farenheith a Celcius")
						grados_f=input("Ingrese los grados Farenheith: ")
						num1=grados_f.isdigit()
						while num1==False:
							print("Opcion incorrecta intente nuevamente.\n")
							grados_f=input("Ingrese los grados Farenheith: ")
							num1=grados_f.isdigit()
						print("Los grados de Farenheith a Celcius es igual a: ", (5*(int(grados_f)-32)/9))
					farenheith_celcius()
				if trans=="6":
					def farenheith_kelvin():
						print("Transformacion de grados Farenheith a Kelvin")
						grados_f=input("Ingrese los grados Farenheith: ")
						num1=grados_f.isdigit()
						while num1==False:
							print("Opcion incorrecta intente nuevamente.\n")
							grados_f=input("Ingrese los grados Farenheith: ")
							num1=grados_f.isdigit()
						print("Los grados de Farenheith a Kelvin es igual a: ", (5*(int(grados_f)-32)/9)+273.15)
					farenheith_kelvin()
				if trans=="7":
					break
			if fun=="5":
				break
		if elegir=="NO":
			break
print("Hasta la proxima")