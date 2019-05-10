# Instalation on GNU/Linux

Link to video tutorial.


## Instalation with the terminal:
Open a terminal an run the follow commands:

### Install de LaTeX:
Debian distributions:
```sh
$ sudo apt-get install texlive-full
```
Arch distributions:
```sh
$ sudo pacman -S texlive-most
```
Fedora distributions:
```sh
$ yum -y install texlive-collection-latexextra
```

### Install python3.7
Depends of your distribution

### Install pip:

```sh
$ mkdir pip
$ cd pip
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
$ python3 get-pip.py
```

### Install ffmpeg:

```sh
$ sudo apt-get install ffmpeg
```

### Install sox:

```sh
$ sudo apt-get install sox
```

### Install pycairo dependences (only for Debian distributions):

```sh
$ sudo apt-get install libcairo2-dev libjpeg-dev libgif-dev python3-dev libffi-dev
```

### Install pycairo, pyreadline, pydub:

```sh
$ python3 -m pip install pycairo
$ python3 -m pip install pyreadline
$ python3 -m pip install pydub
```

### Download Manim from [actual version](https://github.com/3b1b/manim), or [3/Feb/2019 version](https://github.com/3b1b/manim/tree/3b088b12843b7a4459fe71eba96b70edafb7aa78).

<p align="center"><img src ="/English/0_instalation/gnuLinux/gifs/manimDescarga.png" /></p>

Unzip the file into a directory that does not have spaces

## Install list requirements.txt:
Move the terminal to the manim-master directory:

```sh
~/manim-master$
```

Then run:

```sh
$ python3 -m pip install -r requirements.txt
```

# Run Manim

Run this command in manim-master directory:

```sh
$ python3 -m manim example_scenes.py SquareToCircle -pl
```

