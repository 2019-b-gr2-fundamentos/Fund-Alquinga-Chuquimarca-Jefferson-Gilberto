'''#Examen bimestral Nombre:JEFFERSON  GILBERTO ALQUINGA CHUQUIMARCA. FUNDAMENTOS DE PROGRAMACIÒN'''

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
n=int(input("¿Cuàl elemento?"))
Zapatos[0]='puma'
print(Zapatos)
Zapatos[-1]='New Balance'
print(Zapatos)
Zapatos[1:3]=['Reebok','Havaianas']
print(Zapatos)
Zapatos[1:3]=[]
print(Zapatos)
del Zapatos[0]
print(Zapatos)
Zapatos=['Nike','adidas','Converse','Reebok']
Zapatos.remove('Reebok')
print(Zapatos)
#Insertar
Zapatos[1:1]=['Bibi Lou','Buffalo','Aldo']
print(Zapatos)
Zapatos.insert(3,'ART')
print(Zapatos)
#Copiar listas 
Zapatos2=Zapatos.copy()
print(Zapatos2)
Zapatos3=Zapatos[:]
print (Zapatos3)
#Pop
Zapatos2.pop()
print(Zapatos2)
Zapatos2.pop(2)
print(Zapatos2)
Zapatos.extend(Zapatos3)
print(Zapatos)
Zapatos2.clear()
print(Zapatos2)
#Modificar valores de una lista 
r=['A','B','C','D','E']
for i,letra in enumerate(r):
    r[i]=letra.lower()
    print(r)


