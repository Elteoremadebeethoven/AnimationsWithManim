from big_ol_pile_of_manim_imports import *

COLOR_P="#3EFC24"

class TextColor(Scene):
    def construct(self):
        text = TextMobject("A","B","C","D","E","F")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(ORANGE)
        text[4].set_color("#DC28E2") #Hexadecimal color
        text[5].set_color(COLOR_P)
        self.play(Write(text))
        self.wait(2)

class FormulaColor1(Scene): 
    def construct(self):
        text = TexMobject("x","=","{a","\\over","b}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(ORANGE)
        text[4].set_color("#DC28E2")
        self.play(Write(text))
        self.wait(2)

class FormulaColor2(Scene): 
    def construct(self): 
        text = TexMobject("x","=","\\frac{a}{b}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        self.play(Write(text))
        self.wait(2)

class FormulaColor3(Scene): 
    def construct(self):
        text = TexMobject("\\sqrt{","\\int_{","a}^","{b}","\\left(","\\frac{x}{y}","\\right)","dx}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(YELLOW)
        text[4].set_color(PINK)
        text[5].set_color(ORANGE)
        text[6].set_color(PURPLE)
        text[7].set_color(MAROON)
        self.play(Write(text))
        self.wait(2)

class FormulaColor3Fixed(Scene): 
    def construct(self): 
        text = TexMobject("\\sqrt{","\\int_{","a}^","{b}","\\left(","\\frac{x}{y}","\\right)","dx.}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(YELLOW)
        text[4].set_color(PINK)
        text[5].set_color(ORANGE)
        text[6].set_color(PURPLE)
        text[7].set_color(MAROON)
        self.play(Write(text))
        self.wait(3)

class FormulaColor3Fixed2(Scene): 
    def construct(self): 
        text = TexMobject("\\sqrt{","\\int_","{a}^","{b}","{\\left(","{x","\\over","y}","\\right)}","d","x",".}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(YELLOW)
        text[4].set_color(PINK)
        text[5].set_color(ORANGE)
        text[6].set_color(PURPLE)
        text[7].set_color(MAROON)
        text[8].set_color(TEAL)
        text[9].set_color(GOLD)
        self.play(Write(text))
        self.wait(3)

class FormulaColor4(Scene): 
    def construct(self): 
        text = TexMobject("\\sqrt{","\\int_","{a","+","c}^","{b}","{\\left(","{x","\\over","y}","\\right)}","d","x",".}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(YELLOW)
        text[4].set_color(PINK)
        text[5].set_color(ORANGE)
        text[6].set_color(PURPLE)
        text[7].set_color(MAROON)
        text[8].set_color(TEAL)
        text[9].set_color(GOLD)
        text[10].set_color(GRAY)
        text[11].set_color(RED)
        self.play(Write(text))
        self.wait(3)

class FormulaColor5(Scene): 
    def construct(self): 
        text = TexMobject("\\sqrt{","\\int_","{a","+","c}^","{b}","{\\left(","{x","\\over","y}","\\right)}","d","x",".}")
        for i,color in zip(text,[PURPLE,BLUE,GREEN,YELLOW,PINK]):
            i.set_color(color)
        self.play(Write(text))
        self.wait(3)


class ColorByCaracter(Scene):
	def construct(self):
		text = TexMobject("{d","\\over","d","x","}","\\int_","{a}^","{","x","}","f(","t",")d","t","=","f(","x",")")
		text.set_color_by_tex("x",RED)
		self.play(Write(text))
		self.wait(2)

class ColorByCaracterFixed(Scene): 
	def construct(self):
		text = TexMobject("{d","\\over","d","x","}","\\int_","{a}^","{","x","}","f(","t",")d","t","=","f(","x",")")
		text.set_color_by_tex("x",RED)
		text[6].set_color(RED)
		text[8].set_color(WHITE)
		self.play(Write(text))
		self.wait(2)
	
class ListFor(Scene): 
    def construct(self): #no usar siempre frac
        text = TexMobject("[0]","[1]","[2]","[3]","[4]","[5]","[6]","[7]")
        for i in [0,1,3,4]:
        	text[i].set_color(RED)
        self.play(Write(text))
        self.wait(3)

class ForRange1(Scene): 
    def construct(self): #no usar siempre frac
        text = TexMobject("[0]","[1]","[2]","[3]","[4]","[5]","[6]","[7]")
        for i in range(3):
        	text[i].set_color(RED)
        self.play(Write(text))
        self.wait(3)

class ForRange2(Scene): 
    def construct(self): #no usar siempre frac
        text = TexMobject("[0]","[1]","[2]","[3]","[4]","[5]","[6]","[7]")
        for i in range(2,6):
        	text[i].set_color(RED)
        self.play(Write(text))
        self.wait(3)

class ForTwoVariables(Scene): 
    def construct(self): #no usar siempre frac
        text = TexMobject("[0]","[1]","[2]","[3]","[4]","[5]","[6]","[7]")
        for i,color in [(2,RED),(4,PINK)]:
        	text[i].set_color(color)
        self.play(Write(text))
        self.wait(3)

class ChangeSize(Scene):
    def construct(self):
        text = TexMobject("\\sum_{i=0}^n i=\\frac{n(n+1)}{2}")
        self.add(text)
        self.wait()
        text.scale_in_place(2)
        self.wait(2)

class AddAndRemoveText(Scene):
    def construct(self):
        text = TextMobject("Text or object")
        self.wait()
        self.add(text)
        self.wait()
        self.remove(text)
        self.wait()

class FadeText(Scene):
    def construct(self):
        text = TextMobject("Text or object")
        self.play(FadeIn(text))
        self.wait()
        self.play(FadeOut(text),run_time=1)
        self.wait()

class FadeTextFromDirection(Scene):
    def construct(self):
        text = TextMobject("Text or object")
        self.play(FadeInFrom(text,DOWN),run_time=1)
        self.wait()

class GrowObjectFromCenter(Scene):
    def construct(self):
        text = TextMobject("Text or object")
        self.play(GrowFromCenter(text),run_time=1)
        self.wait()

class ShowCreationObject(Scene):
    def construct(self):
        text = TextMobject("Text or object")
        self.play(ShowCreation(text),run_time=1)
        self.wait()

class ColoringText(Scene):
    def construct(self):
        text = TextMobject("Text or object")
        self.add(text)
        self.wait(0.5)
        for letter in text:
            self.play(LaggedStart(
                ApplyMethod, letter,
                lambda m : (m.set_color, YELLOW),
                run_time = 0.12
            ))
        self.wait(0.5)

class CrossText1(Scene):
    def construct(self):
        text = TexMobject("\\sum_{i=1}^{\\infty}i","=","-\\frac{1}{2}")
        cross = Cross(text[2])
        cross.set_stroke(RED, 6)
        self.play(Write(text))
        self.wait(.5)
        self.play(ShowCreation(cross))
        self.wait(2)

class CrossText2(Scene):
    def construct(self):
        text = TexMobject("\\sum_{i=1}^{\\infty}i","=","-\\frac{1}{2}")
        eq = VGroup(text[1],text[2])
        cross = Cross(eq)
        cross.set_stroke(RED, 6)
        self.play(Write(text))
        self.wait(.5)
        self.play(ShowCreation(cross))
        self.wait(2)

class FrameBox1(Scene):
    def construct(self):
        text=TexMobject(
            "\\hat g(", "f", ")", "=", "\\int", "_{t_1}", "^{t_{2}}",
            "g(", "t", ")", "e", "^{-2\\pi i", "f", "t}", "dt"
        )
        frameBox = SurroundingRectangle(text[4], buff = 0.5*SMALL_BUFF)
        self.play(Write(text))
        self.wait(.5)
        self.play(ShowCreation(frameBox))
        self.wait(2)

class FrameBox2(Scene):
    def construct(self):
        text=TexMobject(
            "\\hat g(", "f", ")", "=", "\\int", "_{t_1}", "^{t_{2}}",
            "g(", "t", ")", "e", "^{-2\\pi i", "f", "t}", "dt"
        )
        seleccion=VGroup(text[4],text[5],text[6])
        frameBox = SurroundingRectangle(seleccion, buff = 0.5*SMALL_BUFF)
        frameBox.set_stroke(GREEN,9)
        self.play(Write(text))
        self.wait(.5)
        self.play(ShowCreation(frameBox))
        self.wait(2)

class BraceText(Scene):
    def construct(self):
        text=TexMobject(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        brace_top = Brace(text[1], UP, buff = SMALL_BUFF)
        brace_bottom = Brace(text[3], DOWN, buff = SMALL_BUFF)
        text_top = brace_top.get_text("$g'f$")
        text_bottom = brace_bottom.get_text("$f'g$")
        self.play(
            GrowFromCenter(brace_top),
            GrowFromCenter(brace_bottom),
            FadeIn(text_top),
            FadeIn(text_bottom)
            )
        self.wait()