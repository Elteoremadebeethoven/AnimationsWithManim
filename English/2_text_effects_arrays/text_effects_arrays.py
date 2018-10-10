from big_ol_pile_of_manim_imports import *

COLOR_P="#3EFC24"

class ColorTexto(Scene):
    def construct(self):
        texto = TextMobject("A","B","C","D","E","F")
        texto[0].set_color(RED)
        texto[1].set_color(BLUE)
        texto[2].set_color(GREEN)
        texto[3].set_color(ORANGE)
        texto[4].set_color("#DC28E2") #Los colores son hexadecimales
        texto[5].set_color(COLOR_P)
        self.play(Write(texto))
        self.wait(2)

class FormulaColor1(Scene): 
    def construct(self):
        texto = TexMobject("x","=","{a","\\over","b}")
        texto[0].set_color(RED)
        texto[1].set_color(BLUE)
        texto[2].set_color(GREEN)
        texto[3].set_color(ORANGE)
        texto[4].set_color("#DC28E2")
        self.play(Write(texto))
        self.wait(2)

class FormulaColor2(Scene): 
    def construct(self): 
        texto = TexMobject("x","=","\\frac{a}{b}")
        texto[0].set_color(RED)
        texto[1].set_color(BLUE)
        texto[2].set_color(GREEN)
        self.play(Write(texto))
        self.wait(2)

class FormulaColor3(Scene): 
    def construct(self):
        texto = TexMobject("\\sqrt{","\\int_{","a}^","{b}","\\left(","\\frac{x}{y}","\\right)","dx}")
        texto[0].set_color(RED)
        texto[1].set_color(BLUE)
        texto[2].set_color(GREEN)
        texto[3].set_color(YELLOW)
        texto[4].set_color(PINK)
        texto[5].set_color(ORANGE)
        texto[6].set_color(PURPLE)
        texto[7].set_color(MAROON)
        self.play(Write(texto))
        self.wait(2)

class FormulaColor3Mejorada(Scene): 
    def construct(self): 
        texto = TexMobject("\\sqrt{","\\int_{","a}^","{b}","\\left(","\\frac{x}{y}","\\right)","dx.}")
        texto[0].set_color(RED)
        texto[1].set_color(BLUE)
        texto[2].set_color(GREEN)
        texto[3].set_color(YELLOW)
        texto[4].set_color(PINK)
        texto[5].set_color(ORANGE)
        texto[6].set_color(PURPLE)
        texto[7].set_color(MAROON)
        self.play(Write(texto))
        self.wait(3)

class FormulaColor3Mejorada2(Scene): 
    def construct(self): 
        texto = TexMobject("\\sqrt{","\\int_","{a}^","{b}","{\\left(","{x","\\over","y}","\\right)}","d","x",".}")
        texto[0].set_color(RED)
        texto[1].set_color(BLUE)
        texto[2].set_color(GREEN)
        texto[3].set_color(YELLOW)
        texto[4].set_color(PINK)
        texto[5].set_color(ORANGE)
        texto[6].set_color(PURPLE)
        texto[7].set_color(MAROON)
        texto[8].set_color(TEAL)
        texto[9].set_color(GOLD)
        self.play(Write(texto))
        self.wait(3)

class FormulaColor4(Scene): 
    def construct(self): 
        texto = TexMobject("\\sqrt{","\\int_","{a","+","c}^","{b}","{\\left(","{x","\\over","y}","\\right)}","d","x",".}")
        texto[0].set_color(RED)
        texto[1].set_color(BLUE)
        texto[2].set_color(GREEN)
        texto[3].set_color(YELLOW)
        texto[4].set_color(PINK)
        texto[5].set_color(ORANGE)
        texto[6].set_color(PURPLE)
        texto[7].set_color(MAROON)
        texto[8].set_color(TEAL)
        texto[9].set_color(GOLD)
        texto[10].set_color(GRAY)
        texto[11].set_color(RED)
        self.play(Write(texto))
        self.wait(3)

class ColorPorCaracter(Scene):
	def construct(self):
		texto = TexMobject("{d","\\over","d","x","}","\\int_","{a}^","{","x","}","f(","t",")d","t","=","f(","x",")")
		texto.set_color_by_tex("x",RED)
		self.play(Write(texto))
		self.wait(2)

class ColorPorCaracterCorregida(Scene): 
	def construct(self):
		texto = TexMobject("{d","\\over","d","x","}","\\int_","{a}^","{","x","}","f(","t",")d","t","=","f(","x",")")
		texto.set_color_by_tex("x",RED)
		texto[6].set_color(RED)
		texto[8].set_color(WHITE)
		self.play(Write(texto))
		self.wait(2)
	
class ForLista(Scene): 
    def construct(self): #no usar siempre frac
        texto = TexMobject("[0]","[1]","[2]","[3]","[4]","[5]","[6]","[7]")
        for i in [0,1,3,4]:
        	texto[i].set_color(RED)
        self.play(Write(texto))
        self.wait(3)

class ForRango1(Scene): 
    def construct(self): #no usar siempre frac
        texto = TexMobject("[0]","[1]","[2]","[3]","[4]","[5]","[6]","[7]")
        for i in range(3):
        	texto[i].set_color(RED)
        self.play(Write(texto))
        self.wait(3)

class ForRango2(Scene): 
    def construct(self): #no usar siempre frac
        texto = TexMobject("[0]","[1]","[2]","[3]","[4]","[5]","[6]","[7]")
        for i in range(2,6):
        	texto[i].set_color(RED)
        self.play(Write(texto))
        self.wait(3)

class For2Variables(Scene): 
    def construct(self): #no usar siempre frac
        texto = TexMobject("[0]","[1]","[2]","[3]","[4]","[5]","[6]","[7]")
        for i,color in [(2,RED),(4,PINK)]:
        	texto[i].set_color(color)
        self.play(Write(texto))
        self.wait(3)

class CambioTamanho(Scene):
    def construct(self):
        texto = TexMobject("\\sum_{i=0}^n i=\\frac{n(n+1)}{2}")
        self.add(texto)
        self.wait()
        texto.scale_in_place(2)
        self.wait(2)

class AparicionDesaparicionTexto1(Scene):
    def construct(self):
        texto = TextMobject("Texto u objeto")
        self.wait()
        self.add(texto)
        self.wait()
        self.remove(texto)
        self.wait()

class AparicionDesaparicionTexto2(Scene):
    def construct(self):
        texto = TextMobject("Texto u objeto")
        self.play(FadeIn(texto))
        self.wait()
        self.play(FadeOut(texto),run_time=1)
        self.wait()

class EfectoAparicionTexto1(Scene):
    def construct(self):
        texto = TextMobject("Texto u objeto")
        self.play(FadeInFromDown(texto),run_time=1)
        self.wait()

class EfectoAparicionTexto2(Scene):
    def construct(self):
        texto = TextMobject("Texto u objeto")
        self.play(GrowFromCenter(texto),run_time=1)
        self.wait()

class EfectoAparicionTexto3(Scene):
    def construct(self):
        texto = TextMobject("Texto u objeto")
        self.play(ShowCreation(texto),run_time=1)
        self.wait()

class ColoreadoTexto(Scene):
    def construct(self):
        texto = TextMobject("Texto u objeto")
        self.add(texto)
        self.wait(0.5)
        for letra in texto:
            self.play(LaggedStart(
                ApplyMethod, letra,
                lambda m : (m.set_color, YELLOW),
                run_time = 0.12
            ))
        self.wait(0.5)

class Tachado1(Scene):
    def construct(self):
        texto = TexMobject("\\sum_{i=1}^{\infty}i","=","-\\frac{1}{2}")
        tache = Cross(texto[2])
        tache.set_stroke(RED, 6)
        self.play(Write(texto))
        self.wait(.5)
        self.play(ShowCreation(tache))
        self.wait(2)

class Tachado2(Scene):
    def construct(self):
        texto = TexMobject("\\sum_{i=1}^{\infty}i","=","-\\frac{1}{2}")
        eq = VGroup(texto[1],texto[2])
        tache = Cross(eq)
        tache.set_stroke(RED, 6)
        self.play(Write(texto))
        self.wait(.5)
        self.play(ShowCreation(tache))
        self.wait(2)

class Encuadre1(Scene):
    def construct(self):
        texto=TexMobject(
            "\\hat g(", "f", ")", "=", "\\int", "_{t_1}", "^{t_{2}}",
            "g(", "t", ")", "e", "^{-2\\pi i", "f", "t}", "dt"
        )
        marco = SurroundingRectangle(texto[4], buff = 0.5*SMALL_BUFF)
        self.play(Write(texto))
        self.wait(.5)
        self.play(ShowCreation(marco))
        self.wait(2)

class Encuadre2(Scene):
    def construct(self):
        texto=TexMobject(
            "\\hat g(", "f", ")", "=", "\\int", "_{t_1}", "^{t_{2}}",
            "g(", "t", ")", "e", "^{-2\\pi i", "f", "t}", "dt"
        )
        seleccion=VGroup(texto[4],texto[5],texto[6])
        marco = SurroundingRectangle(seleccion, buff = 0.5*SMALL_BUFF)
        marco.set_stroke(GREEN,9)
        self.play(Write(texto))
        self.wait(.5)
        self.play(ShowCreation(marco))
        self.wait(2)

class Llave(Scene):
    def construct(self):
        texto=TexMobject(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(texto))
        llave_s = Brace(texto[1], UP, buff = SMALL_BUFF)
        llave_i = Brace(texto[3], DOWN, buff = SMALL_BUFF)
        t_s = llave_s.get_text("$g'f$")
        t_i = llave_i.get_text("$f'g$")
        self.play(
            GrowFromCenter(llave_s),
            GrowFromCenter(llave_i),
            FadeIn(t_s),
            FadeIn(t_i)
            )
        self.wait()