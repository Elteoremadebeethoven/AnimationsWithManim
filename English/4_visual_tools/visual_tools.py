from big_ol_pile_of_manim_imports import *

class MovimientoLlaves(Scene):
    def construct(self):
        texto=TexMobject(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(texto))
        llave1 = Brace(texto[1], UP, buff = SMALL_BUFF)
        llave2 = Brace(texto[3], UP, buff = SMALL_BUFF)
        t1 = llave1.get_text("$g'f$")
        t2 = llave2.get_text("$f'g$")
        self.play(
            GrowFromCenter(llave1),
            FadeIn(t1),
            )
        self.wait()
        self.play(
        	ReplacementTransform(llave1,llave2),
        	ReplacementTransform(t1,t2)
        	)
        self.wait()

class MovimientoLlavesCopia(Scene):
    def construct(self):
        texto=TexMobject(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(texto))
        llave1 = Brace(texto[1], UP, buff = SMALL_BUFF)
        llave2 = Brace(texto[3], UP, buff = SMALL_BUFF)
        t1 = llave1.get_text("$g'f$")
        t2 = llave2.get_text("$f'g$")
        self.play(
            GrowFromCenter(llave1),
            FadeIn(t1),
            )
        self.wait()
        self.play(
        	ReplacementTransform(llave1.copy(),llave2),
        	ReplacementTransform(t1.copy(),t2)
        	)
        self.wait()

class MovimientoEncuadre(Scene):
    def construct(self):
        texto=TexMobject(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(texto))
        marco1 = SurroundingRectangle(texto[1], buff = .1)
        marco2 = SurroundingRectangle(texto[3], buff = .1)
        self.play(
            ShowCreation(marco1),
            )
        self.wait()
        self.play(
        	ReplacementTransform(marco1,marco2),
        	)
        self.wait()

class MovimientoEncuadreCopia(Scene):
    def construct(self):
        texto=TexMobject(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(texto))
        marco1 = SurroundingRectangle(texto[1], buff = .1)
        marco2 = SurroundingRectangle(texto[3], buff = .1)
        self.play(ShowCreation(marco1))
        self.wait()
        self.play(
        	ReplacementTransform(marco1.copy(),marco2),
        	path_arc=-np.pi
        	)
        self.wait()

class MovimientoEncuadreCopia2(Scene):
    def construct(self):
        texto=TexMobject(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(texto))
        marco1 = SurroundingRectangle(texto[1], buff = .1)
        marco2 = SurroundingRectangle(texto[3], buff = .1)
        t1 = TexMobject("g'f")
        t2 = TexMobject("f'g")
        t1.next_to(marco1, UP, buff=0.1)
        t2.next_to(marco2, UP, buff=0.1)
        self.play(
        	ShowCreation(marco1),
        	FadeIn(t1)
        	)
        self.wait()
        self.play(
        	ReplacementTransform(marco1.copy(),marco2),
        	ReplacementTransform(t1.copy(),t2),
        	)
        self.wait()

class Flecha1(Scene):
	def construct(self):
		paso1 = TextMobject("Paso 1")
		paso2 = TextMobject("Paso 2")
		flecha = Arrow(LEFT,RIGHT)
		paso1.move_to(LEFT*2)
		flecha.next_to(paso1,RIGHT,buff = .1)
		paso2.next_to(flecha,RIGHT,buff = .1)
		self.play(Write(paso1))
		self.wait()
		self.play(GrowArrow(flecha))
		self.play(Write(paso2))
		self.wait()

class Flecha2(Scene):
	def construct(self):
		paso1 = TextMobject("Paso 1")
		paso2 = TextMobject("Paso 2")
		paso1.move_to(LEFT*2+DOWN*2)
		paso2.move_to(4*RIGHT+2*UP)
		flecha1 = Arrow(paso1.get_right(),paso2.get_left(),buff=0.1)
		flecha1.set_color(RED)
		flecha2 = Arrow(paso1.get_top(),paso2.get_bottom(),buff=0.1)
		flecha2.set_color(BLUE)
		self.play(Write(paso1),Write(paso2))
		self.play(GrowArrow(flecha1))
		self.play(GrowArrow(flecha2))
		self.wait()

class Linea(Scene):
	def construct(self):
		paso1 = TextMobject("Paso 1")
		paso2 = TextMobject("Paso 2")
		paso1.move_to(LEFT*2+DOWN*2)
		paso2.move_to(4*RIGHT+2*UP)
		linea1 = Line(paso1.get_right(),paso2.get_left(),buff=0.1)
		linea1.set_color(RED)
		linea2 = Line(paso1.get_top(),paso2.get_bottom(),buff=0.1)
		linea2.set_color(BLUE)
		self.play(Write(paso1),Write(paso2))
		self.play(ShowCreation(linea1))
		self.play(ShowCreation(linea2))
		self.wait()

class LineaDiscontinua(Scene):
	def construct(self):
		paso1 = TextMobject("Paso 1")
		paso2 = TextMobject("Paso 2")
		paso1.move_to(LEFT*2+DOWN*2)
		paso2.move_to(4*RIGHT+2*UP)
		linea1 = DashedLine(paso1.get_right(),paso2.get_left(),buff=0.1)
		linea1.set_color(RED)
		linea2 = Line(paso1.get_top(),paso2.get_bottom(),buff=0.1)
		linea2.set_color(BLUE)
		self.play(Write(paso1),Write(paso2))
		self.play(ShowCreation(linea1))
		self.play(ShowCreation(linea2))
		self.wait()

class AnimacionLinea1(Scene):
	def construct(self):
		paso1 = TextMobject("Paso 1")
		paso2 = TextMobject("Paso 2")
		paso1.move_to(LEFT*2+DOWN*2)
		paso2.move_to(4*RIGHT+2*UP)
		linea = Line(paso1.get_right(),paso2.get_left(),buff=0.1)
		self.play(Write(paso1),Write(paso2))
		self.play(GrowArrow(linea))
		self.play(
			paso2.next_to, paso2, LEFT*2,
			)
		self.wait()

class AnimacionLinea2(Scene):
	def construct(self):
		paso1 = TextMobject("Paso 1")
		paso2 = TextMobject("Paso 2")
		paso3 = paso2.copy()
		paso1.move_to(LEFT*2+DOWN*2)
		paso2.move_to(4*RIGHT+2*UP)
		paso3.next_to(paso2, LEFT*2)
		linea = Line(paso1.get_right(),paso2.get_left(),buff=0.1)
		lineaCopia = Line(paso1.get_right(),paso3.get_bottom(),buff=0.1)
		self.play(Write(paso1),Write(paso2))
		self.play(GrowArrow(linea))
		self.play(
			ReplacementTransform(paso2,paso3),
			ReplacementTransform(linea,lineaCopia)
			)
		self.wait()