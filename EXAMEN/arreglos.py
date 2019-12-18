'''#Examen bimestral Nombre:JEFFERSON  GILBERTO ALQUINGA CHUQUIMARCA. FUNDAMENTOS DE PROGRAMACIÒN'''
while 1 :
    print("HOLA TRABAJEMOS")

    
    print('Marcas de Zapatos')
    Zapatos=['Nike','adidas','Converse']
    cantidades=[1,2,3,4,5]
    matriz=[[1,2,3],[4,5,6],[9,7,2]]
    print(Zapatos)
    print(cantidades)
    print(matriz)

    #Crear lista de teclado
    Zapatos=[]
    n=int(input("¿Cuántos Zapatos?"))
    for i in range(n):
        Zapato=input("Zapato: ")
        Zapatos.append(Zapato)
    print(Zapatos)

    #Reemplazar elementos 
    n=int(input("¿Modificar Un Elemento?"))
    print(Zapatos)
    Zapatos[n]='puma'
    print(Zapatos)
   
    n=int(input("¿Deseas cmabiar del 1 al 3 por puma o converse?"))
    Zapatos[1:3]=['Puma','Converse']
    print(Zapatos)
    n=int(input("¿Eliminar valores de la Lista?"))
    Zapatos[n]=[]
    print(Zapatos)
    del Zapatos[n];
    print(Zapatos)






    print("Muchas Gracias.")

    print("")
    