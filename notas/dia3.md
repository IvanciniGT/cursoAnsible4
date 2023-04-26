# Pruebas

## Vocabulario

- Error         Los humanos cometemos ERRORES
- Defecto       Un ERROR humano puede acabar introduciendo un DEFECTO(bug) enun SISTEMA/PRODUCTO
- Fallo         Ese ERROR puede llegar a manifestarse como un FALLO

## Para que sirven las pruebas?

- Sirven para asegurar que un requisito se cumple
- Sirven para identificar la mayor cantidad posible de FALLOS
    - Esto lo hacemos usando el PRODUCTO / SISTEMA y viendo si ocurre lo que sea 
      que tiene que tiene que ocurrir o si no. 
        > Del fallo, nos tocará identifiar el defecto (depuración / debugging)
- Sirven para identificar la mayor cantidad posible de DEFECTOS
    - Eso lo hacemos directamente revisando el PRODUCTO / SISTEMA... sin necesidad de usarlo
- En caso de FALLO... la prueba debe aportar LUZ ! ¿Qué ha pasado?
- ...

## Tipos de pruebas

### En base al objeto de prueba

- Pruebas estáticas         NO REQUIEREN PONER EN MARCHA EL SISTEMA: REVISION
- Pruebas dinámicas         SI REQUIEREN PONER EN MARCHA EL SISTEMA
    - Pruebas funcionales   SE CENTRAN EN LA FUNCIONALIDAD
    - Pruebas no funcionales:
        - Rendimiento
        - Carga
        - Estres
        - HA
        - UX
        - Humo

### En base al nivel de la prueba

- Pruebas unitarias             SE CENTRAN en un componente AISLADO del sistema
- Pruebas de integración        SE CENTRAN en la COMUNICACION entre componentes
- Pruebas de sistema            SE CENTRA en el COMPORTAMIENTO del sistema en su conjunto
    - Pruebas de aceptación


sudo apt update -y
sudo apt install software-properties-common -y
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install ansible -y
