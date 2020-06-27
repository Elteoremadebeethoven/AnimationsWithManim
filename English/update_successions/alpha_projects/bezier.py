from manimlib.imports import *

class QuadraticBezier(Scene):
    CONFIG = {
        "bezier_points": [(6,0),(-4,3),(-6,-2)],
        "anim_kwargs": {
            "rate_func": linear,
            "run_time": 13
        },
        "bezier_lines_kwargs": {
            "color": TEAL,
            "stroke_opacity": 0.5,
            "stroke_width": 1 
        },
        "bezier_dots_style": {
            "color": "#555555",
            "fill_opacity": 0.5
        },
        "dots_radius": 0.15,
        "moving_line_style": {
            "color": BLUE,
            "stroke_width": 3
        }
    }

    def get_coords_points_and_lines(self,**kwargs):
        bezier_coords = [np.array([x,y,0]) for x,y in self.bezier_points]
        bezier_points = VGroup(*[
            Dot(c,radius=self.dots_radius,**self.bezier_dots_style) 
            for c in bezier_coords
        ])
        lines = VGroup(*[
            Line(
                bezier_coords[i],
                bezier_coords[i+1],
                **kwargs
            ) 
            for i in range(len(bezier_coords)-1)
        ])
        return bezier_coords,bezier_points,lines

    def get_update_function_to_point(self,line):
        return lambda mob,alpha: mob.move_to(line.point_from_proportion(alpha))

    def get_moving_dot(self,line,**kwargs):
        return Dot(line.get_start(),color=RED,radius=self.dots_radius,**kwargs)

    def get_update_function_to_moving_line(self,dot1,dot2,**kwargs):
        return lambda mob: mob.become( Line(dot1.get_center(),dot2.get_center(),**kwargs) )

    def get_update_function_path(self,dot,**kwargs):
        def update_function(path):
            old_path = path.copy()
            old_path.append_vectorized_mobject(
                Line(
                    old_path.points[-1],
                    dot.get_center(),
                    **kwargs
                )
            )
            old_path.make_smooth()
            path.become(old_path)

        return update_function

    def setup(self):
        bc, bp, bl = self.get_coords_points_and_lines(**self.bezier_lines_kwargs)
        moving_dots = VGroup(*[self.get_moving_dot(line) for line in bl])
        dot_funcs = [self.get_update_function_to_point(line) for line in bl]
        self.play(
            ShowCreation(VGroup(bp,bl)),
            *list(map(GrowFromCenter,moving_dots))
        )
        self.bezier_points = bp
        self.bezier_coords = bc
        self.bezier_lines = bl
        self.bezier_points_funcs = dot_funcs
        self.moving_dots = moving_dots


    def construct(self):
        dot1,dot2 = self.moving_dots
        moving_line = Line()
        moving_line_dot = Dot(radius=self.dots_radius,color=ORANGE)
        path = VMobject()
        # Moving line setup
        moving_line_update_func = self.get_update_function_to_moving_line(dot1,dot2,**self.moving_line_style)
        moving_line_update_func(moving_line)
        # Moving line update function setup
        moving_line_dot_update_func = self.get_update_function_to_point(moving_line)
        moving_line_dot_update_func(moving_line_dot,0)
        # Path setup
        # ---- Initial conditions
        path.set_points_as_corners([
            moving_line_dot.get_center(),
            moving_line_dot.get_center()+UP*0.001
        ])
        # ---- Definition
        path_update_func = self.get_update_function_path(moving_line_dot)
        path.add_updater(path_update_func)
        # Show mobs in screen
        self.play(
            *list(map(GrowFromCenter,[moving_line,moving_line_dot]))
        )
        self.add(path)

        self.play(
            *[
                UpdateFromAlphaFunc(dot,func,**self.anim_kwargs)
                for dot,func in zip(self.moving_dots,self.bezier_points_funcs)
            ],
            UpdateFromFunc(moving_line,moving_line_update_func),
            UpdateFromAlphaFunc(moving_line_dot,moving_line_dot_update_func,**self.anim_kwargs),
        )
        self.wait()
        

class CubicBezier(QuadraticBezier):
    CONFIG = {
        "bezier_points": [(6,-2),(2,1),(-3,2),(-6,-2)]
    }
    # TASK
    # See: https://upload.wikimedia.org/wikipedia/commons/d/db/B%C3%A9zier_3_big.gif
