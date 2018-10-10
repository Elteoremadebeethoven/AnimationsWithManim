class Texto2Dv1(Scene):
    def construct(self):
        texto = TextMobject("Texto")
        # texto[0] = T
        # texto[1] = e
        texto.set_color(RED)
        texto[0:3].set_color(GREEN)
        texto[1].set_color(BLUE)
        texto.scale(3)
        self.play(Write(texto))
        self.play(
                    texto[2].set_color,PINK, 
                    texto[2].scale, 1.5,
                    rate_func = there_and_back
                )
        self.play(ReplacementTransform(texto[0].copy(),texto[3]),path_arc = -PI/2)
        self.wait()

class Texto2Dv2(Scene):
    def construct(self):
        texto = TextMobject("Texto 1","Texto 2")
        # texto[0] = Texto 1
        # texto[1] = Texto 2
        # texto[0][0] = T
        # texto[1][0] = T pero del segundo elemento: Texto 2
        texto[0].set_color(RED)
        texto[0][0:3].set_color(GREEN)
        texto[1].set_color(BLUE)
        texto.scale(3)
        self.play(Write(texto))
        self.play(
                    texto[0][2].set_color,PINK, 
                    texto[0][2].scale, 1.5,
                    rate_func = there_and_back
                )
        self.play(ReplacementTransform(texto[0][0].copy(),texto[1][0]),path_arc = -PI/2)
        self.wait()