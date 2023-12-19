#!/usr/bin/env python
# coding: utf-8

# ## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

# In[3]:

l = ["Cusco", "Buenos Aires", "Santo Domingo", "Ciudad de México", "Nueva York", "Madrid", "París", "Génova"] 
print(l)


# 2) Imprimir por pantalla el segundo elemento de la lista

# In[4]:

print(l[1])


# 3) Imprimir por pantalla del segundo al cuarto elemento

# In[8]:

print(l[1:5])




# 4) Visualizar el tipo de dato de la lista

# In[12]:

print(type(l))



# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

# In[14]:

print(l[2:])



# 6) Visualizar los primeros 4 elementos de la lista

# In[15]:

print(l[:4])

    


# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

# In[16]:

l.append("París")
l.append("Roma")

"""No arroja error, solo se repite en caso de que ya esté"""






# 8) Agregar otra ciudad, pero en la cuarta posición

# In[20]:

l.insert(3, "Berlín")



# In[21]:




# 9) Concatenar otra lista a la ya creada

# In[22]:

a = [1, 2, 3, 4]
l.extend(a)


# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

# In[23]:

print(l.index("París"))
"""Solo va a encontrar el primero de los 2"""


# 11) ¿Qué pasa si se busca un elemento que no existe?

# In[24]:

"""ValueError: 'Parí' is not in list"""



# 12) Eliminar un elemento de la lista

# In[25]:

l.remove("Madrid")



# 13) ¿Qué pasa si el elemento a eliminar no existe?

# In[27]:


"""ValueError: list.remove(x): x not in list"""


# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

# In[28]:

p = l.pop()
print(l)
print(p)



# 15) Mostrar la lista multiplicada por 4

# In[29]:

print(l * 4)


# 16) Crear una tupla que contenga los números enteros del 1 al 20

# In[32]:

t = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)


# 17) Imprimir desde el índice 10 al 15 de la tupla

# In[35]:

print(t[10:15])


# 18) Evaluar si los números 20 y 30 están dentro de la tupla

# In[41]:

print(20 in t)
print(30 in t)



# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

# In[48]:

print("París" in l)
if not "París" in l:
    l.append("París")
    print(l)



# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

# In[51]:

c = 0
inp = str(input())
for i in l:
    if i == inp:
        c += 1
        
print(c)



# 21) Convertir la tupla en una lista

# In[52]:

tl = list(t)



# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

# In[55]:

tu = (1,2,3)
a,b,c = tu
print(a)
print(b)
print(c)



# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".

# In[57]:

d={}

d["ciudades"] = l
d["Paises"] = ["Perú", "Argentina", "México"]
d["Continentes"] = ["América", "Europa", "Asia"]

print(d)




# 24) Imprimir las claves del diccionario

# In[59]:

print(d.keys())


# 25) Imprimir las ciudades a través de su clave

# In[61]:

print(d["ciudades"])


