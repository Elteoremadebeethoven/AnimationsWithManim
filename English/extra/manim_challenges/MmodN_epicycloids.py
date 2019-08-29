old_version = True

if old_version:
    from big_ol_pile_of_manim_imports import *
else:
    from manimlib.imports import *

class SimpleMmodN(Scene):
    def construct(self):
        circle,lines = self.get_m_mod_n_objects(3,60)
        self.play(FadeIn(VGroup(circle,lines)))

    def get_m_mod_n_objects(self,x,y):
        circle = Circle().set_height(FRAME_HEIGHT)
        circle.scale(0.85)
        lines = VGroup()
        for i in range(y):
            start_point = circle.point_from_proportion((i%y)/y)
            end_point = circle.point_from_proportion(((i*x)%y)/y)
            line = Line(start_point,end_point).set_stroke(width=1)
            lines.add(line)
        return [circle,lines]

class MmodN(SimpleMmodN):
    def construct(self):
        circle = Circle().set_height(FRAME_HEIGHT)
        circle.scale(0.85)
        circle.to_edge(RIGHT,buff=1)
        self.play(ShowCreation(circle))
        for x,y in [(2,100),(3,60),(4,60),(5,70)]:
            self.Example3b1b(self.get_m_mod_n_objects(x,y),x,y)
        self.play(FadeOut(circle))
       
    def Example3b1b(self,obj,x,y):
        circle,lines = obj
        lines.set_stroke(width=1)
        label = TexMobject(f"f({x},{y})").scale(2.5).to_edge(LEFT,buff=1)
        VGroup(circle,lines).to_edge(RIGHT,buff=1)
        self.play(
                Write(label),
                self.LaggedStartLines(lines)
            )
        self.wait()
        lines_c = lines.copy()
        lines_c.set_color(PINK)
        lines_c.set_stroke(width=3)
        self.play(
                self.LaggedStartShowCrationThenDestructionLines(lines_c)
                )
        self.wait()
        self.play(FadeOut(lines),Write(label,rate_func=lambda t: smooth(1-t)))

    def LaggedStartLines(self,lines):
        if old_version:
            return LaggedStart(
                    ShowCreation,lines,
                    run_time=4
                )
        else:
            return LaggedStartMap(
                    ShowCreation,lines,
                    run_time=4
                )

    def LaggedStartShowCrationThenDestructionLines(self,lines):
        if old_version:
            return LaggedStart(
                    ShowCreationThenDestruction,lines,
                    run_time=6
                )
        else:
            return LaggedStartMap(
                    ShowCreationThenDestruction,lines,
                    run_time=6
                )
