from nodo import nodo_agenda
n=nodo_agenda

class Lista_agenda:
    def __init__(self):
        self.cabeza=None

    def vacio(self):
        if self.cabeza==None:
            return True
        else: 
            return False

    def Ingresar_contacto(self,nombre,apellido,telefono):
        nuevo=n(nombre,apellido,telefono)
        if self.vacio():
            self.cabeza=nuevo
        else:
           
            aux=self.cabeza
            while aux.siguiente is not None:
                aux=aux.siguiente
            aux.siguiente=nuevo
            aux.siguiente.anterior=aux
            
    
    def Buscar_telefono(self,telefono,condicion):
        aux=self.cabeza
        while(aux!=None):
            if aux.telefono!=telefono:
                aux=aux.siguiente
            else:
                break
        if condicion == 1:
            if aux!=None:
                if aux.telefono == telefono:
                    return False
                else:
                    return True
            else:
                return True
        elif condicion==2:
            if aux!=None:
                if aux.telefono==telefono:
                    return aux
                else:
                    return True
            else:
                return True
