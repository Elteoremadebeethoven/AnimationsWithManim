from manimlib.imports import *

class Ellipse(ParametricFunction):
    def __init__(self, a, e, **kwargs):
        digest_config(self,kwargs)
        b = np.sqrt( - ( (e ** 2) - 1 ) * ( a ** 2 ) ) 
        super().__init__(
            lambda t: np.array([
                a * np.sin(t),
                b * np.cos(t),
                0
            ]),
            t_min = 0,
            t_max = 2 * PI,
            **kwargs,
        )

def there_and_back_linear(t):
    new_t = 2 * t if t < 0.5 else 2 * (1 - t)
    return linear(new_t)

class EllipseScene(Scene):
    CONFIG = {
        "semi_major_axis": 2,        # a
        "eccentricity": 0,           # e
        "focus_config": {
            "radius": 0.1,
            "color": RED
        },
        "line_config": {
            "color": TEAL
        },
        "number_line_config": {
            "unit_size": 9, 
            "x_min": 0,
            "x_max": 1,
            "include_numbers": True,
            "numbers_to_show": np.arange(0,1.1, 0.1),
            "decimal_number_config": {
                "num_decimal_places": 1
            },
            "tick_frequency": 0.1
        },
        "dot_config": {
            "radius": 0.1,
            "color": YELLOW,
        }
    }

    def construct(self):
        # Ellipse
        a, e = self.semi_major_axis, self.eccentricity
        ellipse = Ellipse(a, e)
        # Focus
        dots = VGroup(*[
            Dot(**self.focus_config) for _ in range(2)
        ])
        # 
        dot = Dot(**self.dot_config)
        # directrix
        lines = VGroup(*[
            DashedLine(
                DOWN * FRAME_Y_RADIUS,
                UP * FRAME_Y_RADIUS,
                **self.line_config
            ) for _ in range(2)
        ])
        # number_line
        number_line = NumberLine(**self.number_line_config)
        number_line.set_x(0)
        number_line.to_edge(DOWN)
        # eccentricity
        eccentricity = TexMobject("\\varepsilon")
        eccentricity.next_to(number_line.n2p(1), RIGHT,buff=0.5)
        # add all mobs to a group
        group = VGroup(ellipse, lines, dots, dot)
        dot.move_to(number_line.n2p(0))
        number_plane = NumberPlane().fade(0.5)
        self.number_line = number_line
        self.play(
            FadeIn(number_plane),
            *list(map(GrowFromCenter, [ellipse, *dots])),
            # This is the same as:
            # GrowFromCenter(ellipse),
            # GrowFromCenter(dots[0]),
            # GrowFromCenter(dots[1])
            *list(map(Write, [number_line, eccentricity])),
            GrowFromCenter(dot)
        )
        self.add(group)
        self.play(
            UpdateFromAlphaFunc(
                group, self.get_ellipse_group(group, a, e, 1),
                run_time=20,
                rate_func=there_and_back_linear
            )
        )
        self.wait()

    def get_ellipse_group(self, mob, a, e_start, e_end):
        def updater_func(mob,alpha):
            ellipse, lines, dots, dot = mob
            e_target = interpolate(e_start, e_end, alpha)
            c_target = e_target * a
            dots[0].set_x(c_target)
            dots[1].set_x(-c_target)
            f_target = a / (e_target + 0.000001)
            lines[0].set_x(f_target)
            lines[1].set_x(-f_target)
            dot.move_to(self.number_line.n2p(e_target))
            ellipse.become(
                Ellipse(
                    a, e_target
                )
            )
        return updater_func