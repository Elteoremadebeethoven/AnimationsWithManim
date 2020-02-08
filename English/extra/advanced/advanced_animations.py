from manimlib.imports import *
from screen_grid import ScreenGrid

class Scene(Scene):
    CONFIG = {
        "camera_config":{"background_color":"#161616"},
        "include_grid":True
    }
    def setup(self):
        if self.include_grid:
            self.add(ScreenGrid().fade(0.7))

"""
See manimlib/mobject/mobject.py
===============================

    def to_edge(self, edge=LEFT, buff=DEFAULT_MOBJECT_TO_EDGE_BUFFER):
                      ----------
    Default:
                edge = LEFT
                buff = DEFAULT_MOBJECT_TO_EDGE_BUFFER
"""

class ToEdgeAnimation1(Scene):
    def construct(self):
        mob = Circle()

        self.add(mob)
        self.play(
                # Si no le introducimos parametros
                # entonces la animacion utilizara 
                # los que estan por defecto
                mob.to_edge,
            )
        self.wait()

class ToEdgeAnimation2(Scene):
    def construct(self):
        mob = Circle()

        self.add(mob)
        self.play(
                #            edge
                mob.to_edge, UP  
            )
        self.wait()

class ToEdgeAnimation3(Scene):
    def construct(self):
        mob = Circle()

        self.add(mob)
        self.play(
                #            edge, buff
                mob.to_edge, UP  , 0
            )
        self.wait()

# Cambiar parametros especificos

class ToEdgeAnimation4(Scene):
    def construct(self):
        mob = Circle()

        self.add(mob)
        self.play(
                # To modify only a single paramter
                # the edge = LEFT by default
                mob.to_edge,{"buff":0},
            )
        self.wait()

# Multiples animaciones

class ToEdgeAnimation5(Scene):
    def construct(self):
        mob = Circle()

        self.add(mob)
        self.play(
                # The order matters
                mob.to_edge,{"buff":0},
                mob.scale,0.1,
            )
        self.wait()

class ToEdgeAnimation6(Scene):
    def construct(self):
        mob = Circle()
        mob.generate_target()
        # The order still matters
        mob.target.scale(0.1)
        mob.target.to_edge(RIGHT,buff=0)

        self.add(mob)
        self.play(
                MoveToTarget(mob)
            )
        self.wait()

"""
    def scale(self, scale_factor, **kwargs):
                    ------------
                    scale_factor is not predefined
                                    ---
"""


class ScaleAnimation(Scene):
    def construct(self):
        mob = Circle()
        dot = Dot([6,0,0])

        self.add(mob,screen_grid,dot)
        self.play(
                mob.scale,3
            )
        self.play(
                # But if we want more args we have to use a dictionary
                mob.scale,1/3,{"about_point":dot.get_center()}
                # Replace dot.get_center() with ORIGIN
            )
        self.wait()

"""

    def arrange(self, direction=RIGHT, center=True, **kwargs):
                      -----------------------------
"""

class ArrangeAnimation1(Scene):
    def construct(self):
        vgroup = VGroup(
                    Square(),
                    Circle()
                )
        self.add(vgroup)
        self.wait()
        self.play(vgroup.arrange,DOWN)
        self.wait()

class ArrangeAnimation2(Scene):
    def construct(self):
        vgroup = VGroup(
                    Square(),
                    Circle()
                )
        self.add(vgroup)
        self.wait()
        self.play(vgroup.arrange,DOWN,{"buff":0})
        self.wait()

class ArrangeAnimation3(Scene):
    def construct(self):
        vgroup = VGroup(
                    Square(),
                    Circle()
                )
        text = TextMobject("Hello world").to_corner(UL)
        self.add(vgroup)
        self.wait()
        self.play(
                vgroup.arrange,DOWN,{"buff":0},
                Write(text)
            )
        self.wait()

"""
    def shift(self, *vectors):
                    ---------
                     args
"""

class ShiftAnimation1Fail(Scene):
    def construct(self):
        mob = Circle()

        self.add(mob)
        self.play(
                # We can set "n" paraters
                mob.shift,LEFT,LEFT,
                FadeToColor(mob,TEAL)
                # FadeToColor is a MoveToTarget method
            )
        self.wait()

class ShiftAnimation1(Scene):
    def construct(self):
        mob = Circle()

        self.add(mob)
        self.play(
                mob.shift,LEFT,LEFT,LEFT,
                mob.set_color,TEAL
            )
        self.wait()

# Problems with Groups

class MultipleAnimationVGroupFail(Scene):
    def construct(self):
        rect, circ = Rectangle(), Circle()
        vgroup = VGroup(rect, circ)

        self.add(vgroup)
        self.play(
                vgroup.arrange,DOWN,
                rect.set_height,1,
            )
        self.wait()

class MultipleAnimationVGroup(Scene):
    def construct(self):
        rect, circ = Rectangle(), Circle()
        vgroup = VGroup(rect, circ)

        def modify(vg):
            r,c = vg
            r.set_height(1)
            vg.arrange(DOWN)
            return vg

        self.add(vgroup)
        self.play(
                ApplyFunction(modify, vgroup)
            )
        self.wait()

# Problems with liniearity

"""
    def rotate(self, angle, axis=OUT, **kwargs):
"""

class RotationAnimationFail(Scene):
    def construct(self):
        square, circle = VGroup(Square(), Circle()).scale(0.3).set_y(-3)

        reference = DashedVMobject(Circle(radius=3,color=GRAY))

        self.add(square,circle,reference)
        self.play(
            square.rotate,2*PI/3,{"about_point":ORIGIN},
            Rotate(circle,2*PI/3,about_point=ORIGIN),
            run_time=4
            )
        self.wait()

class RotationAndMoveFail(Scene):
    def construct(self):
        square1, square2 = VGroup(
                Square(color=RED), Square(color=BLUE)
            ).scale(0.5).set_x(-5)

        reference = DashedVMobject(Line(LEFT*5,RIGHT*5,color=GRAY))
        self.add(square1,square2,reference)

        square2.save_state()
        def update_rotate_move(mob,alpha):
            square2.restore()
            square2.shift(RIGHT*10*alpha)
            square2.rotate(3*PI*alpha)

        self.play(
                square1.rotate,3*PI,
                square1.move_to, [5,0,0],
                UpdateFromAlphaFunc(square2,update_rotate_move),
                run_time=4
            )
        
class RotateWithPath(Scene):
    def construct(self):
        square1, square2 = VGroup(
                Square(color=RED), Square(color=BLUE)
            ).scale(0.5).set_x(-5)

        path = Line(LEFT*5,RIGHT*5,stroke_opatity=0.5)
        path.points[1:3] += UP*2

        square2.save_state()
        def update_rotate_move(mob,alpha):
            square2.restore()
            square2.move_to(path.point_from_proportion(alpha))
            square2.rotate(3*PI*alpha)

        self.add(square1,square2,path)
        self.play(
                MoveAlongPath(square1,path),
                Rotate(square1,2*PI/3,about_point=square1.get_center()),
                UpdateFromAlphaFunc(square2,update_rotate_move),
                run_time=4
            )
        self.wait()

class MoveAlongPathWithAngle(Scene):
    def get_pendient(self,path,proportion,dx=0.01):
        if proportion < 1:
            coord_i = path.point_from_proportion(proportion)
            coord_f = path.point_from_proportion(proportion+dx)
        else:
            coord_i = path.point_from_proportion(proportion-dx)
            coord_f = path.point_from_proportion(proportion)
        line = Line(coord_i,coord_f)
        angle = line.get_angle()
        return angle

    def construct(self):
        path = Line(LEFT*5,RIGHT*5,stroke_opatity=0.5)
        path.points[1:3] += UP*2
        start_angle = self.get_pendient(path,0)

        triangle = Triangle().set_height(0.5)
        triangle.move_to(path.get_start())
        triangle.rotate(-PI/2)
        triangle.save_state()
        triangle.rotate(start_angle,about_point=triangle.get_center())


        def update_rotate_move(mob,alpha):
            triangle.restore()
            angle = self.get_pendient(path,alpha)
            triangle.move_to(path.point_from_proportion(alpha))
            triangle.rotate(angle,about_point=triangle.get_center())

        self.add(triangle,path)
        self.play(
                UpdateFromAlphaFunc(triangle,update_rotate_move),
                run_time=4
            )
        self.wait()
