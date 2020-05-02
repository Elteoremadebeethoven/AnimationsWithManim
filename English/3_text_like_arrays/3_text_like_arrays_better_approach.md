```python3
COLOR_P="#3EFC24"

class colorIssue(Scene):
    def construct(self):
        # it shows error if you put a single "{" or "}" braces character into array 
        numeros4 = TexMobject( "\\mathbb{N}", "=", "\\{", "1", ",", "2", ",", "3", ",", "\\ldots", "\\}" )
        numeros4[0][2].set_color(RED)
        self.add(numeros4)
        self.wait()

class colorBetterApproach(Scene):
    def construct(self):
        # if you want to color "{" or "}" braces character separately
        numeros4 = TexMobject( "\\mathbb{N}=\\{1,2,3,\\ldots\\}")
        # coloring first 2 characters 
        numeros4[0][0:2].set_color(GREEN)
        # coloring 3rd character
        numeros4[0][2].set_color(RED)
        self.add(numeros4)
        self.wait()
```

<p align="center"><img src ="/English/3_text_like_arrays/gifs/3_text_like_arrays_better_approach.png" /></p>

```python3

class colorBetterApproach1(Scene):
    def construct(self):
       text = TexMobject("\\sqrt{\\int_{a}^{b}\\left(\\frac{x}{y}\\right)dx}")
        text[0][0].set_color(RED)
        text[0][1].set_color(BLUE)
        text[0][2].set_color(GREEN)
        text[0][3].set_color(YELLOW)
        text[0][4].set_color(PINK)
        text[0][5].set_color(ORANGE)
        text[0][6].set_color(PURPLE)
        text[0][7].set_color(MAROON)
        text[0][8].set_color(TEAL)
        text[0][9].set_color(GOLD)
        text[0][10].set_color(GRAY)
        text[0][11].set_color(RED)
        self.play(Write(text))
        self.wait()
```

<p align="center"><img src ="/English/3_text_like_arrays/gifs/text_like_arrays_better_approach.gif" /></p>
