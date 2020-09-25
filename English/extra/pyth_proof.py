from manimlib.imports import *


SQUARE_CONFIG = {
    "color": WHITE,
    "side_length": 4
}

TRIANGLE_CONFIG = {
    "color": ORANGE,
    "stroke_width": 1,
    "fill_opacity": 0.7
}

class LeftGroup(VGroup):
    CONFIG = {
        "square_config": SQUARE_CONFIG,
        "triangle_config": TRIANGLE_CONFIG,
    }
    def __init__(self, alpha=0.2,**kwargs):
        super().__init__(**kwargs)
        square = self.get_square_from_config()
        triangles = self.get_triangles_from_config(square, alpha)
        self.add(square, triangles)

    def get_square_from_config(self):
        return Square(**self.square_config)

    def get_square_corners(self, square):
        return [
            square.point_from_proportion(alpha_corners)
            for alpha_corners in np.arange(0, 1, 0.25)
        ]

    def get_triangles_from_config(self, square, alpha):
        # c1, c2, c3, c4
        corners_coords = self.get_square_corners(square)
        # l = side_length
        side_length = square.side_length / 4
        # l * alpha / 4
        side_proportion = (1-alpha) * side_length / 4
        # p1, p2, p3, p4
        middle_points = [
            square.point_from_proportion((start + side_proportion)%1)
            for start in np.arange(0, 1, 0.25)
        ]
        triangle_ponts = [
            (c1, p1, p2)
            for c1, p1, p2 in zip(
                corners_coords,
                middle_points,
                [middle_points[-1],*middle_points[:-1]]
            )
        ]
        return VGroup(*[
            Polygon(*tg, **self.triangle_config)
            for tg in triangle_ponts
        ])


class RightGroup(LeftGroup):
    def get_triangles_from_config(self, square, alpha):
        left_edge = square.get_left()[0]
        down_edge = square.get_bottom()[1]
        # c1, c2, c3, c4
        c1, c2, c3, c4 = self.get_square_corners(square)
        # l = side_length
        side_length = square.side_length
        # l * alpha / 4
        x_side_proportion = alpha * side_length
        c_x = left_edge + x_side_proportion
        c_y = down_edge + x_side_proportion
        c = [c_x, c_y, 0]
        m1, m2, m3, m4 = [
            c1 + RIGHT * x_side_proportion,
            c3 + UP * x_side_proportion,
            c4 + RIGHT * x_side_proportion,
            c4 + UP * x_side_proportion
        ]
        triangle_ponts= [
            (c, p1, p2)
            for c, p1, p2 in zip(
               # t1  t2, t3, t4
                [c1, c1, c3, c],
                [c ,  c, m2, m2],
                [m4, m1, m3, m3]
            )
        ]
        return VGroup(*[
            Polygon(*tg, **self.triangle_config)
            for tg in triangle_ponts
        ])

class MoveAndRotate(Animation):
    CONFIG = {
        "run_time": 2,
    }
    def __init__(self, mob, target, angle=PI/2, **kwargs):
        digest_config(self, kwargs)
        self.mobject = mob
        self.mob_target = target
        self.angle = angle

    def interpolate_mobject(self, alpha):
        self.mobject.become(self.starting_mobject)
        self.mobject.move_to(
            Line(
                self.mobject.get_center(),
                self.mob_target.get_center()
            ).point_from_proportion(alpha)
        )
        angle = interpolate(0,self.angle,alpha)
        self.mobject.rotate(
            angle,
            about_point=self.mobject.get_center(),
        )

class PythagoreanProof(Scene):
    def setup(self):
        self.left_group = LeftGroup()
        self.right_group = RightGroup()
        
    def construct(self):
        self.show_left_group_at_center()
        self.move_left_group_to_left()
        self.show_right_rectangle()
        self.transform_triangle()

    def show_left_group_at_center(self):
        self.play(
            DrawBorderThenFill(self.left_group)
        )

    def move_left_group_to_left(self):
        self.left_group.generate_target()
        VGroup(self.left_group.target, self.right_group).arrange(RIGHT)
        self.play(
            MoveToTarget(self.left_group)
        )

    def show_right_rectangle(self):
        self.play(
            TransformFromCopy(
                self.left_group[0],
                self.right_group[0]
            )
        )

    def transform_triangle(self):
        lg, rg = self.left_group, self.right_group
        lgt = lg[1]
        rgt = rg[1]
        rt1, rt2, rt3, rt4 = rgt
        lt1, lt2, lt3, lt4 = lgt
        self.play(
            *[
                ApplyMethod(t1.copy().move_to,t2)
                for t1,t2 in [(lt2, rt2), (lt3, rt3)]
            ],
            *[
                MoveAndRotate(t1.copy(),t2,a)
                for t1,t2,a in zip(
                    [lt1, lt4],
                    [rt1, rt4],
                    [PI/2, -PI/2]
                )
            ]
        )

