from manimlib.imports import *

# Contents
# ========
# Abstract scenes :      Line 
# New Classes (objects): Line
# alpha examples :       Line
# dt examples :          Line

r"""
    _    _         _                  _     ____                           
   / \  | |__  ___| |_ _ __ __ _  ___| |_  / ___|  ___ ___ _ __   ___  ___ 
  / _ \ | '_ \/ __| __| '__/ _` |/ __| __| \___ \ / __/ _ \ '_ \ / _ \/ __|
 / ___ \| |_) \__ \ |_| | | (_| | (__| |_   ___) | (_|  __/ | | |  __/\__ \
/_/   \_\_.__/|___/\__|_|  \__,_|\___|\__| |____/ \___\___|_| |_|\___||___/
"""

class ExampleScene(Scene):
    CONFIG = {
        "title_config": {
            "edge": DL,
            "buff": 0.3,
            "height": 0.6,
            "color": GRAY,
            "fade": 0.7,
            "extra_str": ""
        }
    }
    def setup(self):
        title_str = self.__class__.__name__
        ex_str = self.title_config["extra_str"]
        title = TextMobject(f"\\tt {title_str}{ex_str}",color=self.title_config["color"])
        title.set_height(self.title_config["height"])
        title.fade(self.title_config["fade"])
        if get_norm(self.title_config["edge"]) > 1:
            title.to_corner(self.title_config["edge"],buff=self.title_config["buff"])
        else:
            title.to_edge(self.title_config["edge"],buff=self.title_config["buff"])
        self.add(title)

r"""
 _   _                  ____ _                         
| \ | | _____      __  / ___| | __ _ ___ ___  ___  ___ 
|  \| |/ _ \ \ /\ / / | |   | |/ _` / __/ __|/ _ \/ __|
| |\  |  __/\ V  V /  | |___| | (_| \__ \__ \  __/\__ \
|_| \_|\___| \_/\_/    \____|_|\__,_|___/___/\___||___/
"""

class NewRegularPolygon(RegularPolygon):
    def get_sides(self,**kwargs):
        vertices = [*self.get_vertices(), self.get_vertices()[0]]
        sides = VGroup(*[
                Line(vertices[i],vertices[i+1],**kwargs)
                for i in range(len(vertices)-1)
            ])
        return sides

    def get_external_sides(self,size=1,**kwargs):
        sides = self.get_sides()
        external_sides = VGroup()
        kwargs["stroke_width"] = self.get_stroke_width()
        for side in sides:
            unit_vector = side.get_unit_vector()
            start = side.get_end()
            line = Line(
                    start,
                    start + size * unit_vector,
                    **kwargs   
                )
            external_sides.add(line)
        return external_sides

    def get_external_angles(self,radius=0.7,**kwargs):
        external_sides = self.get_external_sides()
        sides = self.get_sides()
        ind = -1 if self.start_angle == 0 else 1
        angle = abs(external_sides[0].get_angle() - sides[ind].get_angle())
        arcs = VGroup(*[
            Arc(
                sides[n].get_angle(),
                angle,
                radius=radius,
                arc_center=external_sides[n].get_start(),
                **kwargs
            ) for n in range(len(sides))
        ])
        return arcs

class GroupRegularPolygon(VGroup):
    CONFIG = {
        "polygon_color": RED,
        "ext_side_color": BLUE,
        "ext_angle_color": TEAL
    }
    def __init__(self,n,size=1,radius=0.7,height=2,**kwargs):
        regular_polygon = NewRegularPolygon(n,**kwargs)
        regular_polygon.set_height(height)
        super().__init__(
            regular_polygon.get_external_sides(**kwargs),
            regular_polygon.get_external_angles(**kwargs),
            regular_polygon
        )
        self[0].set_color(self.ext_side_color)
        self[1].set_color(self.ext_angle_color)
        self[2].set_color(self.polygon_color)
        self.regular_polygon = regular_polygon

    def get_number_sides(self):
        return len(self.regular_polygon.get_sides())

    def get_figure_height(self):
        return self.regular_polygon.get_height()

class Ball(Circle):
    CONFIG = {
        "radius": 0.4,
        "fill_color": BLUE,
        "fill_opacity": 1,
        "color": BLUE
    }

    def __init__(self, ** kwargs):
        Circle.__init__(self, ** kwargs)
        self.velocity = np.array((2, 0, 0))

    def get_top(self):
        return self.get_center()[1] + self.radius

    def get_bottom(self):
        return self.get_center()[1] - self.radius

    def get_right_edge(self):
        return self.get_center()[0] + self.radius

    def get_left_edge(self):
        return self.get_center()[0] - self.radius

class Box(Rectangle):
    CONFIG = {
        "height": 6,
        "width": FRAME_WIDTH - 2,
        "color": GREEN_C
    }

    def __init__(self, ** kwargs):
        Rectangle.__init__(self, ** kwargs)  # Edges
        self.top = 0.5 * self.height
        self.bottom = -0.5 * self.height
        self.right_edge = 0.5 * self.width
        self.left_edge = -0.5 * self.width


r"""
       _       _           
  __ _| |_ __ | |__   __ _ 
 / _` | | '_ \| '_ \ / _` |
| (_| | | |_) | | | | (_| |
 \__,_|_| .__/|_| |_|\__,_|
        |_|                
"""

class SumExternalAngles(ExampleScene):
    CONFIG = {
        "polygon_sides": [3,5,6,7,4],
        "init_buff": 0.6
    }
    def construct(self):
        figures = VGroup(*[GroupRegularPolygon(n) for n in self.polygon_sides])
        for figure in figures:
            figure.save_state()
            figure.height = figure.get_figure_height()

        def shrink_polygon(vgroup,alpha):
            buff = interpolate(self.init_buff,2,alpha)
            for mob in vgroup:
                mob.restore()
                d_height = interpolate(mob.height,0.0001,alpha)
                mob.become(
                    GroupRegularPolygon(
                            mob.get_number_sides(),
                            height = d_height
                        )
                )
            vgroup.arrange(RIGHT,buff=buff)
            vgroup.set_width(FRAME_WIDTH-0.2)

        shrink_polygon(figures,0)
        self.play(LaggedStartMap(GrowFromCenter,figures))
        self.wait()
        self.play(
            UpdateFromAlphaFunc(figures,shrink_polygon),
            run_time = 6,
            rate_func = there_and_back_with_pause
        )
        self.wait()

r"""
     _ _ 
  __| | |_ 
 / _` | __|
| (_| | |_ 
 \__,_|\__|
"""

class BouncingBall(ExampleScene):
    CONFIG = {
        "bouncing_time": 5,
        "title_config":{
            "extra_str": "\\it\\  - by EulerTour",
            "buff": 0.2
        }
    }
    def construct(self):
        box = Box()
        ball = Ball()
        self.play(FadeIn(box))
        self.play(FadeIn(ball))

        def update_ball(ball,dt):
            ball.acceleration = np.array((0, -5, 0))
            ball.velocity = ball.velocity + ball.acceleration * dt
            ball.shift(ball.velocity * dt)  # Bounce off ground and roof
            if ball.get_bottom() <= box.bottom*0.96 or \
                    ball.get_top() >= box.top*0.96:
                ball.velocity[1] = -ball.velocity[1]
            # Bounce off walls
            if ball.get_left_edge() <= box.left_edge or \
                    ball.get_right_edge() >= box.right_edge:
                ball.velocity[0] = -ball.velocity[0]

        ball.add_updater(update_ball)
        self.add(ball)

        self.wait(self.bouncing_time)

# Official code: https://github.com/TheRookieNerd/ManimMiniProjects/blob/master/ThreePhase.py
class ThreePhase(ExampleScene):
    CONFIG = {
        "radians": 0,
        "theta_2": 120 * DEGREES,
        "theta_3": 240 * DEGREES,
        "displacement": 4 * LEFT,
        "amp": 2,
        "t_offset": 0,
        "rate": 0.05,
        "x_min": -4,  # xmin and max are to define the bounds of the horizontal graph
        "x_max": 9,
        "color_1": RED,
        "color_2": YELLOW,
        "color_3": BLUE,

        "axes_config": {
            "x_min": 0,
            "x_max": 10,
            "x_axis_config": {
                "stroke_width": 2,
            },
            "y_min": -2.5,
            "y_max": 2.5,
            "y_axis_config": {
                "tick_frequency": 0.25,
                "unit_size": 1.5,
                "include_tip": False,
                "stroke_width": 2,
            },
        },
        "complex_plane_config": {
            "axis_config": {
                "unit_size": 2
            }
        },
        "title_config": {
            "extra_str": "\\it\\  - by The Rookie Nerd",
            "buff": 0.2,
        }
    }

    def construct(self):
        phase = self.rate
        t_tracker = ValueTracker(0)
        t_tracker.add_updater(lambda t, dt: t.increment_value(dt))
        get_t = t_tracker.get_value

        def get_horizontally_moving_tracing(Vector, color, stroke_width=3, rate=0.25):
            path = VMobject()
            path.set_stroke(color, stroke_width)
            path.start_new_path(np.array([self.displacement[0], Vector.get_end()[1], 0]))
            path.Vector = Vector

            def update_path(p, dt):
                p.shift(rate * dt * 3 * RIGHT)
                p.add_smooth_curve_to(np.array([self.displacement[0], p.Vector.get_end()[1], 0]))
            path.add_updater(update_path)
            return path
        colorcircle = interpolate_color(BLACK, GREY, .5)
        circle = Circle(radius=2, stroke_width=1, color=colorcircle)

        axis = Axes(x_min=-2.5, x_max=10, y_min=-3, y_max=3, stroke_width=2, include_tip=False).shift(self.displacement)
        text = TextMobject("Real").move_to(6.5 * RIGHT)
        text1 = TextMobject("Img").move_to(4 * LEFT + 3.25 * UP)
        phase1 = Vector(2 * RIGHT, color=self.color_1)
        phase1.shift(self.displacement)

        phase2 = Vector(2 * RIGHT, color=self.color_2)
        phase2.shift(self.displacement)

        phase3 = Vector(2 * RIGHT, color=self.color_3)
        phase3.shift(self.displacement)

        subphase1 = DashedLine(phase1.get_end(), np.array([self.displacement[0], phase1.get_end()[1], 0]), color=self.color_1)
        subphase2 = DashedLine(phase2.get_end(), np.array([self.displacement[0], phase2.get_end()[1], 0]), color=self.color_2)
        subphase3 = DashedLine(phase3.get_end(), np.array([self.displacement[0], phase3.get_end()[1], 0]), color=self.color_3)
        circle.move_to(self.displacement)
        self.play(Write(axis), Write(text), Write(text1))
        self.play(ShowCreation(circle))

        phase1.add_updater(lambda t: t.set_angle(get_t()))
        phase2.add_updater(lambda t: t.set_angle(get_t() + 120 * DEGREES))
        phase3.add_updater(lambda t: t.set_angle(get_t() + 240 * DEGREES))

        subphase1.add_updater(lambda t: t.put_start_and_end_on(phase1.get_end(), np.array([self.displacement[0], phase1.get_end()[1], 0])))
        subphase2.add_updater(lambda t: t.put_start_and_end_on(phase2.get_end(), np.array([self.displacement[0], phase2.get_end()[1], 0])))
        subphase3.add_updater(lambda t: t.put_start_and_end_on(phase3.get_end(), np.array([self.displacement[0], phase3.get_end()[1], 0])))

        self.play(
            GrowArrow(phase1,)
        )
        self.play(
            ShowCreation(subphase1,)
        )
        self.add(phase1, subphase1)
        self.add(
            t_tracker,
        )
        traced_path1 = get_horizontally_moving_tracing(phase1, self.color_1)
        self.add(
            traced_path1,
        )
        self.wait(2 * 2 * PI)

        traced_path1.suspend_updating()
        t_tracker.suspend_updating()

        self.play(
            GrowArrow(phase2,)
        )
        arc1 = Arc(0, phase2.get_angle(), radius=.5, arc_center=self.displacement, color=YELLOW)
        label1 = TexMobject("120 ^\\circ").move_to(arc1.get_center() + .3 * UP + .5 * RIGHT).scale(.5)
        grp1 = VGroup(arc1, label1)
        self.play(ShowCreation(arc1),Write(label1))
        self.wait()
        self.play(FadeOut(grp1))

        self.play(
            FadeIn(subphase2, )
        )
        t_tracker.resume_updating()
        traced_path1.resume_updating()

        traced_path2 = get_horizontally_moving_tracing(phase2, self.color_2)
        self.add(
            traced_path2,
        )
        self.wait(2 * PI)
        traced_path2.suspend_updating()
        traced_path1.suspend_updating()
        t_tracker.suspend_updating()
        self.play(
            GrowArrow(phase3,)
        )
        self.play(
            FadeIn(subphase3,)
        )

        arc2 = Arc(0, 240 * DEGREES, radius=.85, arc_center=phase1.points[0], color=BLUE)
        label2 = TexMobject("240 ^\\circ").move_to(arc2.get_center() + .4 * DOWN + .5 * RIGHT)
        grp2 = VGroup(arc2, label2).scale(.5)
        self.play(ShowCreation(arc2), Write(label2), run_time=2)
        self.wait()
        self.play(FadeOut(grp2))

        t_tracker.resume_updating()
        traced_path1.resume_updating()
        traced_path2.resume_updating()

        traced_path3 = get_horizontally_moving_tracing(phase3, self.color_3)
        self.add(
            traced_path3,
        )

        self.wait(15)

class Oscillator(ExampleScene):
    CONFIG={
        "amp":2.3,
        "t_offset":0,
        "rate":0.05,
        "x_min":4,
        "x_max":9,
        "wait_time":5,
        "color_1":RED,
        "color_2":GREEN,
    }
 
    def construct(self):
        rate_no_updater=self.rate
        def update_curve(c, dt):
            other_mob = FunctionGraph(
                lambda x: self.amp*np.sin((x - (self.t_offset + self.rate)+rate_no_updater)),
                    x_min=0,x_max=self.x_max
                ).shift(LEFT*self.x_min)
            c.become(other_mob)
            self.t_offset += self.rate
       
        c = FunctionGraph(
            lambda x: self.amp*np.sin((x- (self.t_offset + self.rate)+rate_no_updater)),
            x_min=0,x_max=self.x_max
            ).shift(LEFT*self.x_min)
 
        point=Dot()
        point.move_to(c.points[0])
        point_center=Dot()
        circle=Circle(radius=self.amp)\
               .shift(RIGHT*point.get_center()[0])
        point_center.move_to(circle.get_center())
 
        la=Line(
            circle.get_center(),
            circle.get_center()+RIGHT*self.amp/2,
            color=self.color_1
            )
        lb=DashedLine(
            circle.get_center(),
            circle.get_center()+RIGHT*self.amp/2,
            color=self.color_2
            ).rotate(PI)
        lc=Line(
            circle.get_center(),
            circle.get_center()+LEFT*self.amp/2,
            color=self.color_1
            )
        ld=DashedLine(
            circle.get_center(),
            circle.get_center()+LEFT*self.amp/2,
            color=self.color_2
            ).rotate(PI)
        def update_la(la,dt):
            a=point.get_center()[1]
            b=la.get_length()
            alpha_la=4*np.arctan((2*b-np.sqrt(4*(b**2)-a**2))/(a+0.00001))
            beta_la=PI/2-alpha_la/2
            ap=PI-alpha_la/2
            bp=PI/2-beta_la
 
            la.set_angle(bp)
        def update_lc(lc,dt):
            a=point.get_center()[1]
            b=lc.get_length()
            alpha_lc=4*np.arctan((2*b-np.sqrt(4*(b**2)-a**2))/(a+0.00001))
            beta_lc=PI/2-alpha_lc/2
            ap=PI-alpha_lc/2
            bp=PI/2-beta_lc
 
            lc.set_angle(bp+2*beta_lc)
 
 
        self.play(  ShowCreation(c),
                    ShowCreation(point),
                    ShowCreation(circle),
                    ShowCreation(la),
                    ShowCreation(lb),
                    ShowCreation(lc),
                    ShowCreation(ld),
                )
        self.wait()
 
        la.add_updater(update_la)
        lc.add_updater(update_lc)
        point.add_updater(lambda m: m.move_to(c.points[0]))
        lb.add_updater(lambda m: m.put_start_and_end_on(la.points[-1],point.get_center()))
        ld.add_updater(lambda m: m.put_start_and_end_on(lc.points[-1],point.get_center()))
        c.add_updater(update_curve)
        self.add(c,point,la,lb,lc,ld)
 
        self.wait(self.wait_time)
        c.remove_updater(update_curve)
 
        self.wait()
