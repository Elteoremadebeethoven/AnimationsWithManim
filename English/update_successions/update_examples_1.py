#from big_ol_pile_of_manim_imports import *
#from manimlib.imports import *

class TangentVector(Scene):
    def construct(self):
        figure = Ellipse(color=RED).scale(2)
        dot = Dot()
        alpha = ValueTracker(0)
        vector = self.get_tangent_vector(alpha.get_value(),figure,scale=2)
        dot.add_updater(lambda m: m.move_to(vector.get_start()))
        self.play(
            ShowCreation(figure),
            GrowFromCenter(dot),
            GrowArrow(vector)
            )
        vector.add_updater(
            lambda m: m.become(
                    self.get_tangent_vector(alpha.get_value()%1,figure,scale=2)
                )
            )
        self.add(vector,dot)
        self.play(alpha.increment_value, 2, run_time=8, rate_func=linear)
        self.wait()

    def get_tangent_vector(self, proportion, curve, dx=0.001, scale=1):
        coord_i = curve.point_from_proportion(proportion)
        coord_f = curve.point_from_proportion(proportion + dx)
        reference_line = Line(coord_i,coord_f)
        unit_vector = reference_line.get_unit_vector() * scale
        vector = Arrow(coord_i, coord_i + unit_vector, buff=0)
        return vector

# TEST - Make a line tangent to the curve

class D0t(Dot):
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
            )
        

        parabola_left = self.get_graph(
                parabola_function,
                x_min = 0,
                x_max = -5,
                color = BLUE
            )
        anim_kwargs = {"run_time":5,"rate_func":linear}
        self.move_dot_path(parabola_right,anim_kwargs)
        self.move_dot_path(parabola_left,anim_kwargs)

    def move_dot_path(self,parabola,anim_kwargs):
        h = 0; k = 1; p = 1
        parabola_copy = parabola.copy()
        focus = D0t(self.coords_to_point(0,2))
        dot_guide = D0t(self.coords_to_point(h,p))
        dot_d = D0t(self.coords_to_point(0,0))
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

        self.play(
            FadeInFromLarge(circle,scale_factor=2),
            *[GrowFromCenter(mob) for mob in [line_f_d,line_d_d,dot_guide,dot_d,focus]],
            )
        self.add(
            group,
            focus,
            dot_guide,
            )
        self.wait()
        self.add(parabola)
        self.bring_to_back(parabola)
        self.bring_to_back(self.axes)
        self.play(
            MoveAlongPath(dot_guide,parabola_copy),
            ShowCreation(parabola),
            **anim_kwargs
            )
        group.clear_updaters()
        self.wait(1.2)
        self.play(FadeOut(VGroup(group,dot_guide,focus)))

class EpicycloidScene(Scene):
    def construct(self):
       radius1 = 2.4
       radius2 = radius1/3
       self.epy(radius1,radius2)

    def epy(self,r1,r2):
        # Manim circle
        c1 = Circle(radius=r1,color=BLUE)
        # Small circle
        c2 = Circle(radius=r2,color=PURPLE).rotate(PI)
        c2.next_to(c1,RIGHT,buff=0)
        c2.start = c2.copy()
        # Dot
        # .points[0] return the start path coordinate
        # .points[-1] return the end path coordinate
        dot = Dot(c2.points[0],color=RED)
        # Line
        line = Line(c2.get_center(),dot.get_center()).set_stroke(BLACK,2.5)
        # Path
        path = VMobject(color=RED)
        # Path can't have the same coord twice, so we have to dummy point
        path.set_points_as_corners([dot.get_center(),dot.get_center()+UP*0.001])
        # Path group
        path_group = VGroup(line,dot,path)
        # Alpha, from 0 to 1:
        alpha = ValueTracker(0)
        
        self.play(ShowCreation(line),ShowCreation(c1),ShowCreation(c2),GrowFromCenter(dot))

        # update function of path_group
        def update_group(group):
            l,mob,previus_path = group
            mob.move_to(c2.points[0])
            old_path = path.copy()
            # See manimlib/mobject/types/vectorized_mobject.py
            old_path.append_vectorized_mobject(Line(old_path.points[-1],mob.get_center()))
            old_path.make_smooth()
            l.put_start_and_end_on(c2.get_center(),mob.get_center())
            path.become(old_path)

        # update function of small circle
        def update_c2(c):
            c.become(c.start)
            c.rotate(TAU*alpha.get_value(),about_point=c1.get_center())
            c.rotate(TAU*(r1/r2)*alpha.get_value(),about_point=c.get_center())

        path_group.add_updater(update_group)
        c2.add_updater(update_c2)
        self.add(c2,path_group)
        self.play(
                alpha.set_value,1,
                rate_func=linear,
                run_time=6
                )
        self.wait(2)
        c2.clear_updaters()
        path_group.clear_updaters()
        self.play(FadeOut(VGroup(c1,c2,path_group)))
        
# The calculations were based on the book of:
# Design Of Machinery - Robert Norton 4th Edition - Chapter 4 - Position Analysis

class SliderCrankMechanism(Scene):
    CONFIG={
        "a":2,
        "b":-6.5,
        "c":1.7,
        "theta_in":70,
        "theta_end":70-2.5*360,
        "slider_color":RED,
        "crank_color":BLUE,
        "piston_color":GREEN,
        "anchor_color":TEAL,
        "line_stroke":10
    }
    def construct(self):
        O2 = Dot().shift(LEFT*4+DOWN*1.5)
        a  = self.a
        b  = self.b
        c  = self.c
        theta_in  = self.theta_in
        theta_end = self.theta_end
        slider_color = self.slider_color
        piston_color = self.piston_color
        radio = 0.08

        base_down=Line(LEFT*4,RIGHT*4)
        base_down.shift(0.1*DOWN)
        anchor_point = Dot(O2.get_center(),radius=radio)
        semi_circle_anchor = Dot(O2.get_center(),radius=0.2,color=self.anchor_color)
        anchor_rect = Square(side_length=0.4).set_stroke(None,0).set_fill(self.anchor_color,1).move_to(O2.get_center()+DOWN*semi_circle_anchor.get_width()/2)


        anchor_group = VGroup(semi_circle_anchor,anchor_rect)

        slider      = self.position_slider(O2.get_center(),theta_in,a,slider_color)
        theta_3     = np.arcsin((a*np.sin(theta_in*DEGREES)-c)/b)*180/PI
        piston      = self.position_piston(O2.get_center(),theta_in,theta_3,a,b,c,piston_color)
        crank       = Line(slider.get_end(),piston.get_center()).set_stroke(self.crank_color,self.line_stroke)
        point_bm    = Dot(slider.get_end(),radius=radio)
        point_mp    = Dot(crank.get_end(),radius=radio)
        grupo       = VGroup(slider,piston,crank,point_mp,point_bm)

        base_down.next_to(piston,DOWN,buff=0).shift(LEFT)
        self.play(*[FadeIn(objeto)for objeto in [anchor_group,base_down]],
                    ShowCreation(slider),DrawBorderThenFill(piston),ShowCreation(crank),
                    GrowFromCenter(point_mp),GrowFromCenter(point_bm),GrowFromCenter(anchor_point),
                    )
        self.add_foreground_mobject(anchor_point)
        alpha = ValueTracker(self.theta_in)

        def update(grupo):
            dx = alpha.get_value()
            slider       = self.position_slider(O2.get_center(),dx,self.a,self.slider_color)

            theta_3   = np.arcsin(np.sign(dx)*((self.a*np.sin(dx*DEGREES)-self.c)/self.b))

            piston      = self.position_piston(O2.get_center(),dx,theta_3*180/PI,self.a,self.b,self.c,self.piston_color)
            crank    = Line(slider.get_end(),piston.get_center()).set_stroke(self.crank_color,self.line_stroke)
            point_bm    = Dot(slider.get_end(),radius=radio)
            point_mp    = Dot(crank.get_end(),radius=radio)

            nuevo_grupo = VGroup(slider,piston,crank,point_mp,point_bm)
            grupo.become(nuevo_grupo)
            return grupo

        self.play(
            alpha.set_value,self.theta_end,
            UpdateFromFunc(grupo,update),
            run_time=8,rate_func=double_smooth)
        self.wait()

    def position_slider(self,origin,theta_2,length,color):
        end_point_x = length * np.cos(theta_2 * DEGREES)
        end_point_y = length * np.sin(theta_2 * DEGREES)
        end_point = origin + np.array([end_point_x, end_point_y, 0])
        slider = Line(origin,end_point, color=color).set_stroke(None,self.line_stroke)
        return slider

    def position_piston(self,origin,theta_2,theta_3,a,b,c,color):
        d = a * np.cos(theta_2 * DEGREES) - b * np.cos(theta_3 * DEGREES)
        end_point = origin + RIGHT * d + UP * c
        piston = Rectangle(color=color, height=1, witdh=1.5)\
                 .set_fill(color,0.7).scale(0.7).move_to(origin+RIGHT * d + UP*c)
        return piston
    
class TriangleScene(Scene):
    def construct(self):
        circle = Circle(radius=3)
        base_line = Line(ORIGIN,RIGHT*3,color=ORANGE)
        side_1 = Line(ORIGIN,RIGHT*3,color=BLUE)
        side_2 = Line(RIGHT*3,RIGHT*3,color=PURPLE)
        sides = VGroup(side_1,side_2)
        
        def triangle_update(mob):
            side_1,side_2 = mob
            new_side_1 = Line(ORIGIN,circle.points[-1],color=BLUE)
            new_side_2 = Line(RIGHT*3,circle.points[-1],color=PURPLE)
            side_1.become(new_side_1)
            side_2.become(new_side_2)

        sides.add_updater(triangle_update)
        self.add(base_line,sides)
        self.play(ShowCreation(circle,run_time=3))

        self.wait()
