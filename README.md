# Computacion Cuantica

## Construir Imagen
En la terminal, dentro de la carpeta qiskit-docker:
   docker build -t qiskit-demo 

## Ejecutar el contenedor y sacar las imagenes
En Linux/Mac:
docker run --rm -v "$(pwd)":/app qiskit-demo

En PowerShell (Windows):
docker run --rm -v ${PWD}:/app qiskit-demo

# SIGEC
