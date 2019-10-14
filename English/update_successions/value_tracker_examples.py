#from manimlib.imports import *
#from big_ol_pile_of_manim_imports import *

class FunctionTracker(Scene):
    def construct(self):
        # f(x) = x**2
        fx = lambda x: x.get_value()**2
        # ValueTrackers definition
        x_value = ValueTracker(0)
        fx_value = ValueTracker(fx(x_value))
        # DecimalNumber definition
        x_tex = DecimalNumber(x_value.get_value()).add_updater(lambda v: v.set_value(x_value.get_value()))
        fx_tex = DecimalNumber(fx_value.get_value()).add_updater(lambda v: v.set_value(fx(x_value)))
        # TeX labels definition
        x_label = TexMobject("x = ")
        fx_label = TexMobject("x^2 = ")
        # Grouping of labels and numbers
        group = VGroup(x_tex,fx_tex,x_label,fx_label).scale(2.6)
        VGroup(x_tex, fx_tex).arrange_submobjects(DOWN,buff=3)
        # Align labels and numbers
        x_label.next_to(x_tex,LEFT, buff=0.7,aligned_edge=x_label.get_bottom())
        fx_label.next_to(fx_tex,LEFT, buff=0.7,aligned_edge=fx_label.get_bottom())

        self.add(group.move_to(ORIGIN))
        self.wait(3)
        self.play(
            x_value.set_value,30,
            rate_func=linear,
            run_time=10
            )
        self.wait()
        self.play(
            x_value.set_value,0,
            rate_func=linear,
            run_time=10
            )
        self.wait(3)


class FunctionTrackerWithNumberLine(Scene):
    def construct(self):
        # f(x) = x**2
        fx = lambda x: x.get_value()**2
        # ValueTrackers definition
        x_value = ValueTracker(0)
        fx_value = ValueTracker(fx(x_value))
        # DecimalNumber definition
        x_tex = DecimalNumber(x_value.get_value()).add_updater(lambda v: v.set_value(x_value.get_value()))
        fx_tex = DecimalNumber(fx_value.get_value()).add_updater(lambda v: v.set_value(fx(x_value)))
        # TeX labels definition
        x_label = TexMobject("x = ")
        fx_label = TexMobject("x^2 = ")
        # Grouping of labels and numbers
        group = VGroup(x_tex,fx_tex,x_label,fx_label).scale(2)
        # Set the labels position
        x_label.next_to(x_tex,LEFT, buff=0.7,aligned_edge=x_label.get_bottom())
        fx_label.next_to(fx_tex,LEFT, buff=0.7,aligned_edge=fx_label.get_bottom())
        # Grouping numbers and labels
        x_group = VGroup(x_label,x_tex)
        fx_group = VGroup(fx_label,fx_tex)
        # Align labels and numbers
        VGroup(x_group, fx_group).arrange_submobjects(RIGHT,buff=2,aligned_edge=DOWN).to_edge(UP)
        # Get NumberLine,Arrow and label from x
        x_number_line_group = self.get_number_line_group(
            "x",30,0.2,step_label=10,v_tracker=x_value,tick_frequency=2
            )
        x_number_line_group.to_edge(LEFT,buff=1)
        # Get NumberLine,Arrow and label from f(x)
        fx_number_line_group = self.get_number_line_group(
            "x^2",900,0.012,step_label=100,v_tracker=fx_tex,
            tick_frequency=50
            )
        fx_number_line_group.next_to(x_number_line_group,DOWN,buff=1).to_edge(LEFT,buff=1)

        self.add(
            x_number_line_group,
            fx_number_line_group,
            group
            )
        self.wait()
        self.play(
            x_value.set_value,30,
            rate_func=linear,
            run_time=10
            )
        self.wait()
        self.play(
            x_value.set_value,0,
            rate_func=linear,
            run_time=10
            )
        self.wait(3)


    def get_numer_labels_to_numberline(self,number_line,x_max=None,x_min=0,buff=0.2,step_label=1,**tex_kwargs):
        # This method return the labels of the NumberLine
        labels = VGroup()
        x_max = number_line.x_max
        for x in range(x_min,x_max+1,step_label):
            x_label = TexMobject(f"{x}",**tex_kwargs)
            # See manimlib/mobject/number_line.py CONFIG dictionary
            x_label.next_to(number_line.number_to_point(x),DOWN,buff=buff)
            labels.add(x_label)
        return labels

    def get_number_line_group(self,label,x_max,unit_size,v_tracker,step_label=1,**number_line_config):
        # Set the Label (x,or x**2)
        number_label = TexMobject(label)
        # Set the arrow 
        arrow = Arrow(UP,DOWN,buff=0).set_height(0.5)
        # Set the number_line
        number_line = NumberLine(
            x_min=0,
            x_max=x_max,
            unit_size=unit_size,
            numbers_with_elongated_ticks=[],
            **number_line_config
            )
        # Get the labels from number_line
        labels = self.get_numer_labels_to_numberline(number_line,step_label=step_label,height=0.2)
        # Set the arrow position
        arrow.next_to(number_line.number_to_point(0),UP,buff=0)
        # Grouping arrow and number_label
        label = VGroup(arrow,number_label)
        # Set the position of number_label
        number_label.next_to(arrow,UP,buff=0.1)
        # Grouping all elements
        numer_group = VGroup(label,number_line,labels)
        # Set the updater to the arrow and number_label
        label.add_updater(lambda mob: mob.next_to(number_line.number_to_point(v_tracker.get_value()),UP,buff=0))

        return numer_group

#HSL color, see https://pypi.org/project/colour/
def HSL(hue,saturation=1,lightness=0.5):
    return Color(hsl=(hue,saturation,lightness))


# This function is come and go, but linear
def double_linear(t):
    if t < 0.5:
        return linear(t*2)
    else:
        return linear(1-(t-0.5)*2)

class ValueTrackerWithColor(Scene):
    def construct(self):
        gradient_rectangle = Rectangle(
                                    width=FRAME_WIDTH-1,
                                    height=1,
                                    fill_opacity=1,
                                    # Gradient direction
                                    sheen_direction=RIGHT,
                                    stroke_width=0
                                    )
        square = Square(fill_opacity=1)
        square.to_edge(UP,buff=1)
        gradient_rectangle.to_edge(DOWN,buff=1)

        gradient_rectangle.set_color(color=self.get_hsl_set_colors())

        color_tracker = ValueTracker(0)

        color_label = Integer(color_tracker.get_value(),unit="^\\circ")
        color_label.add_updater(lambda v: v.set_value(color_tracker.get_value()).next_to(square,UP))

        square.add_updater(lambda s: s.set_color(HSL(color_tracker.get_value()/360)))

        line_color = Line(
                        gradient_rectangle.get_corner(UL),
                        gradient_rectangle.get_corner(UR)
                        )
        arrow = Arrow(LEFT,RIGHT)
        arrow.add_updater(lambda a: a.put_start_and_end_on(square.get_bottom()+DOWN*0.3,line_color.point_from_proportion(color_tracker.get_value()/360)))

        self.add(gradient_rectangle,square,color_label,arrow)
        self.wait(3)
        self.play(
            color_tracker.set_value,360,
            rate_func=double_linear,
            run_time=20,
            )
        self.wait(3)

    def get_hsl_set_colors(self,saturation=1,lightness=0.5):
        return [*[HSL(i/360,saturation,lightness) for i in range(360)]]


class MmodNTracker(Scene):
    CONFIG = {
        "number_of_lines": 400,
        "gradient_colors":[RED,YELLOW,BLUE],
        "end_value":100,
        "total_time":180,
    }
    def construct(self):
        circle = Circle().set_height(FRAME_HEIGHT*0.9)
        mod_tracker = ValueTracker(0)
        lines = self.get_m_mod_n_objects(circle,mod_tracker.get_value())
        lines.add_updater(
            lambda mob: mob.become(
                self.get_m_mod_n_objects(circle,mod_tracker.get_value())
                )
            )
        self.add(circle,lines)
        self.wait(3)
        self.play(
            mod_tracker.set_value,self.end_value,
            rate_func=linear,
            run_time=self.total_time
            )
        self.wait(3)

    def get_m_mod_n_objects(self,circle,x,y=None):
        if y==None:
            y = self.number_of_lines
        lines = VGroup()
        for i in range(y):
            start_point = circle.point_from_proportion((i%y)/y)
            end_point = circle.point_from_proportion(((i*x)%y)/y)
            line = Line(start_point,end_point).set_stroke(width=1)
            lines.add(line)
        lines.set_color_by_gradient(*self.gradient_colors)
        return lines

