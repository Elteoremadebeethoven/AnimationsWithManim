<p align="center"><img src ="/_title.gif" /></p>

## Contents (updating)
0. Installation on [Windows](https://github.com/Elteoremadebeethoven/AnimacionesConManim/blob/master/Espa%C3%B1ol/0_instalacion/windows/INSTRUCCIONES.md), [GNU/Linux](https://github.com/Elteoremadebeethoven/AnimacionesConManim/blob/master/Espa%C3%B1ol/0_instalacion/gnuLinux/INSTRUCCIONES.md) and [Mac](https://github.com/Elteoremadebeethoven/AnimacionesConManim/blob/master/Espa%C3%B1ol/0_instalacion/macOS/INSTRUCCIONES.md).
1. Text format/YouTube/[Scenes](https://github.com/Elteoremadebeethoven/AnimacionesConManim/blob/master/Espa%C3%B1ol/1_formato_textos/ESCENAS.md)
2. Tex formulas/YouTube/[Scenes](https://github.com/Elteoremadebeethoven/AnimacionesConManim/blob/master/Espa%C3%B1ol/extras/formulas_tex/ESCENA.md)
3. Text like arrays and basic animations/YouTube/[Scenes](https://github.com/Elteoremadebeethoven/AnimacionesConManim/blob/master/Espa%C3%B1ol/2_efectos_arreglos_texto/ESCENAS.md)
4. Transformations/YouTube/[Scenes](https://github.com/Elteoremadebeethoven/AnimacionesConManim/blob/master/Espa%C3%B1ol/3_transformaciones_texto/ESCENAS.md)
5. Visual tools/YouTube/[Scenes](https://github.com/Elteoremadebeethoven/AnimacionesConManim/blob/master/Espa%C3%B1ol/4_herramientas_visuales/ESCENAS.md)
6. Introduction in 2D plot/YouTube/[Scenes](https://github.com/Elteoremadebeethoven/AnimacionesConManim/blob/master/Espa%C3%B1ol/5_introducci%C3%B3n_gr%C3%A1ficas/ESCENAS.md)
7. Introduction in 3D plot/YouTube/Scenes
8. Add audio/YouTube
9. Ad svg images/YouTube/Scenes
10. First project/YouTube

Extras:
* Leave progress bars by default.
* Customize the rendering.
* Modify the directory "media".

## What is Manim?
[Manim](https://github.com/3b1b/manim) is a free tool for Python created by [Grant Sanderson](http://www.3blue1brown.com/) ([twitter](https://twitter.com/3blue1brown?lang=es)), matematician from Stantford and owner of the channel of YouTube [3Blue1Brown](https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw). It is specialized in scientific subjects, mainly mathematical, so it is based on LaTeX commands (mainly in TeX).

## What is LaTeX?
LaTeX is a processor of specialized texts in the scientific field, however, Manim only uses the TeX commands (with some exceptions), which refers to the writing of formulas. An example of the code in TeX is:
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
* Works on Windows, GNU / Linux (any distribution) and Mac perfectly, although it is preferable to use Mac or GNU / Linux.
* Can be used in old computers.
* Being open source is completely customizable to the user's taste.
* It is constantly improving.
* The video files are very high quality and light.
* The formulas are created using the TeX commands, so they are of professional quality.
* In the case of not having programming knowledge, it is a good tool to start learning Python 3 and LaTeX.
### Disadvantages:
* If you do not have the LaTeX package (complete) installed, it will occupy more than 4 GB of space on your computer.
* A graphic interface is not used to perform the animations, everything is based on the Python 3 and TeX commands. The example of the classic Hello world! would be
```python
from big_ol_pile_of_manim_imports import *
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


