17 # Defino un DATO de tipo numerico con valor 17

"hola" # Defino un DATO de tipo texto con valor hola
# Donde se deposita ese dato? En la memoria RAM
# Python... tonto tonto no es... y esas lineas anteriores... al no tener una variable...
# Ya sabe que esos DATOS son basura... y directamente no los pone en RAM

True 

# Tiene python comentario en bloque? NO

texto = """
linea 1 de código
linea 2 de código
"""
print(texto)

"""
linea 1 de código
linea 2 de código
"""
numero = 17

         ###### EXPRESION
numero = numero + 5        # STATEMENT

# Felipe es aquel chico de alli
# Él es muy inteligente!
# ^ Pronombre, que me permite refrirme a FELIPE !
# Y aquel es Lucas
# Él es muy poco inteligente!

# Cuantas cosas hace esa linea? 3
# - 17      -> Defino un DATO de tipo numerico con valor 17 y lo guardo en RAM
# - numero  -> Define una variable con nombre: numero
# - =       -> Asigna la variable al valor 17

numero = 25
# Cuantas cosas hace esa linea? 3
# - 25      -> Defino un DATO de tipo numerico con valor 25 y lo guardo en RAM. DONDE? No, en otro sitio
#               En este punto cuantas cosas tengo en RAM? 2: El 17 y el 25
# - numero  -> Toma la variable con nombre: numero
# - =       -> Asigna la variable al valor 25
#               En este momento el 17 se convierte en BASURA (GARBAGE) ya que nadie apunta hacia él
#               Y en algún momento entra el RECOLECTOR DE BASURA (GARBAGE COLLECTOR): Python, Java, JS

# En python, Java, JS
# Una variable es una referencia a un DATO que tengo en memoria.

# En ansible nos lo vamos a plantear de otra forma diferente.
# En ansible una variable la entendemos como un CAJON donde meto cosas

try:
    print("HOLA")
except:
    print("solo me ejecuto en caso de error")
finally:
    print("me ejecuto en cualquier caso")
else:
    print("me ejecuto solo si ha ido bien")