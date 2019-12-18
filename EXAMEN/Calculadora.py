#Examen bimestral Nombre:JEFFERSON  GILBERTO ALQUINGA CHUQUIMARCA. FUNDAMENTOS DE PROGRAMACIÒN
import math
while 1:

    print('Para el valor de funciones trigonometricas escoger solo variable x, ademas en calculo de areas x= lado=radio y=altura')

    x= float(input('Indica el valor de x:'))
    y= float(input('Indica el valor de y:'))
    
    print(' Selecciona la operacion que desees realizar:')
    print('1. Suma')
    print('2.Resta')
    print('3.Multiplicaicon')
    print('4.División')
    print('5.Potencia')
    print('6.Logaritmo(logaritmo del primer número [x])')
    print('7.volumen de un cilindro, donde x=radio, y=altura')
    print('8.area de un cuadrado')
    print('9.area de un triangulo ')
    print('10.Factorial(del primer numero[x])')
    print('Funciones Trigonometricas')
    print('11.cos(x)')
    print('12.sin(x)')
    print('13.tan(x)')
  

    n= int(input('¿Cuál opcion quieres?'))


    if n==1:
        Resultado=x+y
        print(Resultado)

    elif n==2:
        Resultado=x-y 
        print(Resultado)
    elif n==3:
        Resultado=x*y    
        print(Resultado)
    elif n==4 and y!=0:
        Resultado=x/y    
        print(Resultado)
    elif n==5:
        Resultado=x**y    
        print(Resultado)
    elif n==6 and x>0:
        Resultado=math.log10(x)   
        print(Resultado)

    elif n==7 and x>0 and y>0: 
        Resultado=(math.pi * x * x * y)
        print(Resultado)
    elif n==8:
        Resultado=x*x   
        print(Resultado)
    elif n==9:
        Resultado=(x*y)/2
        print(Resultado)
    elif n==10:
        Resultado=math.factorial(x)
        print(Resultado)
        
    elif n==11:
        Resultado= math.cos(x)
        print(Resultado)

    elif n==12:
        Resultado= math.sin(x)
        print(Resultado)

    elif n==13:
        Resultado= math.tan(x)
        print(Resultado)

    print('FIN VUELVA PRONTO')
