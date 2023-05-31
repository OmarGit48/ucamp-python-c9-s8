import sys

## LONGITUD DE UNA PRASE
print ('LONGITUD DE UNA FRASE')
#Crear un programa para identificar la longitud de una palabra ingresada. 
# La palabra correcta debe tener entre cuatro y ocho letras. 
# toma en cuenta las siguientes consideraciones:
# Si la longitud de 1
# la palabra se encuentra en el rango de cuatro a ocho letras, 
# se debe imprimir un mensaje que indique que la palabra es correcta
palabra = input('Ingresa una palabra entre 4 y 8 caracteres: ') # Se solicita ingresar una palabra

longitud = len(palabra) # Se de una variable a la medida de la palabra

if longitud >= 4 and longitud <= 8 : # Si la palabra esta dentro de dicho rango se imprime que esta coorecta
    print ('La palabra es correcta')

# Si la palabra tiene menos de 4 letras debe indicar un mensaje que diga: 
# Hacen falta letras. Solo tiene N letras (siendo N el número de letras de la palabra)
if longitud < 4 : # Aqui es donde el codigo detecta uq etiene menos de 4 letras la longitud de la palabra y dice que faltan
    print (f'Hace falta letras. Solo tiene {longitud} letras')

# Si la palabra tiene más de 8 letras debe indicar un mensaje que diga: 
# Sobran letras. Tiene N letras ((siendo N el número de letras de la palabra))
if longitud > 8 : # Aqui es donde se detecta que hay mas d e8 letras y hace mecion del sobrante
    print (f'Sobran letras. Tiene {longitud} letras')

############################################################################## 
    
## ENCUENTRA EL CUADRANTE
 
print ('ENCUENTRA EL CUADRANTE')

# Crear un programa que en base a 2 números de entrada, coordenadas, identifique en cuál 
# de los 4 cuadrantes se encuentra el punto. El programa debe verificar que ninguna 
# coordenada sea 0. Por ejemplo

# Ingrese X: para poder dar el valor horizontal
x = int(input('Escribe el valor de X: '))
# Ingrese Y: para dar calor vertical en el cuadrante
y = int(input('Escribe el valor de Y: '))
  
# El punto se encuentra en el cuadrante ??

if x > 0 and y > 0 : # si el numero es POSITIVO tanto X como Y, nos da este punto el cuadrante I
    print('El punto se encuentra en el cuadrante I')
    # y si no...
elif x > 0 and y < 0 :  # Este punto de codigo dice que si Y es NEGATIVO y X es POSITIVO, este estara en la parte baja de la horizontal X
    print('El punto se encuentra en el cuadrante IV')
     # y si...
elif x < 0 and y < 0 : # Este punto de codigo dice que si Y es NEGATIVO y X es NEGATICO, el punto estara a la izquierda de la vertical Y y abajo de la horizontal X
    print ('El punto se encuentra en el cuadrante III')
    # y si...
elif x < 0 and y > 0 : # Este punto de codigo dice que si Y es POSITIVA y X es NEGATIVO, este estara en la parte derecha de la vertical Y y por arriba de la horizontal X
    print ('El punto se encuentra en el cuadrante II')
else : #y si no es ninguno de los casos anteriores, quiere decir que es 0 alguno de los dos o ambos
    print ('Los valores deben ser diferentes de 0')
    

