#!/usr/bin/env python
# coding: utf-8

# ## Funciones

# 1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es

# In[1]:

def prim(nu):
  es = True
  for i in range(2,nu):
    if nu % i == 0:
      es = False
      break
  return es
      
print(prim(int(input())))



# 2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista

# In[25]:

b = [1, 4, 7, 34, 53 ,7 ,2 ,52]

def pr(lista):
  n_li = []
  for i in lista:
    if prim(i):
      n_li.append(i)
  return n_li
      
print(pr(b))



# 3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera

# In[33]:

a = [12, 451, 526, 36, 47, 25, 234, 521, 1, 3, 7, 465, 347, 4, 27, 35, 3, 1, 412, 41, 4, 5, 32, 1, 42, 41, 3, 5, 12, 4, 2, 4, 14, 2, 2, 4, 2, 4, 1, 1, 3, 34, 24, 1, 3, 3, 3, 3, 3, 3, 3, 14]

def mas(n):
  lis = {}
  for i in n:
    if str(i) in lis:
      lis[str(i)] += 1
    else:
      lis[str(i)] = 1
  m = max(lis, key=lis.get)
  n = lis[m]
  return m, n


print(mas(a))



# 4) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
# Fórmula 1	: (°C × 9/5) + 32 = °F<br>
# Fórmula 2	: °C + 273.15 = °K<br>
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
# 

# In[56]:
def con(val, ori, des):
    
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
    
print(con(int(input()), input(), input()))


# 5) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:

# In[62]:

def con(val, ori, des):
    
    if ori == "Celsius":
        if des == "Farenheit":
            val =  1.8 * val + 32
        elif des == "Kelvin":
            val = val + 273.15
        elif des == ori:
            return val
        else:
            print("no valido")
        
    elif ori == "Farenheit":
        if des == "Celsius":
            val = (val - 32) / 1.8
        elif des == "Kelvin":
            val = ((val - 32) / 1.8) + 273.15
        elif des == ori:
            return val
        else:
            print("no valido")
            
    elif ori == "Kelvin":
        if des == "Farenheit":
            val = ((val - 273.15) * 1.8 + 32) 
        elif des == "Celsius":
            val = val - 273.15
        elif des == ori:
            return val
        else:
            print("no valido")
        
    else:
        print("no valido")
    
    return(val)

g = ["Celsius", "Farenheit", "Kelvin"]

for i in g:
    for e in g:
        print("1 grado", i, "a", e, "es:", con(1, i, e))


# 6) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo

# In[65]:

def fac(val):
    if val > 0:
        nu = 1
        for i in range(1, int(val + 1)):
          nu *= i
        return nu
    else:
        return "valor no valido"

print(fac(int(input())))



