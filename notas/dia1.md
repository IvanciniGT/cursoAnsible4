# Ansible

Ansible es no una herramienta, sino TODA UNA FAMILIA de productos de software que nos ayudan con AUTOMATIZACIONES.

Quién está detrás? Redhat Inc.

## Redhat Inc.

Es la empresa que nos demostró (al mundo) que el mundo opensource es rentable.

    * Opensource: Código abierto
        El código de un producto está disponible para que el mundo lo consulte.
        Dependiendo de la licencia del software podrá o no:
        - Cambiarlo,
        - Distribuirlo
        - ...
        Opensource NO SIGNIFICA GRATUITO !!!! 
        Gratuito en el mundo del software lo llamamos Freeware
        Un software gratuito y opensource es lo que llamamos Free Software!
    
La gente de Redhat sigue una política muy peculiar que aplica a todos sus productos:
- Todos son Opensource
- Pero Redhat, en sus productos ofrecidos a empresas requiere de un pago... 
  - No es por licencia
  - Cobra una subscripción: Básicamente lo que pago es por SOPORTE !

De todo producto, Redhat ofrece 2 versiones (distribuciones), una GRATUITA y otra de pago (mediante ese modelo de subscripción)

| PAGO                              | Gratuito                                    |
| --------------------------------- | ------------------------------------------- |
| RHEL                              | Fedora (proyecto UPSTREAM)                  |
| JBOSS                             | Wildfly                                     |
| Openshift Container Platform      | OKD                                         |
| Ansible engine                    | Ansible project                             |
| Ansible Tower                     | AWX                                         |
| Ansible Galaxy                    | Ansible Galaxy                              |

## Productos dentro del acosistema Ansible

### Ansible engine / Ansible project

Herramienta de software que nos ofrece:
- Un lenguaje (un esquema YAML) para crear scripts de AUTOMATIZACIÓN            -> PLAYBOOKS
- Varias sintaxis (3) para definit catalogos de entornos remotos                -> INVENTARIOS
  sobre los que ejecutar esos scripts
- Una serie de comandos, con los que poder aplicar operaciones sobre esos playbooks x inventarios

### Ansible Tower / AWX

Herramienta que se instala en un servidor y que nos ofrece:
- Un entorno gráfico para gestionar inventarios/playbooks
- Orquestación de playbooks
- Planificar ejecuciones de playbooks x inventarios
- Monitorizar ejecuciones x inventarios
- Gestión de usuario / Asignación de recursos-operaciones sobre los mismos
- Repositorio centralizado de CREDENCIALES
- API REST para gestionar/ejecutar playbooks remotamente (integración con otros sistemas)

### Ansible Galaxy

??? JUEVES


# Ansible engine / Ansible project

## Para que usamos Ansible engine/project

Montar AUTOMATIZACIONES, como:
- Instalar servicios
- Monitorizarlo
- Actualizarlo
- Modificar una BBDD
- Atacar un API Rest
- Enviar correo
 
### Automatizaciones

Contruir un programa que haga lo que a mi interesa... que antes hacía manualmente.

#### Tipos de software

- Sistema Operativo
- Driver
- Librería de operaciones
- Aplicación
- Demonio
- Servicio
- Comando
- Script        >> ESTO ES LO QUE VAMOS A MONTAR CON ANSIBLE!!!! > PLAY

#### Y por qué Ansible para este trabajo?

No tenemos ya un montón de lenguajes, que llevan decadas en el mercado, que tienen MILES de librerías para montar SCRIPTS?
- sh / bash
- ps1
- py

Por qué Ansible? 
Por la forma en la que está definido su lenguaje... o mejor dicho, por la forma en la que nos expresamos al usar su lenguaje.

## Un lenguaje (un esquema YAML) para crear scripts de AUTOMATIZACIÓN            -> PLAYBOOKS

### Formas de usar un lenguaje / Formas de expresar una idea / concepto en un lenguaje

> Ejemplo 1, usando un lenguaje al que estamos bastante acostumbrados: ESPAÑOL


    FELIPE, debajo de la ventana hay una silla          ENUNCIATIVA AFIRMATIVA
    FELIPE, hay una silla debajo de la ventana?         INTERROGATIVA
    FELIPE, quiero una silla debajo de la ventana       DESIDERATIVA
    FELIPE, pon una silla debajo de la ventana!         IMPERATIVA
    FELIPE, debajo de la ventana ha de haber una silla  DECLARATIVA

La mayor parte de lenguajes de scripting (bash, ps1, py...) usan paradigmas IMPERATIVOS.
Estamos muy acostumbrados al paradigma IMPERATIVO... De hecho nos gusta... ser mandones.
A pesar de ello, odiamos los lenguajes IMPERATIVOS!!!! son horribles de usar, incomodísimos!

Y por ello, han salido al mercado un montón de herramientas que usan otra forma de expresar conceptos: DECLARATIVA !
Como Ansible, que nos ofrece un lenguaje DECLARATIVO !!!
Otras herramienats que usan lenguajes declarativos serían: Kubernetes, terraform...

#### Qué problema le vemos a los lenguajes imperativos?

El problema principal es que no se centran el lo que quiero conseguir, sino en el COMO CONSEGUIRLO...

    FELIPE, centrate !!!!
    SI NO HAY UNA SILLA DEBAJO DE LA VENTANA: 
        FELIPE, SI hay algo debajo de la ventana:           IF: Condicional
            FELIPE, QUITALO !!!!!
        FELIPE, SI NO HAY SILLAS:
            VETE AL IKEA y compra una silla
    FELIPE, pon una silla debajo de la ventana!         IMPERATIVA

    Felipe... bien mandado se pone manos a la obra... pero....
    hay un mueble debajo de la ventana... a lo que FELIPE RESPONDE: ERROR, EXCEPTION, 404 
    Pero... no hay sillas, para poner....

** NOTA:
    En inglés, para contuir una frase en imperativo, ponemos solo el verbo en infinitivo y algo más caracteriza al imperativo?
    No se escribe el sujeto

No me estoy centrando en el objetivo: Que debajo de la ventana tiene que haber una silla.

#### Vamos al lenguaje declarativo:

En el lenguaje declarativo, me centro en el objetivo, en lo que quiero... y noo en cómo conseguirlo.

    FELIPE, debajo de la ventana ha de haber una silla  DECLARATIVA

Le estoy dando instrucciones a FELIPE acerca de COMO conseguir lo que quiero conseguir? NO
Quién debe ahora, diseñar el flujo de tareas necesario para conseguir lo que yo quiero conseguir? En quién lo he delegado?
En FELIPE!

#### Consideraciones

No podemos traducir sin más un script escrito en lenguaje IMPERATIVO a en script escrito en lenguaje DECLARATIVO.
Esto no va de hacer lo que haciamos antes en python o en la bash, o en la ps1, en ANSIBLE. Eso es imposible!
Se trata de montar un script en lenguaje DECLARATIVO que llegue al mismo sitio a donde llegaba el script IMPERATIVO.

### Idempotencia

Da igual el estado inicial de un sistema, al aplicarle un script, siempre voy a conseguir el mismo estado final!
El lenguaje declarativo, per se, nos lleva al camnio de la idempotencia, simplemente por la forma en la que nos expresamos.

Que nadie se equivoque... Ansible genera scripts IDEMPOTENTES? NO
Ansible (algunos de sus componentes, NO TODOS) me facilitan la labor de montar scripts IDEMPOTENTES... 

pero es MI RESPONSABILIDAD el hacerlo.... Y QUIERO HACERLO !
Y esto es algo que cuando montaba scripts imperativos (bash, py...) normalmente NI ME PLANTEABA!

Pero... por qué me tomo tan en serio la idenpotencia? Eso es algo de ANSIBLE? NO
Terraform, también me permite montar scripts idempotentes, y Kubernetes....

Cuando monto un script de Ansible, no quiero un script de:
- Instalación de un sistema (que es a lo que habitualmente tendemos)
- Monitorización de un sistema
- Actualización de un sistema

De hecho esos scripts ya los venimos resolviendo desde hace AÑOS con herramientas como bash, py...
Ahora lo que quiero es UN script que me haga DE TODO !!!!!
Que no le importa cómo está un entorno!

ESTA ES LA GRACIA DE ANSIBLE !

## Arquitectura / Componentes

Ansible, va a estar instalado en una máquina. Esa máquina la denominamos NODO CONTROLADOR

### Nodo controlador

Un entorno cualquiera donde tenemos instalado ansible y vamos a ejecutar unos playbooks.
Ese nodo controlador debe ser una máquina LINUX !

Es posible instalar ANSIBLE en WINDOWS? NO !!!!!
En esa máquina necesitaré además tener instalado PYTHON !
Lo cual no es un problema... casi toda máquina linux, por no decir TODA lo llevan de serie.

### Nodo gestionado / remoto

Es un entorno accesible por red desde el nodo controlador, en el que se irán ejecutando tareas.
Esa máquina puede ser Windows, Linux, MacOS... lo que sea, siempre que también tenga PYTHON instalado...
y tenga una forma YA CONFIGURADA de antemano para acceder a ella:
- ssh
- winrm
- ...

### INVENTARIO

Catalogo de nodos gestionados/remotos.
Dentro de ese inventario (que será un fichero o una carpeta), definiremos:
- Cada nodo
- La forma en la que vamos a contar con él desde el controlador
- Datos adicionales que puedan ser relevantes para mis scripts de automatización

### PLAY

Es un script de automatización. En ese script vamos a definir:
- Los entornos sobre los que voy a ejecutar algunas o todas las tareas que defino en el play
- tareas que quiero ejecutar
- parametrización de esas tareas

Los plays los agrupamos en unos ficheros/carpetas llamados PLAYBOOKS!.

Tanto playbooks como los inventarios finalmente acabará almacendos en:
En un repositorio de un sistema de control de código fuente, tipo GIT

### MODULOS

Un modulo de Ansible es: UN PROGRAMA que se encarga de realizar un tipo de tarea muy concreta.
Dentro de ese módulo habrá mucho código... normalmente escrito en python y código imperativo.
La gracia es que nosotros nos comunicaremos con el módulo mediante lenguaje DECLARATIVO !
La mayor parte de los módulos soportan el concepto de IDEMPOTENCIA.

> Ejemplo: En tal máquina debe existir un usuario llamado "ivan", cuyo home sea "/home/ivancini", y cuya contraseña sea "Pa$$w0rd"


    Eso es lenguaje? DECLARATIVO
    Ansible tendrá un módulo para ese trabajo.
    A ese módulo, yo le hago llegar esa información.
    El módulo me debe garantizar que da igual si el usuario ya existe con esos datos, o con otros datos, o no existe...
        La máquina va a quedar como yo quiero!
    
    Ansible viene con MILES DE MODULOS. No es objetivo del curso aprender TODOS LOS MODULOS DE ANSIBLE.
    Los módulos de Ansible vienen muy bien documentados... y me pasaré el día en esa documentación.
---

---

# DEV--->OPS

Cultura, filosofía, un movimiento en pro de la AUTOMATIZACION... Y qué quiero automatizar? TODO !!!! 
TODO Lo que está entre el desarrollo y la operación de una sistema

Antiguamente los proyecto del mundo IT se regían por metodologías en CASCADA!

Hoy en día han sido reemplazadas por Metodologías agiles. 
Esas metodologías ágiles, lo que nos invitan es a ENTREGAR UN SISTEMA DE FORMA INCREMENTAL !

El día 15 de un proyecto hago paso a producción! Una versión 100% funcional a las 2 semanas... quizás solo el 5% de la funcionalidad
El día 30 hago otra entrega     + 10% 
El día 45 otra entrega           + 5%

Como os podeis imaginar esto resolvió muchos problemas... pero poca gente dice que esto vino con sus propios problemas !!!!
- Cúantas veces instalaba un software en un proyecto hace 20 años?  1, al acabar el proyecto
- Y ahora? Cada 15 días!

- Cúantas veces probaba un software en un proyecto hace 20 años?  1, al acabar el proyecto, antes de ponerlo en prod.
- Y ahora? Cada 15 días!

Y de donde ostias saco la pasta para pagar todo eso? DE NINGUN SITIO !!! NO LA HAY !!!!!
Esto solo tiene una solución: AUTOMATIZAR !

Devops y las metodologías ágiles son cosas diferentes... 
pero es imposible adoptar una metodología AGIL sin abrazar una cultura DEVOPS !... NO HAY PASTA PARA ELLO !!!!

Igual que las metodologías ágiles son el reemplazo de las metodologías en cascada
DEVOPS es el reemplazo de lo que antes llamábamos SOFTWARE DEVELOPMENT MANAGEMENT CYCLE

Qué quiero automatizar? TODO LO AUTOMATIZABLE entre esos dos ombligos, el de desarrollo y el de operaciones.

                        AUTOMATIZABLE?
PLAN                        Poco
CODE                        Me temo que cada día más (chatgpt, copilot)
BUILD                       Totalmente: 
                                JAVA: maven, gradle
                                C#:   dotnet msbuild
                                py:   poetry, pip
                                Ansible: galaxy !!!
TEST                        
    Diseño                  Aún no
    Ejecución               Casi todo !!!
                                jmeter, selenium , appium, soapui, postman, cypress, ...
                            Las pruebas las hacemos en un ENTORNO DE PRUEBAS.
                            Me fío del entorno de pruebas? Me temo que tampoco !
                            Y hoy en día la tendencia es a usar entornos de usar y tirar!!! -> CONTENEDORES !
                            Y la creación de esos entornos... la automatizamos? TOTALMENTE
                                terraform: Adquirir infraestructura < - cloud
                                vagrant: Maquinas virtuales
                                Provisionadores: Ansible, puppet, chef, salt

> Si automatizo todo el trabajo hasta aquí?     INTEGRACION CONTINUA ! 

RELEASE                     TAMBIEN

> Si automatizo todo el trabajo hasta aquí?     ENTREGA CONTINUA ! CONTINUOUS DELIVERY

DEPLOY                      TAMBIEN
                                terraform: Adquirir infraestructura < - cloud
                                vagrant: Maquinas virtuales
                                Provisionadores: Ansible, puppet, chef, salt
                                Kubernetes....

> Si automatizo todo el trabajo hasta aquí?     DESPLIEGUE CONTINUO ! CONTINUOUS DEPLOYMENT
                                
OPERATION                   TOTALMENTE
                                clouds + kubernetes
MONITOR                     TOTALMENTE 

Hay una cosa más que automatizar: LA EJECUCION / ORQUESTACION DE ESAS AUTOMATIZACIONES 
Eso lo hacen los servidores de AUTOMATIZACION: Jenkins, TeamCity, Bamboo, TravisCI...
                                               TOWER (pero solo vale para automatizar la ejecución y orquestación de playbooks de ansible)

## Dentro de este nuevo paradigma... donde quiero automatiar TODO lo automatizable....
## cómo entra en concepto de IDEMPOTENCIA 

Imaginad un script, que diga:
Necesito en la máquina X:
- Tales usuarios
- Tales programas instalados
- Tales programas corriendo

Para qué me sirve ese script? 
- Me sirve para hacer una instalación desde CERO ? SI
- Me sirve para hacer una actualización de un sistema? SI
- Me sirve para hacer una monitorización de un sistema? SI




# Entornos:

- Desarrollo
- Pruebas, Testing Q&A, Integración!
- Producción
 
---

# Estados en los que puede acabar una tarea de un play:

- ok                Que no ha habido problemas, pero la tarea no ha provoca cambios en la máquina... o eso parece!!!!
- changed           Que no ha habido problemas, pero que ha provocado cambios en la máquina (en el entorno controlado)
- failed            Que la tera no se ha podído conseguir /ejecutar
 

# Apparmor

SELinux: Security Enhanced for Linux.
         Eso es un programa que se monta como parte del kernel de Linux 
         en sistema operativos REDHAT para ampliar las funciones de seguridad del SO

AppArmor es un equivalente en SO Ubuntu