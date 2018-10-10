from big_ol_pile_of_manim_imports import *

class WriteText(Scene): 
    def construct(self): 
        text = TextMobject("This is a normal text")
        self.play(Write(text))
        self.wait(3)

class TextoAdd(Scene): 
    def construct(self): 
        texto = TextMobject("Esto es un texto normal")
        self.add(texto)
        self.wait(3)

class Formula(Scene): 
    def construct(self): 
        formula = TexMobject("Esto es una formula")
        self.play(Write(formula))
        self.wait(3)

class TextoMixto(Scene): 
    def construct(self): 
        textoMixto = TextMobject("""
        	Esto es un texto normal,
        	$esto es una formula$,
        	$$esto es una formula$$
        	""")
        self.play(Write(textoMixto))
        self.wait(3)

class TextoMixto2(Scene): 
    def construct(self): 
        textoMixto = TextMobject("""
        	Esto es un texto normal,
        	$\\frac{x}{y}$,
        	$$x^2+y^2=a^2$$
        	""")
        self.play(Write(textoMixto))
        self.wait(3)

class TextoMixtoDisplay(Scene): 
    def construct(self): 
        textoMixto = TextMobject("""
        	Esto es un texto normal,
        	$\\displaystyle\\frac{x}{y}$,
        	$$x^2+y^2=a^2$$
        	""")
        self.play(Write(textoMixto))
        self.wait(3)

class PosicionTextoCentro(Scene):
    def construct(self):
        texto = TextMobject("Texto genérico.")
        self.play(Write(texto))
        self.wait(3)

class PosicionTextoSuperior(Scene):
    def construct(self):
        texto = TextMobject("Texto genérico.")
        texto.to_edge(UP)
        self.play(Write(texto))
        self.wait(3)

class PosicionTextoInferior(Scene):
    def construct(self):
        texto = TextMobject("Texto genérico.")
        texto.to_edge(DOWN)
        self.play(Write(texto))
        self.wait(3)

class PosicionTextoDerecha(Scene): #Probar con "Texto genérico ampliado"
    def construct(self):
        texto = TextMobject("Texto genérico.")
        texto.to_edge(RIGHT)
        self.play(Write(texto))
        self.wait(3)

class PosicionTextoIzquierda(Scene):
    def construct(self):
        texto = TextMobject("Texto genérico.")
        texto.to_edge(LEFT)
        self.play(Write(texto))
        self.wait(3)

class PosicionTextoSuperiorDerecha(Scene):
    def construct(self):
        texto = TextMobject("Texto genérico.")
        texto.to_edge(UP+RIGHT)
        self.play(Write(texto))
        self.wait(3)

class PosicionTextoInferiorIzquierda(Scene): 
    def construct(self): #Este es un comentario, no es código
        texto = TextMobject("Texto genérico.") #Este es un comentario, no es código
        texto.to_edge(LEFT+DOWN)
        self.play(Write(texto))
        self.wait(3)

class PosicionPersonalizado1(Scene):
    def construct(self):
        textoM = TextMobject("Texto genérico.")
        textoC = TextMobject("Texto genérico central.") #Texto de referencia
        textoM.move_to(0.25*UP)  #Jugar con los valores numéricos
        self.play(Write(textoM),Write(textoC))
        self.wait(3)

class PosicionPersonalizado2(Scene): #move_to siempre es referente al centro
    def construct(self):
        textoM = TextMobject("Texto genérico.")
        textoC = TextMobject("Texto genérico central.")
        textoM.move_to(1*UP+1*RIGHT)
        self.play(Write(textoM),Write(textoC))
        self.wait(1)
        textoM.move_to(1*UP+1*RIGHT) #El sistema de referencia es el centro
        self.play(Write(textoM))
        self.wait(3)

class PosicionRelativa1(Scene):
    def construct(self):
        textoM = TextMobject("Texto relativo.")
        textoC = TextMobject("Texto de referencia.")
        textoM.next_to(textoC,LEFT,buff=1) #La posición toma como referencia la posición de textoC
        self.play(Write(textoM),Write(textoC))
        self.wait(3)

class Tamanhos(Scene):
	def construct(self):
		textoHuge = TextMobject("{\\Huge Huge Texto 012.\\#!?} Texto normal")
		textohuge = TextMobject("{\\huge huge Texto 012.\\#!?} Texto normal")
		textoLARGE = TextMobject("{\\LARGE LARGE Texto 012.\\#!?} Texto normal")
		textoLarge = TextMobject("{\\Large Large Texto 012.\\#!?} Texto normal")
		textolarge = TextMobject("{\\large large Texto 012.\\#!?} Texto normal")
		textoNormal = TextMobject("{\\normalsize normal Texto 012.\\#!?} Texto normal")
		textosmall = TextMobject("{\\small small Texto 012.\\#!?} Texto normal")
		textofootnotesize = TextMobject("{\\footnotesize footnotesize Texto 012.\\#!?} Texto normal")
		textoscriptsize = TextMobject("{\\scriptsize scriptsize Texto 012.\\#!?} Texto normal")
		textotiny = TextMobject("{\\tiny tiny Texto 012.\\#!?} Texto normal")
		textoHuge.to_edge(UP)
		textohuge.next_to(textoHuge,DOWN,buff=0.1)
		textoLARGE.next_to(textohuge,DOWN,buff=0.1)
		textoLarge.next_to(textoLARGE,DOWN,buff=0.1)
		textolarge.next_to(textoLarge,DOWN,buff=0.1)
		textoNormal.next_to(textolarge,DOWN,buff=0.1)
		textosmall.next_to(textoNormal,DOWN,buff=0.1)
		textofootnotesize.next_to(textosmall,DOWN,buff=0.1)
		textoscriptsize.next_to(textofootnotesize,DOWN,buff=0.1)
		textotiny.next_to(textoscriptsize,DOWN,buff=0.1)
		self.add(textoHuge,textohuge,textoLARGE,textoLarge,textolarge,textoNormal,textosmall,textofootnotesize,textoscriptsize,textotiny)
		self.wait(3)

class TamanhosPersonalizados(Scene):
	def construct(self):
		texto = TextMobject("{\\fontsize{60}{70}\\selectfont Texto.}")
		self.play(Write(texto))
		self.wait(3)

class Fuentes(Scene):
	def construct(self):
		textoNormal = TextMobject("{Texto normal 012.\\#!?} Texto normal")
		textoItalica = TextMobject("\\textit{Texto en itálicas 012.\\#!?} Texto normal")
		textoMaquina = TextMobject("\\texttt{Texto en máquina 012.\\#!?} Texto normal")
		textoNegritas = TextMobject("\\textbf{Texto en negritas 012.\\#!?} Texto normal")
		textoSL = TextMobject("\\textsl{Texto en sl 012.\\#!?} Texto normal")
		textoSC = TextMobject("\\textsc{Texto en sc 012.\\#!?} Texto normal")
		textoNormal.to_edge(UP)
		textoItalica.next_to(textoNormal,DOWN,buff=.5)
		textoMaquina.next_to(textoItalica,DOWN,buff=.5)
		textoNegritas.next_to(textoMaquina,DOWN,buff=.5)
		textoSL.next_to(textoNegritas,DOWN,buff=.5)
		textoSC.next_to(textoSL,DOWN,buff=.5)
		self.add(textoNormal,textoItalica,textoMaquina,textoNegritas,textoSL,textoSC)
		self.wait(3)
