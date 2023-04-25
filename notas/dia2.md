# Dentro del ecosistema Ansible

## Ansible engine / project

Quien nos ayuda a escribir PLAYBOOKS e INVENTARIOS y ejecutarlos desde un NODO CONTROLADOR

## Ansible Tower / AWX

Gestiona PLAYBOOKS e INVENTARIO con un entorno gráfico
Gestión de usuarios
Gestión centralizada de CREDENCIALES
Orquestación de PLAYBOOKS
API REST 
...

## Ansible Galaxy

???
Servicio web que ofrece Redhat

---

# PLAYBOOKs

Esos playbooks los escribíamos en ficheros YAML, con un esquema propio que ofrece ANSIBLE... que hay que conocer!

```yaml

-   # PLAY 1
    hosts:          localhost   # En que entornos remotos queremos ejecutar tareas del script
    
    gather_facts:   true        # Lo queremos siempre desactivar (menos por ahora en el curso)
    
    tasks:
        -   name:   Tarea 1
            modulo: 
                # configuración del módulo <<<<< Es donde los módulos usan lenguaje declarativo

```

Al ejecutar un playbook se muestra un informe de las tareas que se han ejecutado...

Esas tareas podían acabar en diferentes estados:
- ok            La tarea había ido bien... y no había provocado un cambio en el entorno
- changed       La tarea había ido bien... y SI había provocado un cambio en el entorno
- failed        La tarea NO había ido bien

Según el principio de idempotencia, en la mayor parte de los escenarios....
cuando ejecute la segunda vez un script (PLAYBOOK) cómo debería yo ver todas las tareas? (en que estado)? OK

## IDEMPOTENCIA

Da igual el estado inicial, siempre llego al mismo estado final

## Modulos

Son los programas que se encargan de ejecutar las tareas del playbook.
Esos programas habitualmente están escritos en python (por esto el requisito de tener python instalado en todos sitios)
y usando lenguaje imperativo.
La gracia es que nosotros nos comunicamos con los mñodulos usando lenguaje declarativo.
Los módulos se programan de forma que RESPETEN EL PRINCIPIO DE IDEMPOTENCIA (o se intenta!!!!)

# VARIABLES

Dependiendo del lenguaje / aplicación que manejemos el concepto de variable cambia:

## En python, Java, JS

Una variable es una referencia a un DATO que tengo en memoria.

## En ansible nos lo vamos a plantear de otra forma diferente.

En ansible una variable la entendemos como un CAJON donde meto cosas

## Para qué usamos una variable en un script de Ansible?

- Poder usar un DATO en muchos sitios, sin tener que repetirlo
- Para parametrizar el comportamiento de un playbook
- Para tener una forma de referirme en tiempo de DISEÑO (codificación) a DATOS 
  que no se conocerán hasta tiempo de EJECUCION
    Si está o no instalado nginx en una maquina.... A priori no la conozco... hasta que no conecte con una máquina.
    Pero esa información (SI|NO)  quiero poder referirme a ella en mi playbook... cuando lo diseño.
    Para decir cosas como: SI ESTA INSTALADO Entonces....
                           SI NO ESTA INSTALADO Entonces....

## Donde podemos definir una variable en Ansible...

EN MAS DE 20 sitios diferentes !

# Tipos de DATOS

Qué tipos de datos existen en ANSIBLE?
- números
- textos
- valores lógicos
- listas (ordenadas)
- mapas (desordenados) / diccionario
 

# Plantillas JINJA

## Qué es JINJA?

Es una librería de PYTHON, que nos permite trabajar con PLANTILLAS (TEMPLATES)
Esas plantillas las definimos como un texto en JINJA.
Dentro de las plantillas podemos usar PLACEHOLDERS, encerradas entre dobles llaves, 
podemos escribir código (expresiones) python.
Expresión? 

    Hola, soy una plantilla JINJA!!!!
    Tú como te llamas?
        Yo me llamo: {{ nombre }}

En castellanño, un texto está compuesto de: PARRAFOS
Los PARRAFOS contienen:                     ORACIONES/FRASES/SENTENCIAS
Las sentencias contienen:                   SINTAGMAS

# Estructura de un play
```yaml

- # PLAY
    hosts:
    gather_facts:
    vars:
    
    pre_tasks:
    tasks:
        -   # A nivel de una tarea
            name:
            vars:
            tags:
            <modulo>:
            when:
            changed_when:
            failed_when:
            register:
            notify:
            ignore_errors:
        
        -   block:
            rescue:
            always:
    post_tasks:
    handlers:
        -   
            + listen:
```