# Instación en GNU/Linux

Ver video tutorial en YouTube.

## Pasos previos a la instalación

### 1. Descargar de Manim 

* Ir al [repositorio oficial](https://github.com/3b1b/manim), click en el recuadro verde "Clone or download" y luego click en "Download ZIP".

<p align="center"><img src ="/English/0_instalation/gnuLinux/gifs/manimDescarga.png" /></p>

* Descomprimir carpeta manim-master preferentemente en el directorio principal.


## Instalación usando la terminal:
Abrir terminal y copiar los siguientes comandos.
### Instalación de LaTeX:

```sh
$ sudo apt-get install texlive-full
```

### Instalación de pip3:

```sh
$ mkdir pip
$ cd pip
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
$ python3 get-pip.py
```

### Instalación de ffmpeg:

```sh
$ sudo apt-get install ffmpeg
```

### Instalación de sox:

```sh
$ sudo apt-get install sox
```

### Instalación de paqueterías previas para instalar pycairo:

```sh
$ sudo apt-get install libcairo2-dev libjpeg-dev libgif-dev python3-dev libffi-dev
$ python3 -m pip install pyreadline
$ python3 -m pip install pydub
```

### Instalación de pycairo:

```sh
$ python3 -m pip install pycairo
```

## Instalación de requerimientos:
Moverse a la carpeta de manim:

```sh
~/manim-master$
```

Luego escribir:

```sh
$ python3 -m pip install -r requirements.txt
```

# Ejecución de Manim

Para ejecutar Manim por primera vez hay que ir a la carpeta de manim y escribir:

```sh
$ python3 -m manim example_scenes.py SquareToCircle -pl
```

Ese código debería generar algo como esto:

<p align="center"><img src ="/English/0_instalation/gnuLinux/gifs/compilacion.gif" /></p>

# Almacenamiento
Al ejecutar manim por primera vez se crearà una carpeta llamada "media" y un archvio de texto "media_dir.txt". En la carpeta "media" se almacenaràn los videos por defecto, si deseas modificar la carpeta donde se exporten los videos tienes que escribir el directorio completo en el archivo "media_dir.txt".
