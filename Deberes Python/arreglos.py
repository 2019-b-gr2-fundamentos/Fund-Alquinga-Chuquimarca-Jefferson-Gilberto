listacontacto=[]
contacto = {}
def listar ():
    for cont in listacontacto:
        print (cont["nombre"],"-",cont["celular"],"-",cont["correo"],"-",cont["direccion"],"-",cont["cumpleaños"])
def agregar():
    contacto = {}
    contacto ["nombre"] = input ("Ingrese nombre:")
    contacto ["celular"] = input ("Ingrese celular:")
    contacto ["correo"] = input ("Ingrese correo:")
    contacto ["direccion"] = input ("Ingrese direccion:")
    contacto ["cumpleaños"] = input ("Ingrese fecha de nacimiento:")
    listacontacto.append(contacto)
 
def buscarnombre(nombrebuscar):
    for cont in listacontacto:
        if (cont["nombre"]== nombrebuscar):
            print (cont["nombre"],"-",cont["celular"],"-",cont["correo"],"-",cont["direccion"],"-",cont["cumpleaños"])
def buscarcorreo(correobuscar):
    for cont in listacontacto:
        if (cont["correo"]== correobuscar):
            print (cont["nombre"],"-",cont["celular"],"-",cont["correo"],"-",cont["direccion"],"-",cont["cumpleaños"])
 
def editar():
 
 
 
def menu():
 while (True):
    print("--------------------")
    print("       Agenda       ")
    print("1.-Agregar contacto:")
    print("2.-Buscar contacto:")
    print("3.-Editar contacto:")
    print("4.-Eliminar contacto:")
    print("5.-Listar contactos")
    print("6.-Salir")
    while (True):
        op = input("Digite una opcion:")
        if(op!=""):
            break
 
    if (op == "1"):
        agregar()
    elif (op == "2"):
        print ("1.-Buscar por nombre:")
        print("2.-Buscar por correo")
        op1 = input ("Digite opcion:")
        if (op1=="1"):
            nombrebuscar=input ("Nombre:")
            buscarnombre(nombrebuscar)
        elif (op1=="2"):
            correobuscar=input ("Correo:")
            buscarcorreo(correobuscar)
 
 
    elif (op == "3"):
        editar()
    elif (op == "4"):
 
    elif( op == "5"):
        listar()
    elif (op == "6"):
        break
 
menu()