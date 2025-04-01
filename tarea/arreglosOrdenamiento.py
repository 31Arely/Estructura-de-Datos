"""import numpy as np

arregloNP = np.array([True, "hola"])

print(arregloNP)

class Estructura:
  def __init__(self):

    self.arreglo=[]
    self.matriz=[[1,2,3],[3,4],[5,6]]
    self.arregloNP=np.array([],dtype=int)

  def insertar(self,valor):
    self.arreglo.append(valor)

  def insertarNP(self,i,valor):
    if 0 <= i <= len(self.arregloNP):
        self.arregloNP = np.insert(self.arregloNP,i,valor)
    else:
        print("Índice no válido")

  def eliminarPorI(self,i):
    self.arreglo.pop(i)
  def eliminarPorV(self,valor):
    self.arreglo.remove(valor)
  def eliminarUltimo(self):
    self.arreglo.pop()

  def eliminarPorINP(self,i):
    self.arregloNP = np.delete(self.arregloNP,i)

  def eliminarPorVNP(self,valor):
    i=0
    while i < len(self.arregloNP):
      if valor == self.arregloNP[i]:
        self.arregloNP = np.delete(self.arregloNP,i)
      i+=1

  def eliminarUltimoNP(self):
    if len(self.arregloNP) > 0:
      i = len(self.arregloNP)-1
      self.arregloNP = np.delete(self.arregloNP,i)
    else:
      print("Arreglo vacio")

  def modificarPorI(self,i,valor):
    self.arreglo[i] = valor

  def modificarPorV(self,valor,valorModificado):
    i=0
    while i < len(self.arreglo):
      if valor == self.arreglo[i]:
        self.arreglo[i] = valorModificado
        break
      i+=1

  def modificarPorINP(self,i,valor):
    self.arregloNP[i] = valor
  def modificarPorVNP(self,valor,valorModificado):
    i=0
    while i < len(self.arregloNP):
      if valor == self.arregloNP[i]:
        self.arregloNP[i] = valorModificado
        break
      i+=1

x = Estructura()

x.insertarNP(0,4)

x.modificarPorVNP(4,50)

print(x.matriz)

print(x.matriz[1][0])"""


#tomando como base lo anterior...
#Crear una función de ordenamiento ascendente y descendente utilizando el archivo presentado en clase. 
#Realicen las acciones necesarias para poder imitar el comportamiento de la 
#función sort() y reverse() en cada caso.

#Estas funciones se deben aplicar para arreglos:
#Tipo list
#Tipo np.array


import numpy as np

class Estructura:
    def __init__(self):
        self.arreglo = []
        self.matriz = [[1, 2, 3], [3, 4], [5, 6]]
        self.arregloNP = np.array([], dtype=int)

    def insertar(self, valor):
        self.arreglo.append(valor)

    def insertarNP(self, i, valor):
        if 0 <= i <= len(self.arregloNP):
            self.arregloNP = np.insert(self.arregloNP, i, valor)
        else:
            print("indice no valido")

    def eliminarPorI(self, i):
        self.arreglo.pop(i)

    def eliminarporV(self, valor):
        self.arreglo.remove(valor)

    def eliminarUltimo(self):
        self.arreglo.pop()

    def eliminarPorINP(self, i):
        self.arregloNP = np.delete(self.arregloNP, i)

    def eliminarPorVPN(self, valor):
        i = 0 
        while i < len(self.arregloNP):
            if valor == self.arregloNP[i]:
                self.arregloNP = np.delete(self.arregloNP, i)
            i += 1

    def eliminarUltimoNP(self):
        if len(self.arregloNP) > 0:
            i = len(self.arregloNP) -1
            self.arregloNP = np.delete(self.arregloNP, i)
        else:
            print("arreglo vacio")

    def modificarPorI(self, i, valor):
        self.arreglo[i] = valor   

    def modificarPorV(self, valor, valorModificado):
        i = 0 
        while i < len(self.arreglo):
            if valor == self.arreglo[i]:
                self.arreglo[i] = valorModificado
                break
            i += 1

    def modificarPorINP(self, i, valor):
        self.arregloNP[i] = valor

    def modificarPorVNP(self, valor, valorModificado):
        i = 0
        while i < len(self.arregloNP):
            if valor == self.arregloNP[i]:
                self.arregloNP[i] = valorModificado
                break
            i += 1

    #fucniones de ordenamiento para listas (tipo list)
    def orden_ascendente(self):
        n = len(self.arreglo)
        for i in range(n):
            for j in range(0, n -i -1):
                if self.arreglo[j] > self.arreglo[j + 1]:
                    self.arreglo[j], self.arreglo[j + 1] = self.arreglo[j + 1], self.arreglo[j]

    def orden_descendente(self):
        n = len(self.arreglo)
        for i in range(n):
            for j in range(0, n - i -1):
                if self.arreglo[j] < self.arreglo[j + 1]:
                    self.arreglo[j], self.arreglo[j + 1] = self.arreglo[j + 1], self.arreglo[j]

    #funciones de ordenamiento para arreglos tipo np.array
    def ordenNP_ascendente(self):
        n = len(self.arregloNP)
        for i in range(n):
            for j in range(0, n - i - 1):
                     if self.arregloNP[j] > self.arregloNP[j + 1]:
                      self.arregloNP[j], self.arregloNP[j + 1] = self.arregloNP[j + 1], self.arregloNP[j]

    def ordenNP_descendente(self):
        n = len(self.arregloNP)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.arregloNP[j] < self.arregloNP[j + 1]:
                  self.arregloNP[j], self.arregloNP[j + 1] = self.arregloNP[j + 1], self.arregloNP[j]

#ejemplo de uso
x = Estructura()

#listas
x.insertar(7)
x.insertar(3)
x.insertar(9)
x.orden_ascendente()
print("la lista en orden ascendente es: ", x.arreglo)
x.orden_descendente()
print("la lista en orden descendente es: ", x.arreglo)
    
#arreglos numpy
x.insertarNP(0, 4)
x.insertarNP(1, 0)
x.insertarNP(2, 6)
x.ordenNP_ascendente()
print("el arreglo en orden ascendente es: ", x.arregloNP)
x.orden_descendente()
print("el arreglo en orden descendente es: ", x.arregloNP)