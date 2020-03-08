from manimlib.imports import *

class RegularPolygon(RegularPolygon):
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
        #kwargs["stroke_width"] = self.CONFIG["stroke_wid"]
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

class SumExternalAngles(Scene):
    def construct(self):
        triangle = RegularPolygon(3)
        pentagon = RegularPolygon(5)
        hexagon = RegularPolygon(6)
        figures = VGroup(*[figure.set_height(2.5) for figure in [triangle,pentagon,hexagon]])
        figures.arrange(RIGHT,buff=1)
        figures.set_stroke(RED,7)

        triangle_sides = hexagon.get_external_sides()

        self.add(figures,triangle_sides)
