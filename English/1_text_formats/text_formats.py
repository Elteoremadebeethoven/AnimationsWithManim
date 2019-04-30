from big_ol_pile_of_manim_imports import *

class WriteText(Scene): 
    def construct(self): 
        text = TextMobject("This is a regular text")
        self.play(Write(text))
        self.wait(3)

class AddText(Scene): 
    def construct(self): 
        text = TextMobject("This is a regular text")
        self.add(text)
        self.wait(3)

class Formula(Scene): 
    def construct(self): 
        formula = TexMobject("This is a formula")
        self.play(Write(formula))
        self.wait(3)

class TipesOfText(Scene): 
    def construct(self): 
        tipesOfText = TextMobject("""
        	This is a regular text,
        	$this is a formula$,
        	$$this is a formula$$
        	""")
        self.play(Write(tipesOfText))
        self.wait(3)

class TipesOfText2(Scene): 
    def construct(self): 
        tipesOfText = TextMobject("""
        	This is a regular text,
        	$\\frac{x}{y}$,
        	$$x^2+y^2=a^2$$
        	""")
        self.play(Write(tipesOfText))
        self.wait(3)

class DisplayFormula(Scene): 
    def construct(self): 
        tipesOfText = TextMobject("""
        	This is a regular text,
        	$\\displaystyle\\frac{x}{y}$,
        	$$x^2+y^2=a^2$$
        	""")
        self.play(Write(tipesOfText))
        self.wait(3)

class TextInCenter(Scene):
    def construct(self):
        text = TextMobject("Text")
        self.play(Write(text))
        self.wait(3)

class TextOnTopEdge(Scene):
    def construct(self):
        text = TextMobject("Text")
        text.to_edge(UP)
        self.play(Write(text))
        self.wait(3)

class TextOnBottomEdge(Scene):
    def construct(self):
        text = TextMobject("Text")
        text.to_edge(DOWN)
        self.play(Write(text))
        self.wait(3)

class TextOnRightEdge(Scene):
    def construct(self):
        text = TextMobject("Text")
        text.to_edge(RIGHT)
        self.play(Write(text))
        self.wait(3)

class TextOnLeftEdge(Scene):
    def construct(self):
        text = TextMobject("Text")
        text.to_edge(LEFT)
        self.play(Write(text))
        self.wait(3)

class TextInUpperRightCorner(Scene):
    def construct(self):
        text = TextMobject("Text")
        text.to_edge(UP+RIGHT)
        self.play(Write(text))
        self.wait(3)

class TextInLowerLeftCorner(Scene): 
    def construct(self): 
        text = TextMobject("Text") 
        text.to_edge(LEFT+DOWN)
        self.play(Write(text))
        self.wait(3)

class CustomPosition1(Scene):
    def construct(self):
        textM = TextMobject("Text")
        textC = TextMobject("Central text")
        textM.move_to(0.25*UP) 
        self.play(Write(textM),Write(textC))
        self.wait(3)

class CustomPosition2(Scene):
    def construct(self):
        textM = TextMobject("Text")
        textC = TextMobject("Central text")
        textM.move_to(1*UP+1*RIGHT)
        self.play(Write(textM),Write(textC))
        self.wait(1)
        textM.move_to(1*UP+1*RIGHT) 
        self.play(Write(textM))
        self.wait(3)

class RelativePosition1(Scene):
    def construct(self):
        textM = TextMobject("Text")
        textC = TextMobject("Reference text")
        textM.next_to(textC,LEFT,buff=1) 
        self.play(Write(textM),Write(textC))
        self.wait(3)

class RelativePosition2(Scene):
    def construct(self):
        textM = TextMobject("Text")
        textC = TextMobject("Reference text")
        textM.shift(UP*0.1)
        self.play(Write(textM),Write(textC))
        self.wait(3)

class RotateObject(Scene):
    def construct(self):
        textM = TextMobject("Text")
        textC = TextMobject("Reference text")
        textM.shift(UP)
        textM.rotate(PI/4) 
        self.play(Write(textM),Write(textC))
        self.wait(2)
        textM.rotate(PI/4)
        self.wait(2)
        textM.rotate(PI/4)
        self.wait(2)
        textM.rotate(PI/4)
        self.wait(2)
        textM.rotate(PI)
        self.wait(2)

class MirrorObject(Scene):
    def construct(self):
        textM = TextMobject("Text")
        textM.flip(UP)
        self.play(Write(textM))
        self.wait(2)

class SizeTextOnLaTeX(Scene):
	def construct(self):
		textHuge = TextMobject("{\\Huge Huge Text 012.\\#!?} Text")
		texthuge = TextMobject("{\\huge huge Text 012.\\#!?} Text")
		textLARGE = TextMobject("{\\LARGE LARGE Text 012.\\#!?} Text")
		textLarge = TextMobject("{\\Large Large Text 012.\\#!?} Text")
		textlarge = TextMobject("{\\large large Text 012.\\#!?} Text")
		textNormal = TextMobject("{\\normalsize normal Text 012.\\#!?} Text")
		textsmall = TextMobject("{\\small small Text 012.\\#!?} Texto normal")
		textfootnotesize = TextMobject("{\\footnotesize footnotesize Text 012.\\#!?} Text")
		textscriptsize = TextMobject("{\\scriptsize scriptsize Text 012.\\#!?} Text")
		texttiny = TextMobject("{\\tiny tiny Texto 012.\\#!?} Text normal")
		textHuge.to_edge(UP)
		texthuge.next_to(textHuge,DOWN,buff=0.1)
		textLARGE.next_to(texthuge,DOWN,buff=0.1)
		textLarge.next_to(textLARGE,DOWN,buff=0.1)
		textlarge.next_to(textLarge,DOWN,buff=0.1)
		textNormal.next_to(textlarge,DOWN,buff=0.1)
		textsmall.next_to(textNormal,DOWN,buff=0.1)
		textfootnotesize.next_to(textsmall,DOWN,buff=0.1)
		textscriptsize.next_to(textfootnotesize,DOWN,buff=0.1)
		texttiny.next_to(textscriptsize,DOWN,buff=0.1)
		self.add(textHuge,texthuge,textLARGE,textLarge,textlarge,textNormal,textsmall,textfootnotesize,textscriptsize,texttiny)
		self.wait(3)

class TextFonts(Scene):
	def construct(self):
		textNormal = TextMobject("{Roman serif text 012.\\#!?} Text")
		textItalic = TextMobject("\\textit{Italic text 012.\\#!?} Text")
		textTypewriter = TextMobject("\\texttt{Typewritter text 012.\\#!?} Text")
		textBold = TextMobject("\\textbf{Bold text 012.\\#!?} Text")
		textSL = TextMobject("\\textsl{Slanted text 012.\\#!?} Text")
		textSC = TextMobject("\\textsc{Small caps text 012.\\#!?} Text")
		textNormal.to_edge(UP)
		textItalic.next_to(textNormal,DOWN,buff=.5)
		textTypewriter.next_to(textItalic,DOWN,buff=.5)
		textBold.next_to(textTypewriter,DOWN,buff=.5)
		textSL.next_to(textBold,DOWN,buff=.5)
		textSC.next_to(textSL,DOWN,buff=.5)
		self.add(textNormal,textItalic,textTypewriter,textBold,textSL,textSC)
		self.wait(3)
