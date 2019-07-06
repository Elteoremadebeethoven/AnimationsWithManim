<p align="center"><img src ="/_title.gif" /></p>

## Contents (updating)
### [Tutorial files](https://drive.google.com/open?id=10LYJVJsvkcl5a7q_S-ZlSxI7hEBepw3P)
### This tutorial is based on the manim version of [3 february of 2019](https://github.com/3b1b/manim/tree/3b088b12843b7a4459fe71eba96b70edafb7aa78) 

0. Installation on [Windows](https://www.youtube.com/watch?v=ZltiKHFWmv8), [GNU/Linux](https://www.youtube.com/watch?v=z_WJaHYH66M) and [Mac](https://www.youtube.com/watch?v=uZj_GQc6pN4).
1. [Text format](https://github.com/Elteoremadebeethoven/AnimationsWithManim/blob/master/English/1_text_formats/scenes.md)/[Part 1 - Youtube](https://www.youtube.com/watch?v=yI2YJff9SgI)/[Part 2 - YouTube](https://www.youtube.com/watch?v=Km09KYWb9ag)/[Part 3 - YouTube](https://www.youtube.com/watch?v=gIvQsqXy5os)
2. Tex formulas/[YouTube](https://www.youtube.com/watch?v=DGSj7weT-y8)
3. [Text like arrays](https://github.com/Elteoremadebeethoven/AnimationsWithManim/blob/master/English/3_text_like_arrays/scenes.md)/[YouTube](https://www.youtube.com/watch?v=QEdVn8socC8)
4. [Transformations](https://github.com/Elteoremadebeethoven/AnimationsWithManim/blob/master/English/4_transform/scenes.md)/[Part 1 - YouTube](https://www.youtube.com/watch?v=HKPm8FZYaqI)/[Part 2 - YouTube](https://www.youtube.com/watch?v=qfifBmYTEfA)
5. [Visual tools](https://github.com/Elteoremadebeethoven/AnimationsWithManim/blob/master/English/5_visual_tools/scenes.md)/[YouTube](false_link)
6. [Introduction in 2D plot](https://github.com/Elteoremadebeethoven/AnimationsWithManim/blob/master/English/6a_plots_2D/scenes.md)/YouTube
7. [Introduction in 3D plot](https://github.com/Elteoremadebeethoven/AnimationsWithManim/blob/master/English/6b_plots_3D/scenes.md)/YouTube
8. Add audio/YouTube
9. Add svg images/YouTube
10. First project/YouTube

Extras:
* [Leave progress bars by default.](https://www.youtube.com/watch?v=K8dVFqXR2JM)
* [Rendering settings.](https://www.youtube.com/watch?v=d_2V5mC2hx0)
* Modify the directory "media".

## What is Manim?
[Manim](https://github.com/3b1b/manim) is a free tool for Python created by [Grant Sanderson](http://www.3blue1brown.com/) ([twitter](https://twitter.com/3blue1brown?lang=es)), matematician from Stantford and owner of the channel of YouTube [3Blue1Brown](https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw). It is specialized in scientific subjects, mainly mathematical, so it is based on LaTeX commands (mainly in TeX).

## What is LaTeX?
LaTeX is a processor of specialized texts in the scientific field, however, manim only uses TeX commands (with some exceptions), which refers to the writing of formulas. An example of the code in TeX is:
```latex
\frac{d}{dx}f(x)=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}.
```
If I built this command TeX return:
<p align="center"><img src ="https://raw.githubusercontent.com/Elteoremadebeethoven/AnimacionesConManim/master/TeX.png" /></p>

## Who is tutorials for?
This course is mainly aimed at teachers who want to explain a didactic and graphic form a mathematical development or the resolution of especially complex problems. The course extends to anyone who wants to explain a scientific topic in a original way.

## I need to know Python 3 and LaTeX to take this tutorials?
No, is not necesary know smething of programming (although it is preferable for faster learning). In addition to learning Python 3, teX knowledge is required to write the formulas. Likewise will be mencion tools such as [Pencil chromestore](http://s1.daumcdn.net/editor/fp/service_nc/pencil/Pencil_chromestore.html), [Codecogs](https://www.codecogs.com/latex/eqneditor.php), [Rinconmatematico](http://rinconmatematico.com/mathjax/), [latex4technics](https://www.latex4technics.com/), [sciweavers](http://www.sciweavers.org/free-online-latex-equation-editor) in other pages to learn and write formulas in TeX.

## I need a modern PC to run Manim?
No, with 512 MB of RAM and an Intel Core Duo processor (or similar) is more than enough, the difference is the compile time (the fewer resources the longer it will take more time the render).

## What advantages does Manim offer with respect to other animation tools?
### Advantages:
* It is free and legal.
* Works on Windows, GNU/Linux (any distribution) and Mac perfectly.
* Can be used in old computers.
* Being open source is completely customizable to the user's taste.
* It is constantly improving.
* The video files are very high quality and light.
* The formulas are created using TeX commands, so they are of professional quality.
* In the case of not having programming knowledge, it is a good tool to start learning Python and LaTeX.
### Disadvantages:
* If you do not have the LaTeX package (complete) installed, it will occupy more than 4 GB of space on your computer.
* A graphic interface is not used to perform the animations, everything is based on the Python 3 and TeX commands. The example of the classic Hello world! would be
```python
from manimlib.imports import *

class HelloWorld(Scene):
    def construct(self):
        helloWorld = TextMobject("Hello world!")
        self.play(Write(helloWorld))
        self.wait()
```
<p align="center"><img src ="https://raw.githubusercontent.com/Elteoremadebeethoven/AnimacionesConManim/master/HelloWorld.gif" /></p>

## Requirements
* Python 3.7
* pip (to install plug ins of python)
* Cairo
* FFmpeg
* LaTeX (complete)
* Sox
* A few plug ins on the list requirements.txt


