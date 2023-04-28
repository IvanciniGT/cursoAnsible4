# Procesos a nivel de SO

Al arrancar un proceso, por defecto tiene 3 canales de comunicación establecidos.
A saber:
- 0=Entrada estandar
- 1=Salida estandar
- 2=Salida de error


## ROLES DE ANSIBLE

Un conjunto de código:
    - Tareas
    - Handlers
    - Variables
    - ...
Reutilizables

## Estructura de un role:
    
    knownhosts                  RAIZ DEL ROLE
        ├── README.md           Archivo descriptivo del role, con ejemplos, variables...
        ├── defaults            Variables que deban modificarse por quien use el role... Damos valores por defecto
        │   └── main.yml
        ├── files               Archivos necesarios para ejecutar el role
        ├── handlers            Los handlers de nuestro role
        │   └── main.yml
        ├── meta                Información descriptiva del role, para compartirlo en ANSIBLE GALAXY
        │   └── main.yml
        ├── tasks               Tareas de nuestro role
        │   └── main.yml
        ├── templates           Plantillas JINJA necesarios para ejecutar el role
        ├── tests
        │   ├── inventory       Archivo de inventario sobre elq ue poder hacer la prueba
        │   └── test.yml        Playbook para automatizar la prueba de nuestro role
        └── vars                Variables que no deben tocarse externamente... son internas del role
            └── main.yml
            
            
# Como nos debemos plantear esto en la empresa:

ERROR! the role 'knownhosts' was not found in 
    ESTAS 2 carpetas son relativas al proyecto (al playbook)
    /home/ubuntu/environment/curso/playbooks/servidorWeb.MegaGuay/roles
    /home/ubuntu/environment/curso/playbooks/servidorWeb.MegaGuay
    
    DE ESTAS ME OLVIDO !
    /home/ubuntu/.ansible/roles
    /usr/share/ansible/roles
    /etc/ansible/roles

## Donde va a estar guardado el playbook?

En un repositorio de git

## Donde va a estar guardado el role?

En otro repositorio de git DIFERENTE !!!!

## PERO GIT NOS OFRECE UNA FUNCIONALIDAD MUY CHULA !

Submodulos de git!

Un proyecto de git, puede tener submodulos

Un submodulo en git, es una carpeta de un proyecto (repositorio) que apunta a otro repositorio

## Sabiendo esto...

En nuestro proyecto con nuestro playbook:

    playbook_nginx
        ├── README.md
        ├── default
        │   └── app1.yaml
        ├── playbook.yaml
        ├── resultado.json
        ├── roles (1)
        │   └── knownhosts -> Apunta a un repo de git
        ├── tasks
        │   ├── asegurar_entorno.yaml
        │   ├── distribuciones
        │   │   ├── Fedora
        │   │   │   ├── nginx.yaml
        │   │   │   └── preparar_entorno.yaml
        │   │   └── Ubuntu
        │   │       ├── nginx.yaml
        │   │       └── preparar_entorno.yaml
        │   ├── nginx_y_app.yaml
        │   └── pruebas.yaml
        ├── templates
        │   └── configuracion.nginx.conf
        └── vars
            └── vars.yaml

Nos interesa crear una carpeta llamada ROLES (1).
Dentro de esa carpeta configuro un submodulo de git, que apunte al repo del role.
De forma que cuando descargue el proyecto de git (lo clone) se me desargue el ROLE ... en esa carpeta.
Y al ejecutar el playbook, me encuentra automaticamente el ROLE.
Cualquier cambio de versión en el role, se me actualizaría mediante un git pull en mi proyecto del playbook.

ESTE ES EL CAMINO !!!!

## Git

RAMA: MAIN/MASTER
        ^ Listo para produccion
RAMA: Playbook1
RAMA: Playbook2

Consultar el historial !!!


PLAYBOOKS
    playbook 1  -> REPO 1
    playbook 2  -> REPO 2 
    playbook 3  -> REPO 3

JENKINS o similar
    REPO 1 (playbook1) ---> COMMIT -> RAMA MAIN -> PUSH -> Jenkins en auto lo pase a producción (que se actualice en ansible TOWER en auto)
    
    
# GIT

Es un sistema de control de código fuente: SCM
Sistema de control de versiones: CVS (Control version system)

CVS -> SUBVERSION  (svn) -> git

De qué van estas herramientas?

- A tener almacenadas distintas versiones del código. -> Y para esto no me vale un Sistema de copias de seguridad?
- Identificar cambios en las versiones a nivel de LINEA DE CODIGO EN UN FICHERO DE TEXTO
- Sicronizar el trabajo del equipo de desarrollo
- Uso de RAMAS !

Una RAMA en un SCM es una linea de evolución paralela en el tiempo de un proyecto

PROYECTO ---> V1.0.0 ---> V1.1.0
                                ---> V1.1.1
                                ---> V2.0.0

### COMMIT

En GIT un COMMIT es una copia completa del proyecto en un INSTANTE DEL TIEMPO. Un backup, UNA FOTO (COMPLETA)

Esos commits se asocian a RAMAS.

En todo proyecto tendremos:
- UNA RAMA PRINCIPAL : main , master.
    En esta rama: NUNCA SE HACE UN COMMIT EN ESTA RAMA
                  LO QUE HAY EN ESTA RAMA SE CONSIDERA LISTO PARA PRODUCCION!
- DESARROLLO: dev, development, desa, desarrollo
- HABITUALMENTE CREAMOS MAS RAMAS:
    - Que cada persona abra su propia rama donde trabajar
    - Para cada funcionalidad abro una rama
    - Hibrida

# FUSION DE CAMBIOS

Consiste en tomar 2 commits (2 fotos del proyecto), determinar que hay de diferencia entre ellas, y generar una foto nueva con
una versión que incluya los cambios que se han realizado en una rama y en otra.

Hay distintas estrategias para hacer fusiones de cambios: MERGE, REBASE, CHERRYPICK

# REPO

Es una BBDD, donde se guardan las fotos (commits) del proyecto, asociados a RAMAS.

## Git es un SCM distribuido

No hay un repositorio centralizado de git en un servidor.
Un proyecto almacenado(gestionado) en git es la suma de muchos repositorios que están distribuidos entre multiples máquinas.

                                                main               C3                            C7
                                                desarrollo C1, C2, C3 -> C4 -> C5 -> c5 -> C6 -> C7
                                            REPO proyecto1
                                            |
                                    Servidor que permita alojar REPOS de git (github, gitlab, bitbcket)
                                            |
    ------------------------------------------------------------------------------- Red
     |                                                                          |
     IvanPC                                                                     MenchuPC
      |- HDD                                                                     |- HDD
          |- proyecto1                                                               |- proyecto1
          |     (ficheros)                                                           |      (ficheros)
          |                                                                          |
          |- REPO                                                                    |- REPO
                main                   C3 [v1.0.0]                    C7 [v1.1.0]           main               C3 [v1.0.0]
                                       ^                              ^                     desarrollo C1, C2, C3 -> C4 -> C5
                desarrollo (local)  C1 -> C2 -> C3 ->c4 -> c5. C6 -> C7                     menchu             C3 -> C4 -> C5
                                                             ^
                desarrollo (remoto) C1, C2, C3 -> C4 -> C5
                
    OPERACIONES:
        - COMMIT:   Hacer una foto en una rama del estado del proyecto (ZIP)
        - PUSH:     Subir mi rama local a un remoto (En git podemos tener 20 remotos). Por defecto el nombre que se da al primer remoto es: origin
        - MERGE/REBASE: Operaciones de fusion de cambios
        - CLONE:    Descargar desde 0 un REPO de git a un local
        - FETCH:    Descargar una/varias ramas de un remoto a un repo ya existente en local
        - PULL:     FETCH + FUSION DE CAMBIOS (MERGE, REBASE)

### Ansible Tower / AWX

Herramienta que se instala en un servidor y que nos ofrece:
- Un entorno gráfico para gestionar inventarios/playbooks
- Orquestación de playbooks
- Planificar ejecuciones de playbooks x inventarios
- Monitorizar ejecuciones x inventarios
- Gestión de usuario / Asignación de recursos-operaciones sobre los mismos
- Repositorio centralizado de CREDENCIALES
- API REST para gestionar/ejecutar playbooks remotamente (integración con otros sistemas)
- Multitenant: tenencia multiple: App que con 1 unica instalacion permite dar servicio a distintos clientes... 
- Manteniendo BBDD separadas para ellos, y acceso restringigo a los recursos