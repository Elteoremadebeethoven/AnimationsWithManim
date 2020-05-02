class colorIssue(Scene):
    def construct(self):
        # it shows error if you put a single "{" or "}" braces character into array 
        numeros4 = TexMobject( "\\mathbb{N}", "=", "\\{", "1", ",", "2", ",", "3", ",", "\\ldots", "\\}" )
        numeros4[0][2].set_color(RED)
        self.add(numeros4)
        self.wait()

class colorissueSolved(Scene):
    def construct(self):
        # if you want to color "{" or "}" braces character separately
        numeros4 = TexMobject( "\\mathbb{N}=\\{1,2,3,\\ldots\\}")
        # coloring first 2 characters 
        numeros4[0][0:2].set_color(GREEN)
        # coloring 3rd character
        numeros4[0][2].set_color(RED)
        self.add(numeros4)
        self.wait()
