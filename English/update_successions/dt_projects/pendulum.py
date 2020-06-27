from manimlib.imports import *

class Pendulum(VGroup):
    CONFIG = {
        "theta_max": 10 * DEGREES,
        "theta_offset": 0,
        "theta_start": None,
        "length": 5,
        "origin": ORIGIN,
        "mass_config": {
            "radius": 0.5,
            "color": RED
        },
        "line_config": {
            "color": WHITE,
            "stroke_width": 3
        }
    }
    def __init__(self,**kwargs):
        digest_config(self,kwargs)
        super().__init__(**kwargs)
        self.mass = self.get_mass()
        self.string = self.get_string()
        self.vertical_line = self.string.copy()
        self.string.save_state()
        self.string.initial_state = self.string.copy()
        if self.theta_start == None:
            self.theta_start = self.theta_max
        self.mass.add_updater(lambda mob: mob.move_to(self.string.get_end()))
        self.rotate(self.theta_start)
        self.add(self.string,self.mass)

    def get_mass(self):
        return Dot(**self.mass_config)

    def get_string(self):
        return Line(
            self.origin,
            self.origin + DOWN * self.length,
            **self.line_config
        )

    def rotate(self,angle):
        self.string.rotate(angle, about_point=self.origin)

    def restore_string(self):
        self.string.restore()
        

    def get_angle(self):
        return angle_between(self.string.get_unit_vector(), DOWN) * 180 / PI

    def add_mass_updater(self):
        self.mass.add_updater(lambda mob: mob.move_to(self.string.get_end()))


class PendulumScene(Scene):
    CONFIG = {
        "total_time": 13,
        "dt_factor": 3,
        "gravity": 9.8
    }
    def construct(self):
        dt_calculate = 1 / self.camera.frame_rate
        roof = self.get_roof()
        roof.to_edge(UP)
        pendulum = Pendulum(
            origin=roof.get_bottom()
        )
        pendulum.restore_string()
        equation = TexMobject(r"\theta = \theta_{max}\cos\left(\sqrt{\frac{g}{L}}\cdot t\right)")
        equation.to_corner(DR)
        self.play(ShowCreation(roof))
        self.play(
            AnimationGroup(
                ShowCreation(pendulum.string),
                GrowFromCenter(pendulum.mass),
                lag_ratio=1
            )
        )
        self.play(
            Rotating(
                pendulum.string,
                radians=10*DEGREES,
                about_point=pendulum.origin,
                rate_func=smooth,
                run_time=1
            )
        )
        self.wait()
        self.play(
            Write(equation)
        )
        pendulum.add_updater(self.get_theta_func(pendulum))
        self.add(pendulum)
        self.wait(self.total_time)

    def get_theta_func(self,mob):
        func = lambda t: mob.theta_max * np.cos(
            t * np.sqrt(
                ( self.gravity / mob.length )
            )
        )
        def updater_func(mob,dt):
            mob.theta_offset += dt * self.dt_factor
            new_theta = func(mob.theta_offset)
            mob.restore_string()
            mob.rotate(new_theta)
        return updater_func

    def get_roof(self,size=0.2,**line_config):
        line = Line(
            ORIGIN, UR * size, **line_config
        )
        lines = VGroup(*[
            line.copy() for _ in range(30)
        ])
        lines.arrange(RIGHT,buff=0)
        down_line = Line(
            lines.get_corner(DL),
            lines.get_corner(DR),
            **line_config
        )
        return VGroup(lines, down_line)