#!/usr/bin/env python
# coding: utf-8

# ## Clases y Programación Orientada a Objetos

# 1) Crear la clase vehículo que contenga los atributos:<br>
# Color<br>
# Si es moto, auto, camioneta ó camión<br>
# Cilindrada del motor

# In[1]:

class vehiculo:
  __init__(self, color, tipo, cilindrada):
  self.color = color
  self.tipo = tipo
  self.cilindrada = cilindrada


# 2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
# Acelerar<br>
# Frenar<br>
# Doblar<br>

# In[5]:

class vehiculo:
  __init__(self, color, tipo, cilindrada):
  self.color = color
  self.tipo = tipo
  self.cilindrada = cilindrada
  self.velocidad = 0
  self.direccion = 0

  
  def acelerar(self, n):
    self.velocidad += n
  def frenar(self, n):
    self.velocidad -= n
  def doblar(self, n):
    self.direccion += n
    



# 3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado

# In[6]:

c1 = vehiculo("rojo", "BMW", 2)
c2 = vehiculo("azul", "VolksWagen", 1)
c3 = vehiculo("verde", "Nissan", 3)

c1.acelerar
c1.frenar
c1.doblar
c2.acelerar
c2.frenar
c3.acelerar
c3.frenar
c3.doblar



# 4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada

# In[12]:

class vehiculo:
  __init__(self, color, tipo, cilindrada):
  self.color = color
  self.tipo = tipo
  self.cilindrada = cilindrada
  self.velocidad = 0
  self.direccion = 0

  
  def acelerar(self, n):
    self.velocidad += n
  def frenar(self, n):
    self.velocidad -= n
  def doblar(self, n):
    self.direccion += n
  def mostrar1(self):
    print(f "soy un automovil {self.color} de tipo {self.tipo} y con {self.cilindrada} de cilindrada)
  def mostrar2(self):
    print(f"el automovil tiene una velocidad de {self.velocidad} y una dirección de {self.direccion}")




# In[13]:






# 5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 7<br>
# Verificar Primo<br>
# Valor modal<br>
# Conversión grados<br>
# Factorial<br>

# In[33]:

class verificador:

  
  def primo(nu):
  es = True
  for i in range(2,nu):
    if nu % i == 0:
      es = False
      break
  return es

  def moda(n):
  lis = {}
  for i in n:
    if str(i) in lis:
      lis[str(i)] += 1
    else:
      lis[str(i)] = 1
  m = max(lis, key=lis.get)
  n = lis[m]
  return m, n

  def grado(val, ori, des):
    
    if ori == "Celsius":
        if des == "Farenheit":
            val =  1.8 * val + 32
        elif des == "Kelvin":
            val = val + 273.15
        else:
            print("no valido")
        
    elif ori == "Farenheit":
        if des == "Celsius":
            val = (val - 32) / 1.8
        elif des == "Kelvin":
            val = ((val - 32) / 1.8) + 273.15
        else:
            print("no valido")
            
    elif ori == "Kelvin":
        if des == "Farenheit":
            val = ((val - 273.15) * 1.8 + 32) 
        elif des == "Celsius":
            val = val - 273.15
        else:
            print("no valido")
        
    else:
        print("no valido")
    
    return(val)

def factorial(n):
   if n == 1:
       return n
   else:
       return n*factorial(n-1)





# 6) Probar las funciones incorporadas en la clase del punto 5

# In[28]:

a = verificador()

b = [1, 2, 3, 4, 5, 6, 7]

a.primo(3)

a.moda(b)

a.grado(9, Celsius, Kelvin)

a.factorial(5)





# 7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se aplquen las funciones incorporadas

# In[55]:

class verificador:


  def __init__(self, lista):
    self.lista = lista
  
  def primo(nu):
  es = True
  for i in range(2,nu):
    if nu % i == 0:
      es = False
      break
  return es

  def moda(n):
  lis = {}
  for i in n:
    if str(i) in lis:
      lis[str(i)] += 1
    else:
      lis[str(i)] = 1
  m = max(lis, key=lis.get)
  n = lis[m]
  return m, n

  def grado(val, ori, des):
    
    if ori == "Celsius":
        if des == "Farenheit":
            val =  1.8 * val + 32
        elif des == "Kelvin":
            val = val + 273.15
        else:
            print("no valido")
        
    elif ori == "Farenheit":
        if des == "Celsius":
            val = (val - 32) / 1.8
        elif des == "Kelvin":
            val = ((val - 32) / 1.8) + 273.15
        else:
            print("no valido")
            
    elif ori == "Kelvin":
        if des == "Farenheit":
            val = ((val - 273.15) * 1.8 + 32) 
        elif des == "Celsius":
            val = val - 273.15
        else:
            print("no valido")
        
    else:
        print("no valido")
    
    return(val)

def factorial(n):
   if n == 1:
       return n
   else:
       return n*factorial(n-1)


# 8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del módulo y probar alguna de sus funciones

# In[1]:




