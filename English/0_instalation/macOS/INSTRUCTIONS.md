# Instalation on MacOS

Link to video tutorial.

## Install dependences.

### Open a terminal 
Search "terminal" on Spotlight

<p align="center"><img src ="/English/0_instalation/macOS/gifs/terminal.png" /></p>

### Install Homebrew
Copy the code from [Homebrew](https://brew.sh/index_es) and paste it in the terminal

<p align="center"><img src ="/English/0_instalation/macOS/gifs/MacP1.gif" /></p>

### InstallLaTeX (versión completa)
Go to [MacTeX](http://www.tug.org/mactex/), download the .pkg file and install it ([help](https://www.youtube.com/watch?v=5CNmIaRxS20)).

<p align="center"><img src ="/English/0_instalation/macOS/gifs/MacP2.gif" /></p>

### Install Python 3
Go to official web of [Python](https://www.python.org/), and download the 3.7 version ([video ayuda](https://www.youtube.com/watch?v=0hGzGdRQeak)).

<p align="center"><img src ="/English/0_instalation/macOS/gifs/MacP3.gif" /></p>

### Install PIP
Run the follow commands:

```sh
brew install curl
mkdir ManimInstall
cd ManimInstall
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```

### Install FFmpeg, SoX and Cairo.
Run the follow commands:

#### FFmpeg
```sh
brew install ffmpeg
```
#### Sox
```sh
brew install sox
```
#### Paqueterías extra
```sh
brew install cairo --use-clang
```

```sh
brew install py2cairo
```

```sh
brew install pkg-config
```

<p align="center"><img src ="/English/0_instalation/macOS/gifs/MacP5.gif" /></p>

### Download Manim from [actual version](https://github.com/3b1b/manim), or [3/Feb/2019 version](https://github.com/3b1b/manim/tree/3b088b12843b7a4459fe71eba96b70edafb7aa78).

<p align="center"><img src ="/English/0_instalation/macOS/gifs/DescargarManim.gif" /></p>

### Unzip the file into a directory that does not have spaces

<p align="center"><img src ="/English/0_instalation/macOS/gifs/pd.png" /></p>

### Install list requirements.txt
Move the terminal in the manim-master folder and run this:

```sh
python3 -m pip install -r requirements.txt
python3 -m pip install pyreadline
python3 -m pip install pydub
```

<p align="center"><img src ="/English/0_instalation/macOS/gifs/MacP6.gif" /></p>

# Run Manim

With the terminal in manim-master directory run this:

```sh
python3 -m manim example_scenes.py WriteStuff -pl
```

That command have to build the follow video:

<p align="center"><img src ="/English/0_instalation/macOS/gifs/MacP8.gif" /></p>

