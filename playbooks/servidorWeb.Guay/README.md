# Super playbook instalador y configurador de nginx

## tags:

| tag            | description                           | Siempre | 
| -------------- | ------------------------------------- | :-----: | 
| configuracion  |                                       | NO      |
| despliegue     |                                       | NO      |
| instalacion    |                                       | NO      |
| pruebas        |                                       | NO      |
| monitorizacion |                                       | SI      |
| notificacion   |                                       | NO      |


## Variables comunes:

```yaml
web:
    repo:       https://github.com/IvanciniGT/webEjemploAnsible
    dominio:    mipaginita.com
    puerto:     8080
    carpeta:    /home/ubuntu/environment/datos/web
    tests:
              - end_point:      /index.html
                status_code:    200
                respuesta:      Soy el fichero de la WEB
                
              - end_point:      /
                status_code:    200
                respuesta:      version
```

## Variables menos comunes:

```yaml
email:          ivan.osuna.ayuste@gmail.com
nginx:
    version:    1.14*
```

## Ejemplo de uso

```sh
ansible-playbook playbook.yaml -e @default/app1.yaml
```

## Cualquier cosa:

A: <ivan.osuna.ayuste@gmail.com>... con cafecito de por medio ;)