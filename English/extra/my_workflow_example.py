from manimlib.imports import *

# 1. Draw square and draw triangles.
# 2. Move square and triangles to the left side.
# 3. Draw the right square.
# 4. Perform the transformation of the squares.
# 5. Draw sub squares and show the formulas in the squares.
# 6. Move the formulas in the squares and put them together forming the theorem on the bottom side of the screen.

DEFAULT_STROKE_WIDTH = 2
TRIANGLE_SIDE_PROPORTION = 0.80
BIG_SQUARE_SIDE_LENGTH = 4
DEFAULT_OPACITY = 0.4

BIG_SQUARE_CONFIG = {
    "side_length": BIG_SQUARE_SIDE_LENGTH,
    "color": WHITE,
    "stroke_width": DEFAULT_STROKE_WIDTH
}
SMALL_SQUARE_CONFIG = {
    "color": ORANGE,
    "fill_opacity": 0,
    "stroke_opacity": 0,
    "stroke_width": DEFAULT_STROKE_WIDTH
}
TRIANGLE_CONFIG = {
    "color": YELLOW,
    "fill_opacity": DEFAULT_OPACITY,
    "stroke_width": DEFAULT_STROKE_WIDTH
}


# Left group
class PythagoreanGroupOneSquare(VGroup):
    CONFIG = {
        "triangle_side_proportion": TRIANGLE_SIDE_PROPORTION,
        "big_square_kwargs": BIG_SQUARE_CONFIG, #or square_config
        "hip_square_kwargs": SMALL_SQUARE_CONFIG,
        "triangle_kwargs": TRIANGLE_CONFIG,
    }

    def __init__(self,**kwargs):
        digest_config(self, kwargs)
        super().__init__(**kwargs)
        self.big_square = Square(**self.big_square_kwargs)
        self.alpha_1 = TRIANGLE_SIDE_PROPORTION / 4
        self.proportion_points = self.get_proportion_points()
        self.triangles = self.get_triangles()
        self.hip_square = self.get_hip_square()
        self.add(
            self.big_square,
            self.triangles,
            self.hip_square
        )

    def get_proportion_points(self):
        alpha_1 = self.alpha_1
        return [(i * 0.25) + alpha_1 for i in range(4)]

    def get_triangles(self):
        bs = self.big_square
        pp = self.proportion_points
        return VGroup(*[
            Polygon(
                bs.point_from_proportion(pp[i % 4]),
                bs.point_from_proportion((i + 1) * 0.25),
                bs.point_from_proportion(pp[(i + 1) % 4]),
                **self.triangle_kwargs
            )
            for i in range(4)
        ])

    def get_hip_square(self):
        bs = self.big_square
        pp = self.proportion_points
        return Polygon(*[
                bs.point_from_proportion(point)
                for point in pp
            ],
            **self.hip_square_kwargs
        )


# Right group
class PythagoreanGroupTwoSquares(PythagoreanGroupOneSquare):
    CONFIG = {
        "small_squares_kwargs": SMALL_SQUARE_CONFIG
    }

    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.big_square = Square(**self.big_square_kwargs)
        self.alpha_1 = TRIANGLE_SIDE_PROPORTION / 4
        self.proportion_points = self.get_proportion_points()
        self.inside_point = np.array([
            self.big_square.point_from_proportion(self.proportion_points[0])[0],  # X coord
            self.big_square.point_from_proportion(self.proportion_points[-1])[1], # Y coord
            0
        ])
        self.triangles    = self.get_triangles()
        self.med_square   = self.get_med_square()
        self.small_square = self.get_small_square()
        self.add(
            self.big_square,
            self.triangles,
            self.med_square,
            self.small_square
        )

    def get_proportion_points(self):
        alpha_1 = self.alpha_1
        return [
            0.25 - alpha_1,
            0.25 + alpha_1,
            0.5  + alpha_1,
            1    - alpha_1
        ]

    def get_triangles(self):
        bs = self.big_square
        pp = self.proportion_points
        ip = self.inside_point
        self.triangle_kwargs["stroke_width"] = 0.8
        triangle_points = [
            [
                bs.point_from_proportion(0),
                bs.point_from_proportion(pp[0]),
                ip
            ], # T_1
            [
                bs.point_from_proportion(pp[1]),
                bs.point_from_proportion(0.5),
                bs.point_from_proportion(pp[2])
            ], # T_2
            [
                bs.point_from_proportion(pp[2]),
                ip,
                bs.point_from_proportion(pp[1])
            ], # T_3
            [
                ip,
                bs.point_from_proportion(pp[3]),
                bs.point_from_proportion(1)
            ] # T_4
        ]
        return VGroup(*[
            Polygon(*coords,**self.triangle_kwargs)
            for coords in triangle_points
        ])

    def get_med_square(self):
        bs = self.big_square
        med_square = Square(
            side_length = TRIANGLE_SIDE_PROPORTION * BIG_SQUARE_SIDE_LENGTH,
            **self.small_squares_kwargs
        )
        med_square.align_to(bs, UR)
        return med_square

    def get_small_square(self):
        bs = self.big_square
        small_square = Square(
            side_length = (1 - TRIANGLE_SIDE_PROPORTION) * BIG_SQUARE_SIDE_LENGTH,
            **self.small_squares_kwargs
        )
        small_square.align_to(bs, DL)
        return small_square


# Animations
class MoveAndShift(Animation):
    def __init__(self, mob, targ_coord, ang, **kwargs):
        digest_config(self, kwargs)
        self.mobject = mob
        self.distance = targ_coord - mob.get_center()
        self.ang = ang

    def interpolate_mobject(self, alpha):
        self.mobject.become(self.starting_mobject)
        self.mobject.rotate(
            self.ang * alpha,
            about_point=self.mobject.get_center()
        )
        self.mobject.shift(
            self.distance * alpha
        )


# Scene name capitalized
class Proof(Scene):
    STEP = 1

    def print_name(sub_scene):
        def _sub_scene(self):
            name = sub_scene.__name__
            name_split = ' '.join(elem.upper() for elem in name.split("_"))
            print(f"--- Subscene #{self.STEP} - {name_split}")
            sub_scene(self)
            print()
            self.STEP += 1
        return _sub_scene

    def construct(self):
        self.draw_square_with_triangles()
        self.moves_group_to_left()
        self.draw_right_square()
        self.move_the_triangles_to_right_square()
        self.show_sub_squares_and_subformulas()
        self.transform_subformulas_into_theorem()

    # SUB-SCENES
    @print_name
    def draw_square_with_triangles(self):
        self.left_group = PythagoreanGroupOneSquare()
        bs, tr, hs = self.left_group
        self.play(
            DrawBorderThenFill(VGroup(bs,tr)),
            run_time=4
        )
        self.wait()

    @print_name
    def moves_group_to_left(self):
        self.right_group = PythagoreanGroupTwoSquares()
        self.left_group.generate_target()
        VGroup(
            self.left_group.target, self.right_group
        ).arrange(RIGHT,buff=1)
        self.play(
            MoveToTarget(self.left_group)
        )
        self.wait()

    @print_name
    def draw_right_square(self):
        self.play(
            TransformFromCopy(
                self.left_group.big_square,
                self.right_group.big_square
            )
        )
        self.wait()

    @print_name
    def move_the_triangles_to_right_square(self):
        # self.play(
        #     TransformFromCopy(
        #         self.left_group.triangles,
        #         self.right_group.triangles
        #     ),
        #     run_time=4
        # )
        self.play(
            LaggedStart(*[
                MoveAndShift(
                    s_t.copy(), e_t.get_center(), angle,
                    run_time=1.7
                )
                for s_t, e_t, angle in zip(
                    self.left_group.triangles, self.right_group.triangles,
                    [0, 0, -PI/2, PI/2]
                )
            ])
        )
        self.wait()

    @print_name
    def show_sub_squares_and_subformulas(self):
        # mobs definition
        group = VGroup(
            self.left_group.hip_square,
            self.right_group.small_square,
            self.right_group.med_square,
        ).set_style(
            stroke_opacity=2,
            fill_opacity=DEFAULT_OPACITY
        )
        # formulas definition
        formulas = VGroup(*[
            TexMobject(t)[0].move_to(square)
            for t,square in zip(["c^2","a^2","b^2"], group)
        ])
        self.play(
            *list(map(DrawBorderThenFill,group))
        )
        self.wait()
        self.play(
            Write(formulas)
        )
        self.wait()
        self.formulas = formulas

    @print_name
    def transform_subformulas_into_theorem(self):
        theorem = TexMobject("c^2", "=", "a^2", "+", "b^2",color=BLUE)
        theorem.scale(1.6)
        theorem.to_edge(DOWN)
        theorem_target = VGroup(theorem[0],theorem[2],theorem[-1])
        self.play(
            Write(VGroup(theorem[1],theorem[3])),
            TransformFromCopy(self.formulas,theorem_target),
            run_time=4
        )
        self.wait(3)
