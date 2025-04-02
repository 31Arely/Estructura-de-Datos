class Pila:
    def __init__(self):
        self.pila = []     #se declara vacia la lista de elementos
    
    def contar_elementos(self):
        return len(self.pila)
    
    def mostrar_contenido(self):
        return self.pila
    
    def imprimir_contenido(self):
        print(self.pila)
    
    def contiene(self, elemento):
        return elemento in self.pila
    
    def insertar(self, elemento):
        if isinstance(elemento, str):
            self.pila.append(elemento)
        else:
            raise ValueError("Solo se permiten objetos String")
    
    def sacar(self):
        if not self.pila:
            return None
        return self.pila.pop()
    
    def siguiente(self):
        if not self.pila:
            return None
        return self.pila[-1]
    


#crear clase cola
class Cola:
    def __init__(self):
        self.cola = []     #se declara vacia la lista de elementos
    
    def contar_elementos(self):
        return len(self.cola)
    
    def mostrar_contenido(self):
        return self.cola
    
    def contiene(self, elemento):
        return elemento in self.cola
    
    def insertar(self, elemento):
        self.cola.append(elemento)
    
    def sacar(self):
        if not self.cola:
            return None
        return self.cola.pop(0)
    
    def siguiente(self):
        if not self.cola:
            return None
        return self.cola[0]


class AplicacionEstructuras:
    def __init__(self):
        self.pila = Pila()
        self.cola = Cola()

    def ejecutar(self):
        #ejemplo 1: pila en un problema de matematicas
        print("Ejemplo 1: Pila para expresiones matematicas (String)")
        self.pila.insertar("3 + 2")
        self.pila.insertar("( 5 * 4 )")
        self.pila.insertar("7 - 6")
        print(f"Contenido de la pila: {self.pila.mostrar_contenido()}")
        print(f"Siguiente en la pila: {self.pila.siguiente()}")
        print(f"Sacando de la pila: {self.pila.sacar()}")
        print(f"Contenido de la pila después de sacar: {self.pila.mostrar_contenido()}")
        print("-----------------------------------------------------------------------------")
        
        #ejemplo 2: cola para una fila de atención de clientes
        print("\nEjemplo 2: Cola para atención de clientes")
        self.cola.insertar({"cliente": "Juan", "asunto": "Consulta"})
        self.cola.insertar({"cliente": "Ana", "asunto": "Reclamación"})
        self.cola.insertar({"cliente": "Luis", "asunto": "Compra"})
        print(f"Contenido de la cola: {self.cola.mostrar_contenido()}")
        print(f"Siguiente en la cola: {self.cola.siguiente()}")
        print(f"Sacando de la cola: {self.cola.sacar()}")
        print(f"Contenido de la cola después de sacar: {self.cola.mostrar_contenido()}")

#ejecucion de la clase principal
if __name__ == "__main__":
    app = AplicacionEstructuras()
    app.ejecutar()