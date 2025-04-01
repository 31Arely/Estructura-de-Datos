import numpy as np

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

print(x.matriz[1][0])