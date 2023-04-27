
item.failed == True
  True      == True -> True
  False     == True -> False
  

# Inventarios

Un catalogo de entornos donde quiero que se ejecuten los playbooks.
En ese catálogo (que no siempre... más bien NUNCA será un fichero, 
salvo en algunos ejemplos que usaremos en el curso) vamos a definir
un listado con todos esos entornos, juntos con:
- los datos para conectar con esos entornos
- y otros datos opcionales que me puedan interesar

## Definición de inventarios

Ansible nos ofrece 3 formas de definir inventarios... (en realidad serán 6):
- Archivos ini    = NO SE HACE JAMAS DE LOS JAMASES
- Archivos yaml   = NO SE HACE JAMAS DE LOS JAMASES
- Carpetas        = ASI ES COMO SE TRABAJA !


# Contenedor

Alternativa a las MV para conseguir entornos aislados de trabajo dentro de una computadora.
No tiene nada que ver con las MV.

Dentro de un contenedor no es posible tener un SO propio.

Un contenedor es un entorno aislado dentro de un SO con kernel LINUX donde correr procesos.