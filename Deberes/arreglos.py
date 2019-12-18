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
 
def editar():.