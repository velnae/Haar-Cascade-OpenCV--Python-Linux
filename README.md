<p align="center">
  <a href="https://codely.com">
    <img alt="Codely logo" src="./banner.png" width="300px" height="auto"/>
  </a>
</p>

<h1 align="center">
 📸🌊 Haar Cascade - OpenCV en Linux - Python
</h1>

En este repositorio se encuentra el codigo y los pasos necesario para generar tu archivo `cascade.xml` o entrenar el reconocimiento de imagenes con la técnica **Haar Cascade** a travez de la linea de comandos en linux, y luego hacer la prueba de entrenamiento con Python, una camara y el obejto en movimiento, en este caso se uso una caja de fosforo 😅

<p align="center">
<img alt="Codely logo" src="./preview.gif" width="300px" height="auto"/>
</p>

Para poder entrenar por **Haar Cascade** con **OpenCV** necsitaremos hacer los siguientes pasos:  

# Table of Contents

- [Instalar OpenCV en Linux](#instalar-opencv-en-linux)
- [Imagenes positivas y negativas](#Imagenes-positivas-y-negativas)


## Instalar OpenCV en Linux

Para instalar en linux. para distrubuciones basadas en debian se puede hacer de 2 maneras, instalar desde e los repositorios la herramienta ya compilada o compilarla desde el repositorio github de OpenCV

**Para compilar e instalar desde el repositorio de github correr los comandos:**

- Aseguramos de actualizar nuestro equipo

  ```sh
  sudo apt-get update
  sudo apt-get upgrade
  ```
- Descargamos las herramientas de compilacion necesarias:

  ```sh
  # Compiler: 
  sudo apt-get install build-essential
  # Libraries: 
  sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
  # Python
  Python bindings and such: sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
  ```
  luego seguiremos los pasos comunes para instalar con make en linux como se muestra en el siguiente enlace

  [Compilar OpenCv - Make](https://gist.github.com/Mahedi-61/804a663b449e4cdb31b5fea96bb9d561)

**Para instalar desde los repos del OS Linux correr los comandos:**
- Basta ejecutar el siguiente comando
```sh
sudo apt-get install libopencv-dev
```

- Luego tener instalado obviamente Python
```sh
# Python
  Python bindings and such: sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
```

## Imagenes positivas y negativas