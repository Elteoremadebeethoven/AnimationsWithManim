from manimlib.imports import *
from check_svg import *
from screen_grid import ScreenGrid
"""
You have to add
\usepackage{listings}
in your tex_template.tex file
"""

code_string = r"""\begin{lstlisting}[language=Python,basicstyle=\scriptsize\ttfamily]
square2.save_state()
def update_rotate_move(mob, alpha):
    square2.restore()
    square2.shift(RIGHT*10*alpha)
    square2.rotate(3*PI*alpha)
\end{lstlisting}
"""

MORADO_ST   ="#A682FE"
ROSA_ST     = "#F8206B"
VERDE_ST    = "#A1E303"
AMARILLO_ST = "#E6DC6B"
FONDO_ST    = "#272822"
AZUL_ST     = "#64DAF8"
NARANJA_ST  = "#FF9514"

class CodeNumbers(CheckTextNumbers):
    CONFIG = {
        "numbers_scale": 0.2,
    }
    def import_text(self):
        return TextMobject(code_string)

class GetCode:
    def change_color(self,text,pairs,color):
        for pair in pairs:
            if len(pair) == 2:
                a,b = pair
                text[a:b].set_color(color)
            else:
                text[pair[0]].set_color(color)

    def get_code(self):
        text = TextMobject(code_string)[0]
        pairs_blue = [(8,18),(20,23),(61,68),(78,83),(107,113)]
        pairs_green = [(23,41)]
        pairs_pink = [(89,),(92,),(115,),(118,)]
        pairs_purple = [(90,92),(114,)]
        pairs_orange = [(42,45),(46,51)]
        self.change_color(text,pairs_blue,AZUL_ST)
        self.change_color(text,pairs_green,VERDE_ST)
        self.change_color(text,pairs_pink,ROSA_ST)
        self.change_color(text,pairs_purple,MORADO_ST)
        self.change_color(text,pairs_orange,NARANJA_ST)
        return text

class ShiftAndRotate(Animation):
    CONFIG = {
        "axis": OUT,
        "run_time": 5,
        "rate_func": linear,
        "about_point": None,
        "about_edge": None,
    }
    def __init__(self, mobject, direction, radians,**kwargs):
        assert(isinstance(mobject, Mobject))
        digest_config(self, kwargs)
        self.mobject = mobject
        self.direction = direction
        self.radians = radians

    def interpolate_mobject(self, alpha):
        self.mobject.become(self.starting_mobject)
        self.mobject.shift(alpha*self.direction)
        self.mobject.rotate(
            alpha * self.radians,
            axis=self.axis,
            about_point=self.about_point,
            about_edge=self.about_edge,
        )

class AdvancedAnimationsSetup(Scene,GetCode):
    def change_finger(self,index):
        self.finger.move_to(
                [
                    0.5,
                    self.code[self.limits[index]].get_y(),
                    0
                ]
            )

    def get_position_finger(self,index):
        return [
                    0.5,
                    self.code[self.limits[index]].get_y(),
                    0
                ]

    def setup(self):
        code = self.get_code()
        code.scale(0.9)
        code.to_corner(UL,buff=0.3)
        self.code = code
        self.finger = SVGMobject("dedo",stroke_width=0)
        self.finger.flip()
        self.finger.set_height(0.4)
        self.limits = [19,52,69,98,124]
        self.change_finger(0)
        self.alphas_text = VGroup(
            *[TexMobject(r"\tt alpha\rm =",r"\rm\frac{%d}{10}"%i) for i in range(11)]
        )
        self.alphas_text.to_corner(UR,buff=0.5)
        self.alphas_text.shift(LEFT*2)
        self.add(
            self.code,
            self.finger,
            self.alphas_text[0]
        )

class AdvancedAnimations(AdvancedAnimationsSetup):
    def construct(self):
        path = Line(LEFT*5,RIGHT*5,stroke_opacity=0.5)
        phantom_path = DashedVMobject(path)
        path.shift(DOWN*1.5)
        phantom_path.add_updater(lambda mob: mob.move_to(path))

        square = Square().set_height(0.7)
        square.move_to(path.get_start())
        square_start = square.copy()
        square_start.set_color(RED)
        ticks = VGroup(*[
            DashedVMobject(Line(DOWN,UP,stroke_opacity=0.3))\
                .move_to(path.point_from_proportion(i/10))
            for i in range(0,11)
        ])
        marks = VGroup(*[
            TexMobject(r"\frac{%d}{10}"%i,height=0.6,fill_opacity=0.2)\
                .next_to(ticks[i],UP,buff=0.2)
            for i in range(0,11)
        ])
        self.add(phantom_path,square_start,square,ticks,marks)
        square.save_state()
        self.wait()
        self.play(
            self.finger.move_to,self.get_position_finger(2)
        )
        for i in range(0,10):
            alpha = i/10
            self.wait()
            self.play(
                self.finger.move_to,self.get_position_finger(3)
            )
            self.wait()
            self.play(
                square.move_to,path.point_from_proportion(alpha)
            )
            self.wait()
            self.play(
                self.finger.move_to,self.get_position_finger(4)
            )
            self.play(
                Rotate(square,3*PI*alpha)
            )
            self.play(
                marks[i].set_fill,None,1
            )
            if i > 0:
                phantom_square = square.copy()
                phantom_square.fade(0.5)
                self.add(phantom_square)
                self.bring_to_front(square)
            self.play(
                self.finger.move_to,self.get_position_finger(2)
            )
            self.play(Restore(square))
            self.play(
                ReplacementTransform(
                    self.alphas_text[i],
                    self.alphas_text[i+1]
                )
            )
        self.wait()
        self.play(
            ShiftAndRotate(square,RIGHT*10,3*PI),
            run_time=10
        )
        self.wait(3)
