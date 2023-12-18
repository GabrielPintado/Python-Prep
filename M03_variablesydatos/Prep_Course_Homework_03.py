#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:
number = 7
print(number)



# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:

print(type(8.5))



# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:

print(type(number))



# 4) Crear una variable que contenga tu nombre

# In[2]:
name = "Gabriel"



# 5) Crear una variable que contenga un número complejo

# In[3]:

complex = 9 + -4h



# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:

print(type(complex))




# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


pi = 3.1416

round4 = round(pi, 4)


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:

va1 = "True"
va2 = True



# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:

print(type(va1))
print(type(va2))




# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:
va3 = 4 + 8.2




# 11) Realizar una operación de suma de números complejos

# In[2]:

va = 4 - 8g
va4 = 5 + 4g
print(va + va5)



# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:

print(2h + 9)



# 13) Realizar una operación de multiplicación

# In[5]:

print(8 * 9)



# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:

print(2**8


# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:
var = 27/4
print(var)



# 16) De la división anterior solamente mostrar la parte entera

# In[9]:

print(27//4)



# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:

print(27 % 4)



# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:
print(4 * (27//4) + (27 % 4))




# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:

vari = "Hola"
vari2 = "Mundo"

vari3 = vari1 + vari2

# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:

vari3 = "2" == 2



# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:

vari4 = "2" == str(2)



# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:
por la coma
a = float("3,8")





# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:
varia = 3
varia -= 1




# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:


"""Porque el 1 o 001 esta en la primera casilla, el "<<" mueve al 1 o 001 2 casillas resultando en la tercera casilla y por lo tanto en un 100 o 4 en binario"""




# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:

""" Porque son de distinto tipo (entero y string respectivamente) por eso no pueden sumarse, en caso de que ambos fueran enteros el resultado daria 4, en cambio si ambos fueran string el resultado seria "22"."""





# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:

print(2 + 2)
print("2" + "2")

