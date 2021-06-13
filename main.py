from lista import Lista_agenda
a=Lista_agenda()
entrada=True

def Opcion_menu(opcion):
    if opcion == 1:
        nombre=input("Ingrese su nombre: ")
        apellido=input("Ingrese su apellido: ")
        telefono=input("ingrese su telefono: ")
        if a.Buscar_telefono(telefono,1):
            a.Ingresar_contacto(nombre,apellido,telefono)
            print("El contacto se ha agregado exitosamente\n")
        else:
            print("El contacto ya existe\n")
    if opcion ==2:
        telefono=input("Ingrese numero de telefono: ")
        aux=a.Buscar_telefono(telefono,2)
        if aux==True:
            entero=int(input("El número de teléfono no existe ¿Desea agregarlo?\n1. Si\n2. No "))
            if entero==1:
                nombre=input("Ingrese su nombre: ")
                apellido=input("Ingrese su apellido: ")
                a.Ingresar_contacto(nombre,apellido,telefono)
                print("El contacto se ha agregado exitosamente\n")
        else:
            print("Nombre: "+aux.nombre+"\nApellido: "+aux.apellido+"\nTeléfono: "+aux.telefono)
    if opcion == 4:
        global entrada
        entrada=False    

while(entrada):
    print("1. Ingrese nuevo contacto\n2. Buscar contacto\n3. Visualizar agenda\n4. Salir")
    opcion=int(input("Ingrese la opción que desea: "))
    Opcion_menu(opcion)