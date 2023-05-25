import sys

## LONGITUD DE UNA PRASE
print ('LONGITUD DE UNA FRASE')
#Crear un programa para identificar la longitud de una palabra ingresada. 
# La palabra correcta debe tener entre cuatro y ocho letras. 
# toma en cuenta las siguientes consideraciones:
palabra = input('Ingresa una palabra entre 4 y 8 caracteres: ')

# Si la longitud de la palabra se encuentra en el rango de cuatro a ocho letras, 
# se debe imprimir un mensaje que indique que la palabra es correcta
longitud = len(palabra)

if longitud >= 4 and longitud <= 8 :
    print ('La palabra es correcta')

# Si la palabra tiene menos de 4 letras debe indicar un mensaje que diga: 
# Hacen falta letras. Solo tiene N letras (siendo N el número de letras de la palabra)
if longitud < 4 :
    print (f'Hace falta letras. Solo tiene {longitud} letras')

# Si la palabra tiene más de 8 letras debe indicar un mensaje que diga: 
# Sobran letras. Tiene N letras ((siendo N el número de letras de la palabra))
if longitud > 8 :
    print (f'Sobran letras. Tiene {longitud} letras')

############################################################################## 
    
## ENCUENTRA EL CUADRANTE
 
print ('ENCUENTRA EL CUADRANTE')

# Crear un programa que en base a 2 números de entrada, coordenadas, identifique en cuál 
# de los 4 cuadrantes se encuentra el punto. El programa debe verificar que ninguna 
# coordenada sea 0. Por ejemplo

# Ingrese X:
x = int(input('Escribe el valor de X: '))
# Ingrese Y:
y = int(input('Escribe el valor de Y: '))

    
    
# El punto se encuentra en el cuadrante ??

if x > 0 and y > 0 :
    print('El punto se encuentra en el cuadrante I')
if x > 0 and y < 0 :
    print('El punto se encuentra en el cuadrante IV')
if x < 0 and y < 0 :
    print ('El punto se encuentra en el cuadrante III')
if x < 0 and y > 0 :
    print ('El punto se encuentra en el cuadrante II')
elif x == 0 or y == 0:
    print ('Los valores deben ser diferentes de 0')
    

