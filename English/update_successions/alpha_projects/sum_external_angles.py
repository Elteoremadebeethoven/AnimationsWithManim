from manimlib.imports import *

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

    def get_polygon_external_sides(self):
        return self[0]

    def get_polygon_external_angles(self):
        return self[1]

    def get_regular_polygon(self):
        return self[2]

class SumExternalAngles(Scene):
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
        regular_polygons = VGroup(*[
            figure.get_regular_polygon()
            for figure in figures
        ])
        external_sides = VGroup(*[
            figure.get_polygon_external_sides()
            for figure in figures
        ])
        external_angles = VGroup(*[
            figure.get_polygon_external_angles()
            for figure in figures
        ])
        self.play(LaggedStartMap(GrowFromCenter,regular_polygons),run_time=2)
        self.play(*list(map(ShowCreation,external_sides)))
        self.play(*list(map(ShowCreation,external_angles)))
        self.wait()
        self.play(
            UpdateFromAlphaFunc(figures,shrink_polygon),
            run_time = 8,
            rate_func = there_and_back
        )
        self.wait(3)