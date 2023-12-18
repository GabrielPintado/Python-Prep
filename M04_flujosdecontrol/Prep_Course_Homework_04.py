#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:

v = 6
print(6 < 0)



# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:

v1 = 4
v2 = "ocho"
if type(v1) == type(v2):
  print("son del mismo tipo")


# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:

for i in range(21):
  if i % 2 == 0:
    print(str(i) + " es par")
  else:
    print(str(i) + " es impar")



# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:
for i in range(6):
  print(i ** 3)




# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:

v3 = 4
for i in range(v3):
  print(i)



# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:

v4 = int(input())
if v4 > 0:
    fac = v4
    while v4 > 2:
      v4 -= 1
      fac *= v4
      print(fac)
else:
  print("ingrese un numero mayor a 0")



# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:
va = 8
while va > 0:
  for i in range(va):
    print(str(i))
    va -= 1



# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:
va = 8
for i in range(va):
  va -= 1
  while va % 2 == 0:
    va -= 3
    print((i * 2))
  




# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:

n = 0
while n < 30:
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
    if primo:
        print(n)
    n += 1
    
    


# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:

n = 0
while n < 30:
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
            break
    if primo:
        print(n)
    n += 1

# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:

"""El break hace que el bucle se pare cuando se localice el primo, haciendo que no tenga que hacer el proceso con le resto de numeros en el rango hasta la otra vuelta"""


# In[57]:
"""Se puede comprobar algo imprimiendo algo cuando no es primo"""
n = 0
while n < 30:
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
            print("----")
    if primo:
        print(n)
    n += 1
"""en este caso aunque se encuentre al primo en el bucle, sigue hasta que termine el rango"""
n = 0
while n < 30:
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
            print("----")
            break
    if primo:
        print(n)
    n += 1
"""en cambio el break termina el rastreo cuando se encuentra el primo"""

# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:

n = 100
while n <= 300:
  if n % 12 != 0:
    n += 1
    continue
  print(n)
  n += 1




# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:

n = 0
while n < 30:
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
            break
    if primo:
        print(n)
        if str(input("¿quiere continuar?")) == "no":
            break
        
        
    n += 1


# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:

n = 100
while n <= 300:
  if n % 6 != 0:
    n += 1
    continue
  print(n)
  break


