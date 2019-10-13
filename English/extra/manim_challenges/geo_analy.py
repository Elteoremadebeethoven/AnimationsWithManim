old_version = False

if old_version:
    from big_ol_pile_of_manim_imports import *
else:
    from manimlib.imports import *

class Dot(Dot):
    CONFIG = {
        "fill_color": BLUE,
        "fill_opacity": 1,
        "stroke_color": RED,
        "stroke_width": 1.7,
    }
    
class ParabolaCreation(GraphScene):
    CONFIG = {
        "x_min": -6,
        "x_max": 6,
        "x_axis_width": 12,
        "y_axis_height": 7,
        "graph_origin": 3.5 * DOWN,
        "y_min": 0,
        "y_max": 7,
    }
    def construct(self):
        self.setup_axes()
        self.x_axis.remove(self.x_axis[1])
        self.y_axis.remove(self.y_axis[1])
        self.play(Write(self.axes))

        h = 0; k = 1; p = 1
        parabola_function = lambda x: ((x-h)**2)/(4*p) + k

        parabola_right = self.get_graph(
                parabola_function,
                x_min = 0,
                x_max = 5,
                color = BLUE
            ).set_stroke(None,3)
        

        parabola_left = self.get_graph(
                parabola_function,
                x_min = 0,
                x_max = -5,
                color = BLUE
            ).set_stroke(None,3)
        anim_kwargs = {"run_time":5,"rate_func":linear}
        self.move_dot_path(parabola_right,anim_kwargs)
        self.move_dot_path(parabola_left,anim_kwargs)

    def move_dot_path(self,parabola,anim_kwargs):
        h = 0; k = 1; p = 1
        parabola_copy = parabola.copy()
        focus = Dot(self.coords_to_point(0,2))
        dot_guide = Dot(self.coords_to_point(h,p))
        dot_d = Dot(self.coords_to_point(0,0))
        circle = Circle(radius=1).move_to(self.coords_to_point(h,p))
        line_f_d = DashedLine(focus.get_center(),dot_guide.get_center())
        line_d_d = DashedLine(dot_guide.get_center(),dot_d.get_center())


        group = VGroup(circle,line_f_d,line_d_d,dot_d)

        def update_group(group):
            c,f_d,d_d,d = group
            d.move_to(self.coords_to_point(dot_guide.get_center()[0],0))
            radius = get_norm(focus.get_center() - dot_guide.get_center())
            new_c = Circle(radius = radius)
            new_c.move_to(dot_guide)
            c.become(new_c)
            f_d.become(DashedLine(focus.get_center(),dot_guide.get_center()))
            d_d.become(DashedLine(dot_guide.get_center(),dot_d.get_center()))

        group.add_updater(update_group)

        self.play(*[
            GrowFromCenter(mob) for mob in [circle,line_f_d,line_d_d,dot_guide,dot_d,focus]
            ])
        self.add(
            group,
            focus,
            dot_guide,
            )
        self.wait()
        self.play(
            ShowCreation(parabola),
            MoveAlongPath(dot_guide,parabola_copy),
            **anim_kwargs
            )
        group.clear_updaters()
        self.wait(1.2)
        self.play(FadeOut(VGroup(group,dot_guide,focus)))
