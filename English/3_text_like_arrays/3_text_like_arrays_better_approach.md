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
