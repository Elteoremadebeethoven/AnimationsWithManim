# Instalation on GNU/Linux

Link to [video tutorial](https://www.youtube.com/watch?v=z_WJaHYH66M).


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
# yum -y install texlive-collection-latexextra
```

### Install python3.7
Debian distributions:
```sh
$ sudo apt-get install python3.7-minimal
```

Arch distributions: always is update

Fedora distributions:
```sh
# yum install gcc openssl-devel bzip2-devel libffi-devel
# cd /usr/src
# wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz
# tar xzf Python-3.7.3.tgz
# cd Python-3.7.3
# ./configure --enable-optimizations
# make altinstall
# rm /usr/src/Python-3.7.3.tgz
```

### Install pip:
All distributions:
```sh
$ mkdir pip
$ cd pip
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
$ python3.7 get-pip.py
```

### Install ffmpeg:
Debian
```sh
$ sudo apt-get install ffmpeg
```
Arch-Linux:
```sh
$ sudo pacman -S ffmpeg
```
Fedora:
```sh
$ sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
$ sudo dnf install https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
$ sudo dnf install ffmpeg ffmpeg-devel
```


### Install sox:
Debian
```sh
$ sudo apt-get install sox
```
Arch-Linux (with AUR):
```sh
$ aurman -S sox
```
Fedora:
Download it from: https://pkgs.org/download/sox

### Install pycairo dependences (only for Debian distributions):
Only for Debian distros:
```sh
$ sudo apt-get install libcairo2-dev libjpeg-dev libgif-dev python3-dev libffi-dev
```

### Install pyreadline, pydub:
All distributions:
```sh
$ python3.7 -m pip install pyreadline
$ python3.7 -m pip install pydub
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
$ python3.7 -m pip install -r requirements.txt
```

# Run Manim

Run this command in manim-master directory:

```sh
$ python3.7 -m manim example_scenes.py SquareToCircle -pl
```

