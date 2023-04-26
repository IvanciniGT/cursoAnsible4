# Quiero un servidor web (nginx), con un sitio web en un entorno (linux-Ubuntu).
# El sitio web lo tengo en un repo de git!

    tasks:
        -   name:       Asegurar que realmente estoy en una máquina UBUNTU                  GUAY
        -   name:       Asegurar que git queda instalado en el entorno                      GUAY
        -   name:       Asegurar que NGINX queda instalado en el entorno                    GUAY
        -   name:       Asegurar que nginx tiene la configuración que necesito              CAMBIO


        -   name:       Asegurar que la carpeta para alojar la web está creada              GUAY
                            # Lenguaje imperativo... pero este lenguaje ... y este código lo aporta? EL MODULO !
                            #
                            #   FELIPE !!! SI la carpeta no está creada
                            #                   CREA LA CARPETA 
                            #
        -   name:       Asegurar que en la carpeta de la web tengo la última versión        GUAY 
                        que hay en el repo de git  
        -   name:       Asegurar que el nginx queda arrancado                               GUAY = CAGADA !!!!!
        -   name:       Si ha habido un cambio en alguna tarea anterior
                            Asegurar que el nginx es reiniciado
        -   name:       Asegurar que la web está en funcionamiento                          RUINA ! OSTION PADRE !!!!
            tags: 
                - pruebas

# ESTO ES UNA RUINA DE UN CALIBRE INIMAGINABLE !!!!

# Esto es un PLAYBOOK de ANSIBLE ? NO... ni parecido a un PLAYBOOK conceptualmente
# Que hemos hecho realmente aquí?  UN SCRIPT DE INSTALACION DE UN ENTORNO !
# Presuponiendo que el entorno está limpio de polvo y paja

# PUNTO 1: IDEMPOTENCIA !
# PUNTO 2: Qué tipo de lenguaje estamos usando? IMPERATIVO POR UN TUBO !!!!!! = RUINA !

# Lo primero: HAY QUE CAMBIAR EL LENGUAJE ! DESDE YA !

# ME temo que no todo va a ser tan bonito... ni tan declarativo... Y el IMPERATIVO va a seguir por ahí de alguna forma.
---
# ESCENARIO 1: TENGO UNA MAQUINA LIMPIA ! Funciona el PLAYBOOK? Debería... Nos faltan cosas 
---
# ESCENARIO 2: TENGO UNA MAQUINA DONDE TODO ESTA YA PERFECTAMENTE LISTO y CONFIGURADO ! Qué hace el playbook? 
# Simplemente asegurar ue todo está OK... no debería hacer ningún cambio... Todo estaría correcto!
# Qué estamos haciendo al ejecutar el script en este escenario?  Cada 5 mins
#. - Monitorizar
#. - Si algo no va bien... trata de arreglarlo
---
# ESCENARIO 3: TENGO UNA MAQUINA DONDE TODO ESTA YA PERFECTAMENTE LISTO y CONFIGURADO , salvo
# El puerto del nginx... estaba el 81... y ahora quiero configurar el 80
# FUNCIONARIA ?
