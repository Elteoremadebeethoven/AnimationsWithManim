# Instalación en Windows

La instalación en Windows es particularmente elaborada, por lo que recomiendo ver el video tutorial de instalación en YouTube, pero aquí se esbozarán los pasos para la gente que tenga más conocimientos en computación.

En caso de haber concluido todos los pasos y no lograr compilar los archivos es recomendable instalar una versión ligera de GNU/Linux (como [Lubuntu](https://lubuntu.net/downloads/)) en una máquina viritual y realizar el proceso de instalación de [GNU/Linux](https://github.com/Elteoremadebeethoven/AnimacionesConManim/blob/master/Espa%C3%B1ol/0_instalacion/gnuLinux/INSTRUCCIONES.md). La única desventaja será que este proceso necesitará unos 10 GB de espacio en tu disco duro.

[Video](https://www.youtube.com/watch?v=44fthwtnrF0) de como instalar Lubuntu en una máquina virtual usando VirtualBox.

## Instalar editor de texto plano.
Yo recomiendo [Sublime Text](https://www.sublimetext.com/).

## Descargar Manim del [repositorio oficial](https://github.com/3b1b/manim).
Descomprimir el archivo donde el usuario desee (en este ejemplo lo descomprimiré en Documentos).

## Modificar el archivo constants.py
Cambiar el código al archivo constants.py, en la linea que dice:
"Dropbox (3Blue1Brown)/3Blue1Brown Team Folder"
por la dirección de una carpeta dedicada los videos de manim, yo recomiendo la carpeta de videos "Videos" en el directorio principal.

## Instalación de LaTeX
Instalar la versión completa de [MikTeX](https://miktex.org/download).
1. Vas a "Downloads", luego a "All donwloads".
2. Seleccionar "Net Installar" de 32 bits o 64 bits dependiendo de tu PC.
3. Descargar e instalar, es un proceso que puede durar varias horas ([ver video ayuda](https://www.youtube.com/watch?v=yPnfHRE_W_g) del minuto 0:00 hasta el 6:19, lo demás no se necesita).

## Instalar Python 3.
Ir a la página oficial de [Python](https://www.python.org/), luego a Donwloads y descargar alguna versión de Python superior a la 3.6 (recomiendo la versión más reciente), el instalador debe decir "Windows x86-64 executable installer" e instalar.

## Modificar la variable PATH
Añadir a la variable PATH la carpeta donde se instalo Python 3 (ve a Inicio, busca Python 3, dale click derecho a algún archivo y luego click en "Abrir la ubicación del archivo"), además de la subcarpeta "Scripts".

La ubicación por defecto de la instalación suele ser:
```
C:\Users\Pc\AppData\Local\Programs\Python\Python37
```
Y la subcarpeta "Scripts":
```
C:\Users\Pc\AppData\Local\Programs\Python\Python37\Scripts
```

## Instalar [ffmpeg](https://ffmpeg.zeranoe.com/builds/)
Descargar e instalar de manera normal ([video ayuda](https://www.youtube.com/watch?v=X7wLMejOjjM)) y añade la carpeta de instalación a la variable PATH.

## Instalar [sox](https://sourceforge.net/projects/sox/)
Descarga e instala de manera normal y añade la carpeta de instalación a la variable PATH.

## Instalar Pycairo
1. Ir a esta [página](https://www.lfd.uci.edu/~gohlke/pythonlibs/)
2. Buscar pycairo (pulsa F3 y escirbe pycairo para encontrarlo más rápido).
3. Descarga todas las versiones para Python 3 (dependiendo si tu PC es de 64 o 32 bits).
4. Ir a la ubicación de la carpeta de Python 3 y copia la versión más reciente del archivo .whl a la carpeta.
5. Abre la terminal y muevete a la dirección de la carpeta de Python 3.

Ejemplo:
```
cd C:\Users\Pc\AppData\Local\Programs\Python\Python37
```
6. Ingresa el siguiente comando:
```
python -3 -m pip install 
```
Seguido del paquete, por ejemplo:
```
python -3 -m pip install pycairo-pycairo‑1.17.1‑cp37‑cp37m‑win_amd64.whl
```
Si sale el error:
```
Unknown option: -3
usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...
Try `python -h' for more information.
```
Elimina el "-3" y escribe solo:
```
python -m pip install pycairo-pycairo‑1.17.1‑cp37‑cp37m‑win_amd64.whl
```

En caso de que emita un error elimina el archivo de la carpeta de Python 3 y copia una versión anterior a la carpeta y vuelve a intentar compilar el comando anterior (modificando el nombre del paquete).

Realiza esto hasta que alguna de las versiones sea instalada correctamente.

## Instala los requerimientos
Muevete a la carpeta de manim-master que descargaste usando la terminal y ejecuta el comando:
```
python -m pip install -r requirements.txt
```

# Ejecución
En la misma carpeta de manim-master compila por primiera vez un archivo de Manim usando:
```
python extract_scene.py example_scenes.py WriteStuff -l
```
# Almacenamiento
El video se pudo haber guardado ya sea en una subcarpeta de "manim-master" llamada igual al archivo .py que compilaste, es decir

```
manim-master/example_scenes/WriteStuff/420p15
```

O bien en la carpeta que definiste en constants.py en una subcarpeta llamada "animations"

```
Videos/example_scenes/WriteStuff/420p15
```

El 420p15 se refiere a la calidad del video a la que fue exportado. Dependerá de la versión de manim que descargaste el lugar donde se guarde el archivo.
