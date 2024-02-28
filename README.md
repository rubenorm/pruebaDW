# Gestión de vehículos

API e interfaz para la gestión y visualización de información de vehículos

## Instalación

El entorno se desarrolló en Ubuntu 22.04.

Usando Python v3.10.12 y Flask v3.0.2

Usa el gestor de paquetes [pip](https://pip.pypa.io/en/stable/) para instalar las bibliotecas de Python.

Se crea una carpeta para el proyecto.
```bash
mkdir Proyecto
cd Proyecto
```
Se crea un entorno para el proyecto.
```bash
python3 -m venv venv
source venv/bin/activate
```
Se instalan los paquetes necesarios.
```bash
pip3 install Flask
```
Se inicializa la base de datos.
```bash
flask --app flaskr init-db
```




## Ejecución

```bash
flask --app flaskr run --debug
```


## Pruebas

Los usuarios de prueba y sus contraseñas son:
Ruben -> abc123
Jose -> bcd456
Juan -> efg789

