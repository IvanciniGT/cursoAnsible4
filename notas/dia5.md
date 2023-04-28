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