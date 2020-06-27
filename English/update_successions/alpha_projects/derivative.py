from manimlib.imports import *

class Derivative(Scene):
    CONFIG = {
        "x_start": 3,
        "x_end": 7,
        "axes_config": {
            "center_point": [-4.5,-2.5,0],
            "x_axis_config": {
                "x_min": -1,
                "x_max": 10,
                "include_numbers": True
            },
            "y_axis_config": {
                "label_direction": UP,
                "x_min": -1,
                "x_max": 6,
                "include_numbers": True
            },
        },
        "func": lambda x: 0.1 * (x - 2) * (x - 8) * (x - 5) + 3,
        "func_config": {
            "color": RED,
            "x_min": 0.8,
            "x_max": 9,
        },
        "dot_radius": 0.1,
        "line_config": {}
    }
    def construct(self):
        axes = self.get_axes()
        func = self.get_graph(self.func,**self.func_config)
        dot_start = self.get_dot_from_x_coord(self.x_start)
        dot_end   = self.get_dot_from_x_coord(self.x_end)
        line = VMobject()
        line.add_updater(self.get_line_updater(dot_start,dot_end))
        # self.add(axes,func,dot_start,dot_end,line)
        self.play(
            Write(axes),
            ShowCreation(func),
            *list(map(GrowFromCenter,[dot_start,dot_end]))
        )
        self.play(ShowCreation(line))
        self.wait()
        self.move_dot(dot_end, self.x_end, self.x_start + 0.0001, run_time=8)
        line.clear_updaters()
        self.remove(dot_end)
        line.add_updater(self.get_derivative_updater(dot_start))
        self.add(line)
        self.wait()
        self.move_dot(
            dot_start,
            self.x_start, 8,
            run_time=18,
            rate_func=there_and_back
        )
        self.wait(3)

    def get_axes(self):
        self.axes = Axes(**self.axes_config)
        # FIX Y LABELS
        y_labels = self.axes.get_y_axis().numbers
        for label in y_labels:
            label.rotate(-PI/2)
        return self.axes

    def get_graph(self,func,**kwargs):
        return self.axes.get_graph(
                                    func,
                                    **kwargs
                                )

    def get_f(self,x_coord):
        return self.axes.c2p(x_coord, self.func(x_coord))

    def get_dot_from_x_coord(self,x_coord,**kwargs):
        return Dot(
            self.get_f(x_coord),
            radius=self.dot_radius,
            **kwargs
        )

    def get_dot_updater(self, start, end):
        def updater(mob,alpha):
            x = interpolate(start, end, alpha)
            coord = self.get_f(x)
            mob.move_to(coord)
        return updater

    def get_line_across_points(self,d1,d2,buff):
        reference_line = Line(d1.get_center(),d2.get_center())
        vector = reference_line.get_unit_vector()
        return Line(
            d1.get_center() - vector * buff,
            d2.get_center() + vector * buff,
            **self.line_config
        )

    def get_line_updater(self,d1,d2,buff=3,**kwargs):
        def updater(mob):
            mob.become(
                self.get_line_across_points(d1,d2,buff)
            )
        return updater

    def move_dot(self,dot,start,end,*args,**kwargs):
        self.play(
            UpdateFromAlphaFunc(
                dot, self.get_dot_updater(start,end),
                *args,
                **kwargs
            )
        )

    def get_derivative_updater(self, dot, length=6):
        def updater(mob):
            derivative = Line(
                dot.get_center(),
                self.get_dot_from_x_coord(
                    self.axes.p2c(dot.get_center())[0] + 0.0001
                ).get_center(),
                **self.line_config
            )
            derivative.set_length(length)
            derivative.move_to(dot)
            mob.become(derivative)
        return updater
