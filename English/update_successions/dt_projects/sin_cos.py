from manimlib.imports import *

class SinFunc(FunctionGraph):
    CONFIG = {
        "color": BLUE_E,
        "func": np.sin,
        "shift_graph": -2,
        "beta": 2,
        "amp": 1.5,
        "shift_left": -1,
        "t_offset": 0
    }
    def __init__(self, factor=1,**kwargs):
        digest_config(self,kwargs)
        func = lambda t: self.amp * self.func(self.beta * t + self.t_offset * factor) + self.shift_graph
        super().__init__(func, x_min=-(PI + PI / 4), x_max=PI ,**kwargs)
        self.shift(RIGHT * self.shift_left)

class CosFunc(SinFunc):
    CONFIG = {
        "color": RED_E,
        "func": np.cos,
        "shift_graph": 2,
    }

class SinCos(Scene):
    CONFIG = {
        "total_time": 25, # seconds
        "dt_factor": 0.4,
        "circle_config": {
            "radius": 1.5,
            "color": WHITE,
            "arc_center": [5,-2,0]
        },
        "cos_config": {
            "color": BLUE
        },
        "sin_config": {
            "color": RED
        },
        "vertical_line_config": {
            "stroke_width": 2,
            "stroke_opacity": 0.5,
            "color": TEAL
        },
        "arc_marks_config": {
            "color": GRAY,
            "stroke_width": 2,
            "stroke_opacity": 0.5
        },
        "sto": 0, # sine t offset
        "cto": 0,
        "tto": 0, # theta t offset
    }
    def construct(self):
        # Create Main Mobjects
        sine   = self.sine   = SinFunc()
        cosine = self.cosine = CosFunc()
        circle = self.circle = Circle(**self.circle_config)
        circle.next_to(sine, RIGHT, buff=0.5)
        dot_theta = self.dot_theta = self.get_dot_from_theta(circle,0)
        # guide lines
        sine_line   = self.sine_line   = self.get_sine_line()
        cosine_guide_line = self.cgl   = self.get_cosine_vertical_guide_line()
        cosine_line = self.cosine_line = self.get_cosine_line()
        # reference lines
        vertical_line   = self.vertical_line   = self.get_vertical_line()
        horizontal_line = self.horizontal_line = self.get_horizontal_line()
        # arc marks
        arc_dx = 0.5
        arc_marks = VGroup(*[
            Arc(
                radius=r,
                arc_center=[vertical_line.get_x(),0,0],
                **self.arc_marks_config
            )
            for r in np.arange(0.5, 3.5 + arc_dx, arc_dx)
        ])
        # Decimal number mobjects
        theta_tex = TexMobject("\\theta =")
        theta_tex.to_corner(UR).shift(LEFT * 1.5)
        theta_number = DecimalNumber(0,unit=r"^\circ")
        theta_number.next_to(theta_tex, RIGHT)
        theta_number.align_to(theta_tex, DOWN)
        # Write in the Screen
        self.play(
            ShowCreation(VGroup(
                vertical_line, horizontal_line
            )),
            GrowFromCenter(circle),
            GrowFromPoint(dot_theta, circle.get_center()),
            run_time=2.5
        )
        self.play(
            *list(map(ShowCreation,[
                sine,
                cosine,
                arc_marks,
                sine_line,
                VGroup(cosine_guide_line, cosine_line) # WHY this?, think about it
            ])),
            Write(VGroup(theta_tex, theta_number)),
            run_time=2.5
        )
        self.wait()
        # Add updaters, THE ORDER MATTERS
        sine.add_updater(
            self.get_updater_func("sto", SinFunc)
        )
        cosine.add_updater(
            self.get_updater_func("cto", CosFunc)
        )
        dot_theta.add_updater(
            self.get_updater_dot(circle)
        )
        sine_line.add_updater(
            lambda mob: mob.become(
                self.get_sine_line()
            )
        )
        cosine_guide_line.add_updater(
            lambda mob: mob.become(
                self.get_cosine_vertical_guide_line()
            )
        )
        cosine_line.add_updater(
            lambda mob: mob.become(
                self.get_cosine_line()
            )
        )
        theta_number.add_updater(
            lambda mob: mob.set_value(
                (self.CONFIG["tto"] % (2*PI)) * 180 / PI
            )
        )
        self.wait(self.total_time)
        # Stop animation
        for mob in [
            sine,
            cosine,
            dot_theta,
            sine_line,
            cosine_guide_line,
            cosine_line,
            theta_number,
        ]:
            mob.clear_updaters()
        self.wait(2)

    def get_updater_func(self, t, TrigFunc, **kwargs):
        def update_func(mob,dt):
            self.CONFIG[t] += dt * self.dt_factor
            mob.become(
                TrigFunc(
                    t_offset=self.CONFIG[t],
                    **kwargs
                )
            )
        return update_func

    def get_dot_from_theta(self,circle,theta,**kwargs):
        return Dot(
            circle.point_at_angle(theta),
            **kwargs
        )

    def get_updater_dot(self, circle):
        def update_func(mob,dt):
            self.CONFIG["tto"] += dt * self.dt_factor
            mob.move_to(
                circle.point_at_angle(self.CONFIG["tto"]%(2*PI))
            )
        return update_func

    def get_sine_line(self):
        return Line(
            self.sine.get_end(),
            self.dot_theta.get_left(),
            color=self.sine.get_color()
        )

    def get_cosine_line(self):
        return ArcBetweenPoints(
            self.cgl.get_end(),
            self.cosine.get_end(),
            angle=PI/2,
            color=self.cosine.get_color()
        )

    def get_vertical_line(self):
        vertical_line = Line(
                                ORIGIN,
                                RIGHT * FRAME_HEIGHT,
                                **self.vertical_line_config
        ).rotate(PI/2)
        vertical_line.set_x(self.cosine.get_end()[0])
        return vertical_line

    def get_horizontal_line(self):
        return Line(
            LEFT  * FRAME_X_RADIUS,
            RIGHT * FRAME_X_RADIUS,
            **self.vertical_line_config
        )

    def get_cosine_vertical_guide_line(self):
        return Line(
            self.dot_theta.get_top(),
            np.array([
                self.dot_theta.get_x(),
                0,
                0
            ]),
            color=self.cosine.get_color()
        )
