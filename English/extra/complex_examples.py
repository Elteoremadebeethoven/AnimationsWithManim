
from manimlib.imports import *

# INDEX:
# Mnemonics - 20
# Sin interface - 158
# Sum vectors - 662
# Angle inscr - 936
# Sine laws - 1733

class Sqrt2(VGroup):
    def __init__(self, n, **kwargs):
        super().__init__(**kwargs)
        body = TexMobject("\\frac{\\sqrt{%s}}{2}"%n)[0]
        number = body[2]
        self.top = body[:3]
        body.remove(body[2])
        self.add(body,number)

class Mnemonics(Scene):
    def construct(self):
        # MOBS DEFINITIONS ----------------------------------
        l_buff = 1.2
        left_labels = VGroup(*[
            TextMobject(t) for t in ["Radians:","Degrees:","sin","cos","tan"]
        ])
        left_labels.arrange(DOWN,buff=l_buff)
        radians_grp = VGroup(*[
            TexMobject(t) for t in ["0",*["\\frac{\\pi}{%s}"%n for n in [6,4,3,2]]]
        ])
        radians_grp.arrange(RIGHT,buff=l_buff)
        radians_grp.next_to(left_labels[0],RIGHT,buff=l_buff)
        degrees_grp = VGroup(*[
            TexMobject(f"{t}^\\circ") for t in [0,30,45,60,90]
        ])
        # TRIG PRE
        sin_vals = VGroup(*[
            Sqrt2(n) for n in range(5)
        ])
        cos_vals = sin_vals.deepcopy()
        cos_vals = cos_vals[::-1]
        tan_vals = VGroup(*[
            TexMobject("\\frac{\\sqrt{%s}}{\\sqrt{%s}}"%(n,d))[0]
            for n,d in zip(range(5),list(range(5))[::-1])
        ])
        # TRIG POST
        sin_vals_p = VGroup(*[
            TexMobject(t)[0] for t in ["0","\\frac{1}{2}","\\frac{\\sqrt{2}}{2}","\\frac{\\sqrt{3}}{2}","1"]
        ])
        cos_vals_p = VGroup(*[
            TexMobject(t)[0] for t in ["0","\\frac{1}{2}","\\frac{\\sqrt{2}}{2}","\\frac{\\sqrt{3}}{2}","1"][::-1]
        ])
        tan_vals_p = VGroup(*[
            TexMobject(t)[0] for t in ["0","\\frac{\\sqrt{3}}{3}","1","\\sqrt{3}","\\infty"]
        ])
        degrees_grp.next_to(left_labels[1],RIGHT,buff=1.2)
        all_grp = VGroup(
            left_labels,
            radians_grp,
            degrees_grp,
            sin_vals,
            cos_vals,
            tan_vals,
            sin_vals_p,
            cos_vals_p,
            tan_vals_p,
        )
        all_grp.move_to(ORIGIN)
        # - Order the values
        for i in range(len(degrees_grp)):
            for j,mob in zip(range(1,5),[degrees_grp,sin_vals,cos_vals,tan_vals]):
                mob[i].set_x(radians_grp[i].get_x())
                mob[i].set_y(left_labels[j].get_y())
            
        for i in range(len(degrees_grp)):
            for j,mob in zip(range(2,5),[sin_vals_p,cos_vals_p,tan_vals_p]):
                mob[i].set_x(radians_grp[i].get_x())
                mob[i].set_y(left_labels[j].get_y())
        v_l_buff = 0.5*UP
        h_l_buff = 0.7*RIGHT
        v_line = Line(left_labels.get_corner(UR)+v_l_buff*0.9,left_labels.get_corner(DR)-v_l_buff)
        v_line.shift(RIGHT*0.6)
        h_line = Line(all_grp.get_corner(UL)-h_l_buff,all_grp.get_corner(UR)+h_l_buff)
        h_line.set_y(v_line.get_start()[1])
        h_line_d = h_line.deepcopy().set_y(v_line.get_end()[1])
        h_lines = VGroup(h_line,h_line_d)
        for i in range(1,4):
            line = h_line.copy()
            line.set_y((left_labels[i].get_y()+left_labels[i+1].get_y())/2)
            h_lines.add(line)
        # self.add(*all_grp,v_line,h_lines)
        # ----------------------------------------------
        # ANIMATIONS -----------------------------------
        # ----------------------------------------------
        self.play(
            LaggedStart(*list(map(GrowFromCenter,[v_line,*h_lines])),run_time=2.5,lag_ratio=0),
            Write(left_labels,run_time=2.5),
            Write(radians_grp,run_time=2.5),
            Write(degrees_grp,run_time=2.5),
        )
        self.wait()
        s_grp = VGroup(*[f[0] for f in sin_vals])
        c_grp = VGroup(*[f[0] for f in cos_vals])
        s_vals = VGroup(*[f[1] for f in sin_vals])
        c_vals = VGroup(*[f[1] for f in cos_vals])[::-1]
        self.play(
            Write(s_grp),
            Write(c_grp),
            run_time=3.5
        )
        self.wait()
        self.play(Write(s_vals),run_time=4)
        self.play(Write(c_vals),run_time=4)
        self.wait()
        LAG_RATIO = 0.4
        PATH_ARC = 120*DEGREES
        self.play(
            LaggedStart(*[
                Write(tv[3])
                for tv in tan_vals
            ],lag_ratio=LAG_RATIO*3.2),
            LaggedStart(*[
                TransformFromCopy(sn,tv[:3],path_arc=PATH_ARC,run_time=3)
                for sn,tv in zip([t.top for t in sin_vals],tan_vals)
            ],lag_ratio=LAG_RATIO),
            LaggedStart(*[
                TransformFromCopy(cn,tv[4:],path_arc=PATH_ARC,run_time=3)
                for cn,tv in zip([t.top for t in cos_vals],tan_vals)
            ],lag_ratio=LAG_RATIO),
        )
        self.wait()
        LAG_RATIO = 0.4
        self.play(
            AnimationGroup(
                LaggedStart(*[
                    ReplacementTransform(sv,svp)
                    for sv,svp in zip(sin_vals,sin_vals_p)
                ],lag_ratio=LAG_RATIO),
                LaggedStart(*[
                    ReplacementTransform(sv,svp)
                    for sv,svp in zip(cos_vals,cos_vals_p)
                ],lag_ratio=LAG_RATIO),
                LaggedStart(*[
                    ReplacementTransform(sv,svp)
                    for sv,svp in zip(tan_vals,tan_vals_p)
                ],lag_ratio=LAG_RATIO),
                lag_ratio=0.8
            )
        )
        self.wait(3)
        self.play(*list(map(FadeOut,self.mobjects)))
        self.wait()
        
# ---------------------------------------------
# ---------------------------------------------
# ---------------------------------------------

class SumVectors(Scene):
    CONFIG = {
        "dot_config": {"fill_opacity": 0},
        "total_time": 35,
        "velocity": [0.01,0.038,0.02]
    }
    def construct(self):
        number_plane = NumberPlane()
        # PATHS 
        path_1 = Circle(radius=1.7).rotate(PI/4)
        path_1.add_updater(lambda mob,dt: mob.rotate(dt*0.1))
        path_2 = Square().set_width(4.5).rotate(-PI*1.2/2)
        path_2.add_updater(lambda mob,dt: mob.rotate(dt*0.1))
        path_3 = Ellipse().scale([7,6,1]).rotate(20*DEGREES)
        path_3.t_offset = 0
        # path_3.add_updater(lambda mob,dt: mob.rotate(dt*0.05))
        paths = VGroup(path_1,path_2,path_3).fade(1)
        # DOTS
        dot_1 = Dot(**self.dot_config)
        dot_1.t_offset = 0
        dot_1.add_updater(self.add_updater_path(path_1,self.velocity[0]))
        dot_2 = Dot(**self.dot_config)
        dot_2.t_offset = 0
        dot_2.add_updater(self.add_updater_path(path_2,self.velocity[1],0.15))
        dot_3 = Dot(**self.dot_config)
        dot_3.t_offset = 0
        dot_3.add_updater(self.add_updater_path(path_3,self.velocity[2],-0.2))
        # Vectors
        vec_kwargs = {
            "background_stroke_color": YELLOW,
            "background_stroke_opacity": 1,
            "background_stroke_width": 3,
        }
        vec_x_kwargs = {
            "background_stroke_color": RED_A,
            "background_stroke_opacity": 1,
            "background_stroke_width": 3,
        }
        vec_y_kwargs = {
            "background_stroke_color": PURPLE_A,
            "background_stroke_opacity": 1,
            "background_stroke_width": 3,
        }
        vec_1 = Arrow(buff=0,**vec_kwargs)
        vec_1.add_updater(lambda mob: mob.put_start_and_end_on(ORIGIN,dot_1.get_center()))
        vec_2 = Arrow(buff=0,color=BLUE,**vec_kwargs)
        vec_2.add_updater(lambda mob: mob.put_start_and_end_on(dot_1.get_center(),dot_2.get_center()))
        vec_3 = Arrow(buff=0,color=RED,**vec_kwargs)
        vec_3.add_updater(lambda mob: mob.put_start_and_end_on(dot_2.get_center(),dot_3.get_center()))
        VGroup(vec_1,vec_2,vec_3).set_style(**vec_kwargs)
        # Proy Vectors
        ST_OP = 1
        vec_1_x = Arrow(buff=0,stroke_opacity=ST_OP,fill_opacity=ST_OP,**vec_x_kwargs)
        vec_1_x.add_updater(lambda mob: mob.put_start_and_end_on(ORIGIN,[vec_1.get_end()[0],0,0]))
        vec_1_y = Arrow(buff=0,stroke_opacity=ST_OP,fill_opacity=ST_OP,**vec_y_kwargs)
        vec_1_y.add_updater(lambda mob: mob.put_start_and_end_on(ORIGIN,[0,vec_1.get_end()[1],0]))
        # -----------------
        vec_2_x = Arrow(buff=0,color=BLUE,stroke_opacity=ST_OP,fill_opacity=ST_OP,**vec_x_kwargs)
        vec_2_x.add_updater(lambda mob: mob.put_start_and_end_on(
            vec_1_x.get_end()+UP*0.1,
            [vec_2.get_end()[0],  0.1,0]
        ))
        vec_2_y = Arrow(buff=0,color=BLUE,stroke_opacity=ST_OP,fill_opacity=ST_OP,**vec_y_kwargs)
        vec_2_y.add_updater(lambda mob: mob.put_start_and_end_on(
            vec_1_y.get_end()+RIGHT*0.1,
            [0.1,vec_2.get_end()[1],0]
        ))
        # -----------------
        vec_3_x = Arrow(buff=0,color=RED,stroke_opacity=ST_OP,fill_opacity=ST_OP,**vec_x_kwargs)
        vec_3_x.add_updater(lambda mob: mob.put_start_and_end_on(
            vec_2_x.get_end()-UP*0.2,
            [vec_3.get_end()[0],-0.1,0]
        ))
        vec_3_y = Arrow(buff=0,color=RED,stroke_opacity=ST_OP,fill_opacity=ST_OP,**vec_y_kwargs)
        vec_3_y.add_updater(lambda mob: mob.put_start_and_end_on(
            vec_2_y.get_end()-RIGHT*0.2,
            [-0.1,vec_3.get_end()[1],0]
        ))
        # -----------------
        VGroup(vec_1_x,vec_1_y,vec_2_x,vec_2_y,vec_3_x,vec_3_y).fade(0.2)
        VGroup(vec_1_x,vec_2_x,vec_3_x).set_style(**vec_x_kwargs)
        VGroup(vec_1_y,vec_2_y,vec_3_y).set_style(**vec_y_kwargs)
        # Proy lines
        x_line = DashedLine()
        x_line.add_updater(lambda mob: mob.become(DashedLine(vec_3_x.get_end(),vec_3.get_end())))
        y_line = DashedLine()
        y_line.add_updater(lambda mob: mob.become(DashedLine(vec_3_y.get_end(),vec_3.get_end())))
        
        updater_grp = VGroup(
            path_1,
            path_2,
            path_3,
            dot_1,
            dot_2,
            dot_3,
            vec_1,
            vec_2,
            vec_3,
            vec_1_x,
            vec_1_y,
            vec_2_x,
            vec_2_y,
            vec_3_x,
            vec_3_y,
            x_line,
            y_line,
        )
        for mob in updater_grp:
            mob.update()
            mob.suspend_updating()
        
        self.add(
            number_plane,
            dot_1,
            dot_2,
            dot_3,
            path_1,
            path_2,
            path_3,
        )
        # -----------------------
        self.add(vec_1)
        self.play(
            GrowArrow(vec_1),
            run_time=2.2,
        )
        self.add(vec_1_x,vec_1_y)
        self.play(
            TransformFromCopy(vec_1,vec_1_x),
            TransformFromCopy(vec_1,vec_1_y),
            run_time=2.2,
        )
        # -----------------------
        self.add(vec_2)
        self.play(
            GrowArrow(vec_2),
            run_time=2.2,
        )
        self.add(vec_2_x,vec_2_y)
        self.play(
            TransformFromCopy(vec_2,vec_2_x),
            TransformFromCopy(vec_2,vec_2_y),
            run_time=2.2,
        )
        # -----------------------
        self.add(vec_3)
        self.play(
            GrowArrow(vec_3),
            run_time=2.2,
        )
        self.add(vec_3_x,vec_3_y)
        self.play(
            TransformFromCopy(vec_3,vec_3_x),
            TransformFromCopy(vec_3,vec_3_y),
            run_time=2.2,
        )
        self.wait()
        # .........................
        self.play(
            *list(map(ShowCreation,[x_line,y_line]))
        )
        self.wait()
        for mob in updater_grp:
            # mob.update()
            mob.resume_updating()
        self.wait(self.total_time)
        
    def add_updater_path(self,path,vel=1,shift=0):
        path.count = 0
        def update(mob,dt):
            if path.count == 0:
                mob.t_offset += (dt * vel + shift)
                path.count += 1
            mob.t_offset += (dt * vel)
            alpha = mob.t_offset % 1
            mob.move_to(path.point_from_proportion(alpha))
        return update
    
# -------------------------------------------
# -------------------------------------------
# -------------------------------------------

class DecimalTextNumber(VMobject):
    CONFIG = {
        "num_decimal_places": 2,
        "include_sign": False,
        "group_with_commas": True,
        "digit_to_digit_buff": 0.05,
        "show_ellipsis": False,
        "unit_type": "font", # tex or font
        "unit": None,  # Aligned to bottom unless it starts with "^"
        "unit_custom_position": lambda mob: mob.set_color(GREEN).shift(RIGHT*0.1),
        "include_background_rectangle": False,
        "edge_to_fix": LEFT,
        "unit_config": {
            "font": "Digital-7",
            "stroke_width": 0,
        },
        "number_config": {
            "font": r"Digital-7",
            "stroke_width": 0,
        }
    }

    def __init__(self, number=0, **kwargs):
        super().__init__(**kwargs)
        self.number = number
        self.initial_config = kwargs

        if isinstance(number, complex):
            formatter = self.get_complex_formatter()
        else:
            formatter = self.get_formatter()
        num_string = formatter.format(number)

        rounded_num = np.round(number, self.num_decimal_places)
        if num_string.startswith("-") and rounded_num == 0:
            if self.include_sign:
                num_string = "+" + num_string[1:]
            else:
                num_string = num_string[1:]

        self.add(*[
            Text(char,color=self.color,**self.number_config)
            for char in num_string
        ])

        # Add non-numerical bits
        if self.show_ellipsis:
            self.add(SingleStringTexMobject("\\dots"))

        if num_string.startswith("-"):
            minus = self.submobjects[0]
            minus.next_to(
                self.submobjects[1], LEFT,
                buff=self.digit_to_digit_buff
            )

        self.num_string = num_string

        if self.unit is not None:
            if self.unit_type == "font":
                self.unit_sign = Text(self.unit,**self.unit_config)
            elif self.unit_type == "tex":
                del self.unit_config["font"]
                self.unit_sign = TexMobject(self.unit,**self.unit_config)
            self.add(self.unit_sign)

        self.arrange(
            buff=self.digit_to_digit_buff,
            aligned_edge=DOWN
        )

        # Handle alignment of parts that should be aligned
        # to the bottom
        for i, c in enumerate(num_string):
            if c == "-" and len(num_string) > i + 1:
                self[i].align_to(self[i + 1], UP)
                self[i].shift(self[i+1].get_height() * DOWN / 2)
            elif c == ",":
                self[i].shift(self[i].get_height() * DOWN / 2)
        if self.unit and self.unit.startswith("^"):
            self.unit_sign.align_to(self, UP)
        #
        if self.include_background_rectangle:
            self.add_background_rectangle()
            
        self.unit_custom_position(self.unit_sign)
        # if num_string[0] == "-" or num_string[0] == "+":
        #     self[0].set_width(0.2)
        #     self[0].set_color(RED)

    def get_formatter(self, **kwargs):
        config = dict([
            (attr, getattr(self, attr))
            for attr in [
                "include_sign",
                "group_with_commas",
                "num_decimal_places",
            ]
        ])
        config.update(kwargs)
        return "".join([
            "{",
            config.get("field_name", ""),
            ":",
            "+" if config["include_sign"] else "",
            "," if config["group_with_commas"] else "",
            ".", str(config["num_decimal_places"]), "f",
            "}",
        ])

    def get_complex_formatter(self, **kwargs):
        return "".join([
            self.get_formatter(field_name="0.real"),
            self.get_formatter(field_name="0.imag", include_sign=True),
            "i"
        ])

    def set_value(self, number, **config):
        full_config = dict(self.CONFIG)
        full_config.update(self.initial_config)
        full_config.update(config)
        new_decimal = DecimalTextNumber(number, **full_config)
        # Make sure last digit has constant height
        #new_decimal.scale(
        #    self[-1].get_height() / new_decimal[-1].get_height()
        #)
        #"""
        height = new_decimal.get_height()
        yPos = new_decimal.get_center()[1]

        for nr in new_decimal:
            if "." != nr.text :
                nr.scale(height/nr.get_height())
                nr.shift([0,(yPos-nr.get_center()[1]),0])
        max_width = max(*[f.get_width() for f in new_decimal[1:]])
        if new_decimal[0].text == "-" or new_decimal[0].text == "+":
            new_decimal[0].set_width(max_width)
            new_decimal[0].set_color(RED)

        #"""
        new_decimal.move_to(self, self.edge_to_fix)
        new_decimal.match_style(self)
        old_family = self.get_family()
        self.submobjects = new_decimal.submobjects
        for mob in old_family:
            # Dumb hack...due to how scene handles families
            # of animated mobjects
            mob.points[:] = 0
        self.number = number
        # if num_string[0] == "-" or num_string[0] == "+":
        #     self[0].set_width(0.2)
        #     self[0].set_color(RED)
        return self

    def get_value(self):
        return self.number

    def increment_value(self, delta_t=1):
        self.set_value(self.get_value() + delta_t)

class ChangingDecimalText(Animation):
    CONFIG = {
        "suspend_mobject_updating": False,
    }

    def __init__(self, decimal_mob, number_update_func, **kwargs):
        self.check_validity_of_input(decimal_mob)
        self.yell_about_depricated_configuration(**kwargs)
        self.number_update_func = number_update_func
        super().__init__(decimal_mob, **kwargs)

    def check_validity_of_input(self, decimal_mob):
        if not isinstance(decimal_mob, DecimalTextNumber):
            raise Exception(
                "ChangingDecimal can only take "
                "in a DecimalNumber"
            )

    def yell_about_depricated_configuration(self, **kwargs):
        # Obviously this would optimally be removed at
        # some point.
        for attr in ["tracked_mobject", "position_update_func"]:
            if attr in kwargs:
                warnings.warn("""
                    Don't use {} for ChangingDecimal,
                    that functionality has been depricated
                    and you should use a mobject updater
                    instead
                """.format(attr)
            )

    def interpolate_mobject(self, alpha):
        self.mobject.set_value(
            self.number_update_func(alpha)
        )


class ChangeDecimalToValueText(ChangingDecimalText):
    def __init__(self, decimal_mob, target_number, **kwargs):
        start_number = decimal_mob.number
        super().__init__(
            decimal_mob,
            lambda a: interpolate(start_number, target_number, a),
            **kwargs
        )

class Grid(VGroup):
    CONFIG = {
        "height": 6.0,
        "width": 6.0,
        "line_kwargs": {}
    }

    def __init__(self, rows, columns, **kwargs):
        digest_config(self, kwargs, locals())
        self.rows = rows
        self.columns = columns
        super().__init__(**kwargs)

        x_step = self.width / self.columns
        y_step = self.height / self.rows

        for x in np.arange(0, self.width + x_step, x_step):
            self.add(DashedLine(
                [x - self.width / 2., -self.height / 2., 0],
                [x - self.width / 2., self.height / 2., 0],
                **self.line_kwargs
            ))
        for y in np.arange(0, self.height + y_step, y_step):
            self.add(DashedLine(
                [-self.width / 2., y - self.height / 2., 0],
                [self.width / 2., y - self.height / 2., 0],
                **self.line_kwargs
            ))

class SinInterface(VGroup):
    CONFIG = {
        "x_size": 16,
        "y_size": 6,
        "axes_config":{
            "x_min": -7,
            "x_max": 7,
            "y_min": -2.5,
            "y_max": 2.5,
            "axis_config": {
                "color": LIGHT_GREY,
                "include_tip": False,
                "exclude_zero_from_default_numbers": False,
                "decimal_number_config": {
                    "num_decimal_places": 1,
                },
            },
            "x_axis_config": {
                "unit_size":0.8,
            },
            "y_axis_config": {
                "label_direction": LEFT,
                "unit_size":0.8,
                # "x_min": -2.5,
                # "x_max": 2.5,
            },
            "center_point": ORIGIN,
        },
        "margin": 1,
        "x_margin": 1.2,
        "y_margin": None,
        "grid_kwargs": {
            "stroke_width": 0.5
        }
    }
    def __init__(self, **kwargs):
        digest_config(self, kwargs)
        super().__init__(**kwargs)
        if self.x_size != None:
            self.axes_config["x_max"] = self.x_size / 2
            self.axes_config["x_min"] = -self.x_size / 2
        if self.y_size != None:
            self.axes_config["y_max"] = self.y_size / 2
            self.axes_config["y_min"] = -self.y_size / 2
        axes = Axes(**self.axes_config)
        inner_margin = RoundedRectangle(
            width=axes.get_width(),
            height=axes.get_height(),
            fill_opacity=1,
            fill_color=BLACK,
            stroke_width=0,
            stroke_color=WHITE,
        )
        if self.x_margin == None:
            self.x_margin = self.margin
        if self.y_margin == None:
            self.y_margin = self.margin
        # print(self.y_margin)
        outer_margin = Rectangle(
            width=axes.get_width()+self.x_margin,
            height=axes.get_height()+self.y_margin,
            fill_opacity=1,
            fill_color="#AAAAAA",
            stroke_width=0,
            stroke_color=WHITE,
        )
        axes[0].add_numbers()
        axes[1].add_numbers()
        axes[0][-1].remove(axes[0][-1][0])
        axes[0][-1].set_y((inner_margin.get_bottom()[1]+outer_margin.get_bottom()[1])/2)
        axes[1][-1].remove(axes[1][-1][0])
        axes[1][-1].set_x((inner_margin.get_left()[0]+outer_margin.get_left()[0])/2)
        # left_side = axes[1][-1].get_right()
        # for n in axes[1][-1]:
        #     n[:].align_to(inner_margin,RIGHT)
        VGroup(axes[0][-1],axes[1][-1]).set_color(BLACK)
        for i in [*axes[0][-1],*axes[1][-1]]:
            i.scale(0.5)
        columns = self.x_size 
        rows = self.y_size
        grid = Grid(rows, columns,width=self.x_size,height=self.y_size,line_kwargs=self.grid_kwargs)
        grid.set_width(inner_margin.get_width())
        grid.move_to(inner_margin)
        self.axes = axes
        self.add(outer_margin,inner_margin,grid,axes)
        

class SinFunctionInterface(Scene):
    def construct(self):
        A_COLOR = YELLOW
        K_COLOR = RED
        W_COLOR = TEAL
        PHI_COLOR = BLUE
        X_COLOR = PURPLE
        T_COLOR = GREEN
        interface = SinInterface()
        interface.to_edge(DOWN,buff=0.2)
        axes = interface.axes
        # f(x,t) = A * sin(k*x + w*t + s)
        A = ValueTracker(1)
        k = ValueTracker(1)
        w = ValueTracker(1)
        s = ValueTracker(0)
        t = ValueTracker(0)
        graph = axes.get_graph(lambda t: np.sin(t),color=RED)
        graph.add_updater(lambda mob: mob.become(
            axes.get_graph(
                lambda x: A.get_value() * np.sin(
                    k.get_value() * x + w.get_value() * t.get_value() + s.get_value()
                ),
            color=RED)
        ))
        graph.t_offset = 0

        labels = VGroup(
            self.get_range_line(-2,2,A,"A",A_COLOR),
            self.get_range_line(-2,2,s,"\\phi",PHI_COLOR),
            self.get_range_line(-2,2,k,"k",K_COLOR),
            self.get_range_line(-2,2,w,"\\omega",W_COLOR),
        )
        max_tex_width = max(*[l[1].get_width() for l in labels])
        for l in range(len(labels)):
            line = labels[l][0]
            line.align_to(labels[l],LEFT)
            line.shift(RIGHT*max_tex_width+0.2*RIGHT)
            labels[l][-1].next_to(labels[l][0],RIGHT,0.3)

        labels.scale(0.8)
        labels.arrange(DOWN,buff=0.2,aligned_edge=LEFT)
        labels.to_edge(UP,buff=0.1)
        labels.to_edge(LEFT)
        # -----------------
        t_tex = TexMobject("t",color=T_COLOR)
        t_dig = DecimalTextNumber(0,num_decimal_places=3)
        t_dig.add_updater(lambda mob: mob.set_value(t.get_value()))
        tg = VGroup(t_tex,t_dig).arrange(RIGHT,buff=0.6)
        tg_r = Rectangle(width=tg.get_width()+0.3,height=tg.get_height()+0.3)
        tg.add(tg_r)
        tg.next_to(interface,UP)
        tg_l = Line(tg.get_corner(UL),tg.get_corner(DL))
        tg_l.next_to(t_tex,RIGHT,buff=abs(tg.get_left()-t_tex.get_left())[0])
        tg.add(tg_l)
        tg.shift(RIGHT*interface.get_width()/4)
        # -------------------
        formula = TexMobject(
            "y(x,t)=A\\ \\!{\\rm sin}(kx+\\omega t+\\phi)",
            tex_to_color_map={
                "A": A_COLOR, "k": K_COLOR, "\\omega": W_COLOR, "\\phi": PHI_COLOR,
                "x": X_COLOR, "t": T_COLOR
            },
        )
        formula.next_to(tg,UP)
        self.play(Write(interface))
        self.play(Write(labels),Write(graph))
        self.play(Write(tg),Write(formula))
        self.add(interface,graph,tg,formula,*labels)
        self.wait()
        # self.play(ChangeDecimalToValueText(t,1),run_time=2) 
        RUN_TIME = 4
        self.play(A.set_value,1.9,run_time=RUN_TIME)
        self.wait(4)
        self.play(s.set_value,0.5,run_time=RUN_TIME)
        self.wait(4)
        self.play(s.set_value,-1.5,run_time=RUN_TIME)
        self.wait(4)
        self.play(k.set_value,-0.4,run_time=RUN_TIME)
        self.wait(4)
        self.play(k.set_value,1.7,run_time=RUN_TIME)
        self.wait(4)
        self.play(Indicate(t_tex),FocusOn(t_tex.get_center()))
        self.wait(0.5)
        def update_t(mob,dt):
            graph.t_offset+= dt * 0.3
            mob.set_value(graph.t_offset)
        t.add_updater(update_t)
        self.add(t)
        self.wait(8)
        self.play(w.set_value,2,run_time=RUN_TIME)
        self.wait(7)
        self.play(w.set_value,-1.1,run_time=RUN_TIME)
        self.wait(7)
        self.play(
            A.set_value,-1.7,
            k.set_value,0.8,
            run_time=RUN_TIME,
        )
        self.wait(7)
        
        
    def get_range_line(self, 
                       start,
                       end,
                       vt,
                       tex="\\alpha",
                       color=WHITE,
                       tex_config={},
                       line_config={}
        ):
        line_config["numbers_with_elongated_ticks"] = []
        line = NumberLine(x_min=start,x_max=end,**line_config)
        tex_ = TexMobject(tex,**tex_config)
        tex_.next_to(line,LEFT)
        dot = Dot()
        dot.add_updater(lambda mob: mob.move_to(line.n2p(vt.get_value())))
        digital = DecimalTextNumber(0,num_decimal_places=3,include_sign=True)
        digital.add_updater(lambda mob: mob.set_value(vt.get_value()))
        digital.next_to(line,RIGHT)
        VGroup(line,tex_,digital).set_color(color)
        return VGroup(line,tex_,dot,digital)
    
# --------------------------------------------------------
# --------------------------------------------------------
# --------------------------------------------------------

class CircleWithAngles(VGroup):
    CONFIG = {
        "inner_line_config": {"color":PURPLE_A},
        "outer_line_config": {"color":TEAL_A},
        "inner_arc_config": {"color":PURPLE_A},
        "outer_arc_config": {"color":TEAL_A},
        "tex_1_config": {"color": TEAL_A},
        "tex_2_config": {"color": PURPLE_A},
    }
    def __init__(self, radius=3, ang1=30, ang2=130, ang3=260, small_radius=0.4, **kwargs):
        digest_config(self, kwargs)
        super().__init__(**kwargs)
        circle = Circle(radius=radius)
        vt_1 = ValueTracker(ang1)
        vt_2 = ValueTracker(ang2)
        vt_3 = ValueTracker(ang3)
        p1 = Dot(circle.point_at_angle(ang1*DEGREES))
        p2 = Dot(circle.point_at_angle(ang2*DEGREES))
        p3 = Dot(circle.point_at_angle(ang3*DEGREES))
        in_lines = VMobject(**self.inner_line_config)
        # ------------- LINES
        out_lines = VMobject(**self.outer_line_config)
        # ------------- ANGLES
        out_arc = self.get_arc_between_lines(small_radius,p1,p2,p3)
        in_arc = self.get_inner_angle(small_radius,p1,p2,p3,circle)
        # ------------- LABELS
        theta_2 = TexMobject("2\\theta",**self.tex_2_config)
        theta_1 = TexMobject("\\theta",**self.tex_1_config)
        # ------------- Equals
        theta_1_val = DecimalTextNumber(0,unit="deg",num_decimal_places=3,**self.tex_1_config)
        theta_2_val = DecimalTextNumber(0,unit="deg",num_decimal_places=3,**self.tex_2_config)
        equal = Text("= 2 * ",font="Digital-7")
        theta_eq = VGroup(theta_1_val, equal, theta_2_val)
        theta_eq_temp = VGroup(theta_1_val, equal, theta_2_val)
        theta_eq.arrange(RIGHT,buff=0.6,aligned_edge=DOWN)
        theta_2_val.shift(LEFT*max(*[f.get_width() for f in theta_2_val])*1)
        rectangle = Rectangle(width=theta_eq.get_width()+0.2,height=theta_eq.get_height()+0.2)
        rectangle.move_to(theta_eq)
        theta_eq.add(rectangle)
        # UPDATERS
        p1.add_updater(lambda mob: mob.move_to(circle.point_at_angle(vt_1.get_value()*DEGREES)))
        p2.add_updater(lambda mob: mob.move_to(circle.point_at_angle(vt_2.get_value()*DEGREES)))
        p3.add_updater(lambda mob: mob.move_to(circle.point_at_angle(vt_3.get_value()*DEGREES)))
        in_lines.add_updater(lambda mob: mob.set_points_as_corners([
            p1.get_center(),circle.get_center(),p2.get_center()
        ]))
        out_lines.add_updater(lambda mob: mob.set_points_as_corners([
            p1.get_center(),p3.get_center(),p2.get_center()
        ]))
        out_arc.add_updater(lambda mob: mob.become(self.get_arc_between_lines(small_radius,p1,p2,p3)))
        in_arc.add_updater(lambda mob: mob.become(self.get_inner_angle(small_radius,p1,p2,p3,circle)))
        theta_1.add_updater(
            lambda mob: mob.move_to(
                p3.get_center()+Line(p3.get_center(),out_arc.point_from_proportion(0.5)).get_vector()*1.7)
        )
        theta_2.add_updater(
            lambda mob: mob.move_to(
                circle.get_center()+Line(circle.get_center(),in_arc.point_from_proportion(0.5)).get_vector()*1.7)
        )
        theta_1_val.add_updater(lambda mob: mob.set_value(self.get_inner_angle(1,p1,p2,p3,circle,False)*180/PI))
        theta_2_val.add_updater(lambda mob: mob.set_value(self.get_arc_between_lines(1,p1,p2,p3,False)*180/PI))
        rectangle.max_width = rectangle.get_width()
        def rect_up(mob):
            line = Line(theta_eq_temp.get_left()+LEFT*0.2,theta_eq_temp.get_right()+RIGHT*0.2)
            if line.get_width() > mob.max_width:
                mob.max_width = line.get_width() 
            mob.set_width(mob.max_width)
            # mob.move_to(line)
            mob.align_to(theta_1_val,LEFT)
            mob.shift(LEFT*0.1)
        rectangle.add_updater(rect_up)
        # ------------- Groups
        dots = VGroup(p1,p2,p3)
        vts = Group(vt_1,vt_2,vt_3)
        self.vts = vts
        self.add(
            circle,dots,
            in_lines,out_lines,
            in_arc,out_arc,
            theta_1,theta_2,
            theta_eq,
        )

    def get_arc_between_lines(self, radius, d1, d2, center,mob=True):
        line1 = Line(center.get_center(),d1.get_center())
        line2 = Line(center.get_center(),d2.get_center())
        h = Line(center.get_center(),center.get_center()+RIGHT)
        angle = angle_between_vectors(line1.get_unit_vector(),line2.get_unit_vector())
        h1 = angle_between_vectors(h.get_unit_vector(),line1.get_unit_vector())
        h2 = angle_between_vectors(h.get_unit_vector(),line2.get_unit_vector())
        if line1.get_angle() <= line2.get_angle():
            start_angle = h1
        else:
            start_angle = h2
        arc = Arc(start_angle, angle,radius=radius,arc_center=center.get_center(),**self.outer_arc_config)
        if mob:
            return arc
        else:
            return angle
    
    def get_inner_angle(self, radius,d1,d2,out_center,in_center,mob=True):
        line1 = Line(out_center.get_center(),d1.get_center())
        line2 = Line(out_center.get_center(),d2.get_center())
        h = Line(out_center.get_center(),out_center.get_center()+RIGHT)
        angle = angle_between_vectors(line1.get_unit_vector(),line2.get_unit_vector())
        v1 = Line(in_center.get_center(),d1.get_center())
        start_angle = angle_between_vectors(h.get_unit_vector(),v1.get_unit_vector())
        arc = Arc(start_angle, angle*2,radius=radius,arc_center=in_center.get_center(),**self.inner_arc_config)
        if mob:
            return arc
        else:
            return angle*2


class ArcBetweenVectors(Arc):
    def __init__(self, radius, d1, d2, center, invert_angle=False,**kwargs):
        line1 = Line(center.get_center(),d1.get_center())
        line2 = Line(center.get_center(),d2.get_center())
        h = Line(center.get_center(),center.get_center()+RIGHT)
        angle = angle_between_vectors(line1.get_unit_vector(),line2.get_unit_vector())
        h1 = angle_between_vectors(h.get_unit_vector(),line1.get_unit_vector())
        h2 = angle_between_vectors(h.get_unit_vector(),line2.get_unit_vector())
        if line1.get_angle() <= line2.get_angle():
            start_angle = h1
        else:
            start_angle = h2
        if invert_angle:
            start_angle = -start_angle
        super().__init__(start_angle, angle,radius=radius,arc_center=center.get_center(), **kwargs)

    def get_angle(self):
        return self.angle
    
class LabelFromArc(TexMobject):
    CONFIG = {
        "distance_proportion": 1.2
    }
    def __init__(self, arc, tex_height, *tex_strings, **kwargs):
        super().__init__(*tex_strings, **kwargs)
        self.set_height(tex_height)
        center = arc.get_arc_center()
        max_size = max(self.get_width(),self.get_height()) * self.distance_proportion/ 2
        vector = Line(center,arc.point_from_proportion(0.5)).get_vector()
        end_coord = center+vector + normalize(vector)*max_size
        self.move_to(end_coord)
        

class InscribedAngle(MovingCameraScene):
    def construct(self):
        circle_grp = CircleWithAngles()
        v1, v2, v3 = circle_grp.vts
        eq = circle_grp[-1]
        circle_grp.to_edge(LEFT,buff=1)
        eq.to_edge(RIGHT,buff=1)
        for mob in circle_grp:
            mob.suspend_updating()
            mob.update()
        self.play(Write(circle_grp))
        for mob in circle_grp:
            mob.resume_updating()
        self.wait()
        self.play(v1.set_value,-10,run_time=3,rate_func=linear)
        self.wait()
        self.play(v2.set_value,225,run_time=5,rate_func=there_and_back)
        self.wait()
        self.play(
            v1.set_value,47,
            v2.set_value,110,
            v3.set_value,335,
            run_time=3,
            rate_func=there_and_back
        )
        self.wait()
        circle_grp.remove(eq)
        self.play(
            FadeOut(eq),
            circle_grp[0].scale,0.64,
            circle_grp[0].move_to,ORIGIN,
            circle_grp[0].to_edge,DOWN,{"buff":0.2}
        )
        self.wait()
        # ---------------------- Transform 2theta by varphi
        theta_2 = circle_grp[-1]
        varphi = TexMobject("\\varphi")
        varphi.match_color(theta_2)
        varphi.move_to(theta_2)
        varphi.match_updaters(theta_2)
        self.play(Transform(theta_2,varphi))
        self.wait()
        # ---------------------- Cases
        titles = VGroup(*[
            TextMobject(f) for f in ["Case 1", "Case 2", "Case 3"]
        ])
        titles.arrange(RIGHT,buff=3).to_edge(UP)
        # ---------------------- Case 1
        self.play(Write(titles[0]))
        self.wait()
        self.play(
            v1.set_value,40,
            v2.set_value,290-180,
            v3.set_value,290,
            run_time=3,
        )
        case_1 = circle_grp.deepcopy()
        case_1.clear_updaters()
        self.play(
            case_1.set_width,2,
            case_1.next_to,titles[0],DOWN,buff=0.2
        )
        self.wait()
        self.bring_to_front(case_1[1])
        # ---------------------- Case 2
        self.play(Write(titles[1]))
        self.wait()
        self.play(
            v1.set_value,30,
            v2.set_value,140,
            v3.set_value,260,
            run_time=3,
        )
        self.wait()
        case_2 = circle_grp.deepcopy()
        case_2.clear_updaters()
        self.play(
            case_2.set_width,2,
            case_2.next_to,titles[1],DOWN,buff=0.2
        )
        self.wait()
        self.bring_to_front(case_2[1])
        # ---------------------- Case 3
        self.play(Write(titles[2]))
        self.wait()
        self.play(
            v1.set_value,30,
            v2.set_value,90,
            v3.set_value,325,
            run_time=3,
        )
        case_3 = circle_grp.deepcopy()
        case_3.clear_updaters()
        self.bring_to_front(case_3[1])
        self.wait()
        self.play(
            case_3.set_width,2,
            case_3.next_to,titles[2],DOWN,buff=0.2
        )
        # ---------------------- Remove updaters
        circle_grp.clear_updaters()
        self.play(Write(circle_grp,rate_func=lambda t: smooth(1-t),run_time=2.5))
        self.wait()
        # ------------ Case by case
        cases = VGroup(case_1,case_2,case_3)
        SCREEN = Rectangle(width=FRAME_WIDTH,height=FRAME_HEIGHT)
        grps = VGroup(*[VGroup(t,c) for t,c in zip(titles,cases)])
        grps.generate_target()
        gt = grps.target[1:]
        gp = grps.target[0]
        gt.align_to(SCREEN,UP)
        gt.shift(UP*grps.get_height())
        gp[1].set_height(6)
        gp[1].move_to(ORIGIN)
        gp[1].to_edge(DOWN)
        gp[1].to_edge(LEFT,buff=2)
        gp[0].set_x(0)
        self.play(
            MoveToTarget(grps)
        )
        self.wait()
        self.cases_group_1 = VGroup(case_1,titles[0])
        self.proof_1(case_1)
        # next case
        def next_proof(height=6, buff_down=1, buff_left=0.5):
            def func(vgr):
                tit, gr = vgr
                tit.move_to(ORIGIN)
                tit.to_edge(UP)
                gr.set_height(height)
                gr.move_to(ORIGIN)
                gr.to_edge(DOWN,buff=buff_down)
                gr.to_edge(LEFT,buff=buff_left)
                return vgr
            return func
        frame_1 = self.get_screen_rect()
        self.cases_group_1.add(frame_1)
        self.play(FadeIn(frame_1))
        self.play(
            self.cases_group_1.set_height,1,
            self.cases_group_1.to_corner,UL,{"buff":0.1},
            run_time=2
        )
        self.play(ApplyFunction(next_proof(), grps[1]))
        self.wait()
        # case 2
        self.cases_group_2 = VGroup(titles[1],case_2)
        self.proof_2(case_2)
        frame_2 = self.get_screen_rect()
        self.cases_group_2.add(frame_2)
        self.play(FadeIn(frame_2))
        self.play(
            self.cases_group_2.set_height,1,
            self.cases_group_2.next_to,self.cases_group_1,RIGHT,0,
            run_time=2
        )
        self.play(ApplyFunction(next_proof(6,0.2), grps[2]))
        # case 3
        self.cases_group_3 = VGroup(titles[2],case_3)
        self.proof_3(case_3)
        frame_3 = self.get_screen_rect()
        self.cases_group_3.add(frame_3)
        self.play(FadeIn(frame_3))
        all_cases = VGroup(self.cases_group_1,self.cases_group_2,self.cases_group_3)
        self.play(
            self.camera_frame.set_width,VGroup(frame_1,frame_2).get_width()*1,
            self.camera_frame.move_to,VGroup(frame_1,frame_2).get_center(),
            self.camera_frame.shift,DOWN*VGroup(frame_1,frame_2).get_height()/2,
            self.cases_group_3.set_height,1,
            self.cases_group_3.next_to,VGroup(frame_1,frame_2),DOWN,0,
            run_time=2
        )
        # self.play(MoveToTarget(all_cases))
        
        self.wait()
        # self.play(v2.set_value,190,run_time=5,rate_func=linear)
    
    def proof_1(self, case):
        print("Proof 1")
        dots = case[1]
        d1, d2, d3 = dots
        center = case[0]
        theta = case[-2]
        varphi = case[-1]
        # Radius
        r1 = Line(center.get_center(),d1.get_center(),color=RED_A,stroke_width=8)
        r2 = Line(center.get_center(),d3.get_center(),color=RED_A,stroke_width=8)
        r1_tex = TexMobject("r").add_background_rectangle()
        r1_tex.move_to(r1)
        r2_tex = r1_tex.deepcopy()
        r2_tex.move_to(r2)
        # self.add(r1,r2,r1_tex,r2_tex)
        self.cases_group_1.add(case,r1,r2,r1_tex,r2_tex,)
        self.play(
            ShowCreation(r1),
            ShowCreation(r2),
            Write(r1_tex),
            Write(r2_tex),
            Animation(dots),
        )
        self.bring_to_front(dots)
        self.wait()
        # Arc and theta
        arc_p1 = ArcBetweenVectors(0.6,center,d3,d1,True)
        arc_p1.match_color(theta)
        theta_copy = LabelFromArc(arc_p1, theta.get_height(), "\\theta", distance_proportion=1.5)
        theta_copy.match_style(theta)
        # psi
        arc_psi = ArcBetweenVectors(0.4,d3,d1,center,True)
        arc_psi.set_color(RED_A)
        psi = LabelFromArc(arc_psi, theta.get_height(), "\\psi", distance_proportion=1.3)
        psi.match_color(arc_psi)
        # self.add(arc_p1,theta_copy,arc_psi,psi)
        self.cases_group_1.add(arc_p1,theta_copy,arc_psi,psi)
        self.play(
            TransformFromCopy(theta,theta_copy),
            ShowCreation(arc_p1),
            run_time=2
        )
        self.wait(2)
        self.play(
            ShowCreation(arc_psi),
            Write(psi),
            run_time=2
        )
        self.wait(2)
        # formulas develop
        t1 = TexMobject("\\psi","+","2","\\theta","=","180^\\circ",
            tex_to_color_map={
                "\\psi": psi.get_color(), "\\theta": theta.get_color(),
            },
        )
        t2 = TexMobject("\\psi","+","\\varphi","=","180^\\circ",
            tex_to_color_map={
                "\\psi": psi.get_color(), "\\varphi": varphi.get_color(),
            },
        )
        t3 = TexMobject("\\psi","+","2","\\theta","=","\\psi","+","\\varphi",
            tex_to_color_map={
                "\\psi": psi.get_color(), "\\varphi": varphi.get_color(),
                "\\theta": theta.get_color()
            },
        )
        t4 = TexMobject("2","\\theta","=","\\varphi",
            tex_to_color_map={
                "\\psi": psi.get_color(), "\\varphi": varphi.get_color(),
                "\\theta": theta.get_color()
            },
        )
        tg = VGroup(t1,t2,t3,t4).arrange(DOWN,buff=0.6)
        self.cases_group_1.add(t1,t2,t3,t4)
        tg.scale(1.35)
        self.align_formulas_with_equal(t2, t1, -2, -2)
        self.align_formulas_with_equal(t3, t1, 4, -2)
        self.align_formulas_with_equal(t4, t1, -2, -2)
        tg.to_edge(RIGHT,buff=0.7)
        # row 1
        tc1 = theta.deepcopy()
        tc2 = theta_copy.deepcopy()
        self.play(
            TransformFromCopy(psi, t1[0]),
            ReplacementTransform(tc1.copy(), t1[3]),
            ReplacementTransform(tc2.copy(), t1[3]),
            # Transform(tc2, t1[3].copy()),
            *[Write(t1[i]) for i in [1,2,-2,-1]],
            run_time=3
        )
        self.cases_group_1.add(tc1,tc2)
        self.wait()
        self.play(
            TransformFromCopy(t1[0],t2[0]),
            TransformFromCopy(varphi,t2[2],path_arc=-PI/2),
            *[Write(t2[i]) for i in [1,*range(3,len(t2))]],
            run_time=3
        )
        self.wait()
        self.play(
            TransformFromCopy(t1[:4],t3[:4]),
            TransformFromCopy(t2[:3],t3[-3:]),
            Write(t3[4]),
            run_time=3
        )
        self.wait()
        self.play(
            t3[0].fade,0.5,
            t3[-3].fade,0.5,
        )
        self.wait()
        self.play(
            TransformFromCopy(t3[2:4],t4[:2]),
            TransformFromCopy(t3[-1],t4[-1]),
            Write(t4[2]),
            run_time=3
        )
        self.wait()
        self.play(
            Succession(
                FadeToColor(t4,YELLOW),
                FadeToColor(t4,PURPLE_A),
            ),
            AnimationGroup(
                ShowCreationThenDestructionAround(t4.deepcopy()),
                ShowCreationThenDestructionAround(t4.deepcopy()),
                lag_ratio=1
            )
        )
        self.wait()

        # n = 0
        # for mob in self.mobjects:
        #     try:
        #         t = Text(f"{n}").next_to(mob,UP,0)
        #         self.add(t)
        #         n += 1
        #     except:
        #         n += 1
        #         pass

    def proof_2(self, case):
        print("Proof 2")
        dots = case[1]
        d1, d2, d3 = dots
        center = case[0]
        theta = case[-2]
        varphi = case[-1]
        # Radius
        r1 = Line(center.get_center(),d1.get_center(),color=RED_A,stroke_width=8)
        r2 = Line(center.get_center(),d2.get_center(),color=RED_A,stroke_width=8)
        r3 = Line(center.get_center(),d3.get_center(),color=RED_A,stroke_width=8)
        r1_tex = TexMobject("r").add_background_rectangle()
        r1_tex.move_to(r1)
        r2_tex = r1_tex.deepcopy()
        r2_tex.move_to(r2)
        r3_tex = r1_tex.deepcopy()
        r3_tex.move_to(r3)
        arc_p3_2 = ArcBetweenVectors(0.8,center,d2,d3).set_color(TEAL)
        arc_p3_1 = ArcBetweenVectors(1,d1,center,d3).set_color(TEAL)
        # theta.shift(LEFT*0.2)
        th_1 = LabelFromArc(arc_p3_1,theta.get_height()*0.8,"\\theta_1",color=theta.get_color(),distance_proportion=2)
        th_2 = LabelFromArc(arc_p3_2,theta.get_height()*0.8,"\\theta_2",color=theta.get_color(),distance_proportion=2)
        self.add_foreground_mobjects(dots,case[5])
        self.cases_group_2.add(th_1,th_2)
        self.play(theta.next_to,d3,DOWN,buff=0.2)
        self.wait()
        self.play(
            ShowCreation(r1),
            ShowCreation(r2),
            ShowCreation(r3),
            Write(r1_tex),
            Write(r2_tex),
            Write(r3_tex),
        )
        self.wait()
        self.play(
            ReplacementTransform(theta.copy()[0],th_1[0]),
            ReplacementTransform(theta.copy()[0],th_2[0]),
            ShowCreation(arc_p3_1),
            ShowCreation(arc_p3_2),
            run_time=3.5
        )
        self.wait()
        # self.remove(theta)
        self.cases_group_2.add(r1,r2,r3,r1_tex,r2_tex,r3_tex,arc_p3_1,arc_p3_2)
        # ---------------- ARC PSI
        arc_psi_1 = ArcBetweenVectors(0.4,d3,d1,center,True).set_color(RED_A)
        arc_psi_2 = ArcBetweenVectors(0.4,d3,d2,center,True).set_color(RED_A)
        arc_psi_2.rotate(-arc_psi_2.get_angle(),about_point=center.get_center())
        psi_1 = LabelFromArc(arc_psi_1,theta.get_height()*0.8,"\\psi_1",color=RED_A,distance_proportion=1.6)
        psi_2 = LabelFromArc(arc_psi_2,theta.get_height()*0.8,"\\psi_2",color=RED_A,distance_proportion=1.6)
        self.play(
            *list(map(Write,[arc_psi_1,arc_psi_2,psi_1,psi_2])),
            run_time=2
        )
        self.wait()
        self.cases_group_2.add(arc_psi_1,arc_psi_2,psi_1,psi_2)
        # ---------------- FORMUAS transformn
        tex_formulas_kwargs = {
            "tex_to_color_map": {
                "\\psi_1": psi_1.get_color(), "\\psi_2": psi_2.get_color(), "\\varphi": varphi.get_color(),
                "\\theta_1": th_1.get_color(), "\\theta_2": th_1.get_color(),
            }
        }
        # FORMULAS
        f1 = TexMobject(
            "\\psi_1","+","\\psi_2","+","\\varphi","=","360^\\circ",**tex_formulas_kwargs
        )
        f2 = TexMobject(
            "(","180^\\circ","-","2","\\theta_1",")","+","(","180^\\circ","-","2","\\theta_2",")","+","\\varphi","=","360^\\circ",
            **tex_formulas_kwargs
        )
        f2.add_background_rectangle()
        f3 = TexMobject(
            "-","2","\\theta_1","-","2","\\theta_2","+","\\varphi","=","0",**tex_formulas_kwargs
        )
        f4 = TexMobject(
            "\\varphi","=","2","\\theta_1","+","2","\\theta_2",**tex_formulas_kwargs
        )
        f5 = TexMobject(
            "\\varphi","=","2","(","\\theta_1","+","\\theta_2",")",**tex_formulas_kwargs
        )
        f6 = TexMobject(
            "\\varphi","=","2","\\theta",**tex_formulas_kwargs
        )
        f6[-1].set_color(theta.get_color())
        # f2[0].set_color(RED)
        fg = VGroup(f1,f2,f3,f4,f5,f6).arrange(DOWN,buff=0.6)
        fg.to_edge(RIGHT).to_edge(DOWN)
        self.align_formulas_with_equal(f3,f1,-2,5)
        self.align_formulas_with_equal(f4,f1,1,5)
        self.align_formulas_with_equal(f5,f1,1,5)
        self.align_formulas_with_equal(f6,f1,1,5)
        # ---------------- FORMUAS transformn
        by_case_1 = TextMobject("By Case 1").to_edge(RIGHT)
        self.play(
            LaggedStart(
                TransformFromCopy(psi_1[0],f1[0],path_arc=-PI/2),
                TransformFromCopy(psi_2[0],f1[2],path_arc=-PI/2),
                TransformFromCopy(varphi,f1[4],path_arc=-PI/2),
                lag_ratio=0.6
            ),
            LaggedStart(*[Write(f1[i]) for i in [1,3,5,6]]),
            run_time=6
        )
        self.wait()
        self.play(Write(by_case_1))
        self.wait()
        self.play(
            FadeIn(f2[0]),
            *[
                TransformFromCopy(f1[i],f2[j+1])
                for i,j in zip(
                    [1,3,4,5,6],
                    [6,13,14,15,16]
                )
            ],
            TransformFromCopy(f1[0],f2[1:6+1]),
            TransformFromCopy(f1[2],f2[7+1:13+1]),
            # LaggedStart(*[Write(f2[i+1]) for i in [6,13]]),
            run_time=4
        )
        self.wait()
        self.play(Write(by_case_1,rate_func=lambda t: smooth(1-t)))
        self.wait()
        self.play(
            *[
                ApplyMethod(mob.fade,0.7)
                for mob in [f2[i+1] for i in [1,8,16]]
            ]
        )
        self.wait(2)
        self.play(
            *[
                TransformFromCopy(f2[i+1],f3[j])
                for i,j in zip(
                    [2,3,4,9,10,11,13,14,15],
                    [*range(len(f3)-1)]
                )
            ],
            Write(f3[-1]),
            # LaggedStart(*[Write(f2[i+1]) for i in [6,13]]),
            run_time=4
        )
        self.wait()
        self.play(
            *[
                TransformFromCopy(f3[i],f4[j])
                for i,j in zip(
                    [1,2,4,5,7,8],
                    [2,3,5,6,0,1]
                )
            ],
            Write(f4[4]),
            # LaggedStart(*[Write(f2[i+1]) for i in [6,13]]),
            run_time=4
        )
        self.wait()
        self.play(
            *[
                ReplacementTransform(f4[i].deepcopy(),f5[j])
                for i,j in zip(
                    [0,1,2,3,4,5,6],
                    [0,1,2,4,5,2,6]
                )
            ],
            Write(f5[3]),
            Write(f5[-1]),
            # LaggedStart(*[Write(f2[i+1]) for i in [6,13]]),
            run_time=4
        )
        self.wait()
        self.play(
            *[
                ReplacementTransform(f5[i].deepcopy(),f6[j])
                for i,j in zip(
                    [0,1,2],
                    [0,1,2]
                )
            ],
            TransformFromCopy(f5[-5:],f6[-1]),
            run_time=4
        )
        self.foreground_mobjects = []
        self.wait()
        self.play(
            Succession(
                FadeToColor(f6,YELLOW),
                FadeToColor(f6,PURPLE_A),
            ),
            AnimationGroup(
                ShowCreationThenDestructionAround(f6.deepcopy()),
                ShowCreationThenDestructionAround(f6.deepcopy()),
                lag_ratio=1
            )
        )
        # self.play(
        #     *[
        #         TransformFromCopy()
        #     ],
        # )
        # self.add(fg)
        # VGroup(case,*self.mobjects[start_index:]).set_color(TEAL)
        self.cases_group_2.add(fg,by_case_1)
        self.wait()
        
    def proof_3(self, case):
        print("Proof 3")
        dots = case[1]
        d1, d2, d3 = dots
        center = case[0]
        theta = case[-2]
        varphi = case[-1]
        self.add_foreground_mobject(dots)
        def fade_mobs(fade=0.9):
            def update(mob):
                mob.fade(fade)
                return mob
            return update
        # ---------------- FIGURES DEFINITION
        diameter_vector = Line(d3.get_center(),center.get_center()).get_vector()
        diameter = Line(d3.get_center(),d3.get_center()+diameter_vector*2,color=RED_A)
        d4 = Dot(diameter.get_end())
        arc_psi_1 = ArcBetweenVectors(0.6,d2,d4,d3,color=RED_A)
        arc_psi_2 = ArcBetweenVectors(0.6,d2,d4,center,color=RED_A)
        arc_alpha_1 = ArcBetweenVectors(0.7,d1,d4,d3,color=YELLOW_B,stroke_width=8)
        arc_alpha_2 = ArcBetweenVectors(0.7,d1,d4,center,color=YELLOW_B,stroke_width=8)
        psi_1 = LabelFromArc(arc_psi_1,theta.get_height()*0.8,"\\psi_1",color=RED_A,distance_proportion=2.1)
        psi_2 = LabelFromArc(arc_psi_2,theta.get_height()*0.8,"\\psi_2",color=RED_A,distance_proportion=2.1)
        alpha_1 = LabelFromArc(arc_alpha_1,theta.get_height()*0.8,"\\alpha_1",color=YELLOW_B,distance_proportion=2.5)
        back_1 = BackgroundRectangle(alpha_1)
        alpha_2 = LabelFromArc(arc_alpha_2,theta.get_height()*0.8,"\\alpha_2",color=YELLOW_B,distance_proportion=2.3)
        back_2 = BackgroundRectangle(alpha_2)
        line_1 = Line(center.get_center(),d1.get_center(),color=varphi.get_color())
        line_2 = Line(d3.get_center(),d1.get_center(),color=varphi.get_color())
        # ---------
        psi_g = VGroup(arc_psi_1,arc_psi_2,psi_1,psi_2)
        alpha_g = VGroup(arc_alpha_1,arc_alpha_2,alpha_1,alpha_2)
        theta_g = VGroup(theta,varphi,case[-3],case[-4],case[2],case[3])
        self.wait()
        self.play(
            GrowFromCenter(diameter)
        )
        self.wait()
        self.play(
            LaggedStart(*[
                Write(arc)
                for arc in psi_g
            ]),
        )
        self.wait(2)
        self.play(
            *list(map(FadeIn,[back_1,back_2])),
            LaggedStart(*[
                Write(arc)
                for arc in alpha_g
            ]),
        )
        self.wait(2)
        self.add_foreground_mobjects(back_1,back_2,alpha_g)
        self.cases_group_3.add(
            arc_psi_1,arc_psi_2,arc_alpha_1,arc_alpha_2,diameter,
            psi_1,psi_2,alpha_1,alpha_2,
        )
        self.add(line_1,line_2)
        for i in [psi_g,theta_g]:
            for j in i:
                j.save_state()
        self.play(
            *[ApplyFunction(fade_mobs(),i) for i in psi_g],
            *[ApplyFunction(fade_mobs(),i) for i in theta_g],
        )
        self.wait()
        # self.play(
        #     Restore(psi_g),
        #     Restore(theta_g),
        # )
        # self.wait()
        # self.play(ApplyFunction(show_mobs(),psi_g))
        # ---------------- FORMULAS DEFINITION
        formulas = [
            ["\\alpha_1","=","\\psi_1","+","\\theta"],
            ["\\alpha_2","=","\\psi_2","+","\\varphi"],
            ["\\alpha_2","=","2","\\alpha_1"],
            ["\\psi_2","+","\\varphi","=","2","(","\\psi_1","+","\\theta",")"],
            ["\\psi_2","=","2","\\psi_1"],
            ["2","\\psi_1","+","\\varphi","=","2","\\psi_1","+","2","\\theta"],
            ["\\varphi","=","2","\\theta"],
        ]
        tex_formulas_kwargs = {
            "tex_to_color_map": {
                "\\psi_1": psi_1.get_color(), "\\psi_2": psi_2.get_color(), "\\varphi": varphi.get_color(),
                "\\theta": theta.get_color(), "\\alpha_1": alpha_1.get_color(), "\\alpha_2": alpha_2.get_color()
            }
        }
        f = VGroup(*[
            TexMobject(*formula, **tex_formulas_kwargs)
            for formula in formulas
        ])
        f.arrange(DOWN)
        f.scale(1.3)
        for fi,i in zip(f[1:],[1,1,3,1,4,1]):
            self.align_formulas_with_equal(fi,f[0],i,1)
        f.to_edge(RIGHT,buff=1.8)
        # --------------------------------------
        by_case_1 = TextMobject("By case 1")
        by_case_1.next_to(f[2],RIGHT)
        by_case_2 = by_case_1.copy()
        by_case_2.next_to(f[4],RIGHT)
        # ----------- FORMULAS ANIMATIONS
        self.play(
            FadeOut(back_1),
            Restore(theta),
            Restore(psi_1),
            ReplacementTransform(alpha_1[0],f[0][0]),
            run_time=2,
        )
        self.play(
            TransformFromCopy(psi_1[0],f[0][2]),
            TransformFromCopy(theta[0],f[0][-1]),
            *[Write(f[0][i]) for i in [1,3]],
            run_time=3,
        )
        self.wait()
        self.play(
            FadeOut(back_2),
            Restore(varphi),
            Restore(psi_2),
            ReplacementTransform(alpha_2[0],f[1][0]),
            run_time=2,
        )
        self.play(
            TransformFromCopy(psi_2[0],f[1][2]),
            TransformFromCopy(varphi[0],f[1][-1]),
            *[Write(f[1][i]) for i in [1,3]],
            run_time=3,
        )
        self.wait()
        # By case 1 - 1
        self.play(
            Write(by_case_1)
        )
        self.wait()
        self.play(
            Write(f[2])
        )
        self.wait()
        # -----------------
        self.play(
            TransformFromCopy(f[0][-3:],f[3][6:9]),
            TransformFromCopy(f[1][-3:],f[3][:3]),
            *[
                TransformFromCopy(f[2][i],f[3][j])
                for i,j in zip(
                    [1,2],
                    [3,4]
                )
            ],
            *[Write(f[3][i]) for i in [5,9]],
            run_time=3
        )
        self.wait()
        # ---------------------------
        self.wait()
        line_3 = Line(d3.get_center(),d2.get_center(),color=TEAL_A)
        line_4 = Line(center.get_center(),d2.get_center(),color=PURPLE_A)
        save_grp = VGroup(arc_alpha_1,arc_alpha_2,varphi,theta)
        for i in save_grp:
            try:
                i.save_state()
            except:
                pass
        self.play(
            FadeOut(line_1),
            FadeOut(line_2),
            # line_1.fade,1,
            # line_2.fade,1,
            FadeIn(line_3),
            FadeIn(line_4),
            *[ApplyMethod(i.fade,0.92) for i in save_grp],
            *[Restore(i) for i in [arc_psi_1,arc_psi_2]]
        )
        self.wait(3)
        # by case 2
        self.play(
            Write(by_case_2)
        )
        self.wait()
        self.play(
            Write(f[4])
        )
        self.wait(3)
        self.play(
            *[Restore(i) for i in [*save_grp,*case[2:6]]]
        )
        self.wait()
        # ---------------------------
        self.play(
            # TransformFromCopy(f[3][-3:],f[5][6:9]),
            TransformFromCopy(f[3][0],f[5][:2]),
            *[
                TransformFromCopy(f[3][i],f[5][j])
                for i,j in zip(
                    [1,2,3,4,6,7,8,4],
                    [2,3,4,5,6,7,9,8]
                )
            ],
            run_time=3
        )
        self.wait()
        self.play(
            *[ApplyMethod(f[5][i].fade,0.8) for i in [0,1,5,6]],
            run_time=2
        )
        self.play(
            *[
                TransformFromCopy(f[5][i],f[6][j])
                for i,j in zip(
                    [3,4,8,9],
                    [0,1,2,3]
                )
            ],
            run_time=3
        )
        # self.play(
        #     *{Restore(i) for i in [case[2],case[3]]}
        # )
        
        # self.add(f,by_case_1,by_case_2)
        
        self.play(
            Succession(
                FadeToColor(f[6],YELLOW),
                FadeToColor(f[6],PURPLE_A),
            ),
            AnimationGroup(
                ShowCreationThenDestructionAround(f[6].deepcopy()),
                ShowCreationThenDestructionAround(f[6].deepcopy()),
                lag_ratio=1
            )
        )
        self.cases_group_3.add(line_1,line_2,line_3,line_4,by_case_1,by_case_2,f)
        self.wait()

    
    def align_formulas_with_equal(self, f1, f2, i1, i2):
        c1 = f1[i1].get_center()
        c2 = f2[i2].get_center()
        distance = c2 - c1
        f1.shift(RIGHT*distance[0])
        
    def get_screen_rect(self):
        return Rectangle(width=FRAME_WIDTH,height=FRAME_HEIGHT)
    
        

# --------------------------------------------------------
# --------------------------------------------------------
# --------------------------------------------------------

class Polygon(Polygon):
    def get_center_of_edges(self,buff=SMALL_BUFF*3):
        vertices = self.get_vertices()
        coords_vertices = []
        for i in range(len(vertices)):
            if i < len(vertices)-1:
                p1,p2 = [vertices[i],vertices[i+1]]
            else:
                p1,p2 = [vertices[-1],vertices[0]]
            guide_line = Line(p1,p2)
            side = guide_line.get_center()
            normal_direction = guide_line.copy()
            normal_direction.rotate(-PI/2)
            vector_normal_direction = normal_direction.get_unit_vector()
            direction = Dot(side).shift(vector_normal_direction*buff).get_center()
            coords_vertices.append(direction)

        return coords_vertices

class SineLaw(Scene):
    CONFIG = {
        "triangle_config": {
            "color": RED,
            "stroke_width": 8,
        },
        "tex_map": {
            "tex_to_color_map": {
                "\\alpha": RED_A, 
                "\\beta": TEAL_A,
                "\\gamma": PURPLE_A,
                "A": RED_A, 
                "B": TEAL_A,
                "C": PURPLE_A,
                "x": GREEN_A,
                "h_1": YELLOW_B,
                "h_2": BLUE_B,
            }
        }
    }
    def construct(self):
        du = UP*1.5
        d1 = Dot(LEFT*4+du)
        d2 = Dot(RIGHT*2+du)
        d3 = Dot(RIGHT*4+UP*2+du)
        triangle = Polygon(
            d1.get_center(),d2.get_center(),d3.get_center(),**self.triangle_config
        )
        def frac_string(n,d):
            return ["{",n,"\\over",d,"}"]
        def frac_strings(n,d):
            return ["{",*n,"\\over",*d,"}"]
        sina_t = ["{\\rm sin}","\\alpha"]
        sinb_t = ["{\\rm sin}","\\beta"]
        sinc_t = ["{\\rm sin}","\\gamma"]
        cosa_t = ["{\\rm cos}","\\alpha"]
        cosb_t = ["{\\rm cos}","\\beta"]
        cosc_t = ["{\\rm cos}","\\gamma"]
        formulas_sine_string_1 = [
            [*sinb_t,"=",*frac_string("h_1","C")],
            [*sinc_t,"=",*frac_string("h_1","B")],
            ["C","\\,",*sinb_t,"=","h_1"],
            ["B","\\,",*sinc_t,"=","h_1"],
            ["C","\\,",*sinb_t,"=","B","\\,",*sinc_t],
            [*frac_strings(["C"],sinc_t),"=",*frac_strings(["B"],sinb_t)]
        ]
        formulas_sine_string_2 = [
            [*sina_t,"=",*frac_string("h_2","B")],
            [*sinb_t,"=",*frac_string("h_2","A")],
            ["B","\\,",*sina_t,"=","h_2"],
            ["A","\\,",*sinb_t,"=","h_2"],
            ["B","\\,",*sina_t,"=","A","\\,",*sinb_t],
            [*frac_strings(["B"],sinb_t),"=",*frac_strings(["A"],sina_t)]
        ]
        sine_law = TexMobject(*[
            *frac_strings(["C"],sinc_t),"=",*frac_strings(["B"],sinb_t),"=",*frac_strings(["A"],sina_t),
        ],**self.tex_map).scale(0.9)
        formulas_sine_1 = VGroup(*[
            TexMobject(*f,**self.tex_map) for f in formulas_sine_string_1
        ])
        # formulas_sine.arrange_in_grid(None,2)
        formulas_sine_arrange_1 = VGroup(
            formulas_sine_1[:2].arrange(RIGHT,buff=1),
            formulas_sine_1[2:4].arrange(RIGHT,buff=1),
            formulas_sine_1[4:].arrange(DOWN),
        ).arrange(DOWN,buff=0.7).scale(0.9)
        formulas_sine_2 = VGroup(*[
            TexMobject(*f,**self.tex_map) for f in formulas_sine_string_2
        ])
        # formulas_sine.arrange_in_grid(None,2)
        formulas_sine_arrange_2 = VGroup(
            formulas_sine_2[:2].arrange(RIGHT,buff=1),
            formulas_sine_2[2:4].arrange(RIGHT,buff=1),
            formulas_sine_2[4:].arrange(DOWN),
        ).arrange(DOWN,buff=0.7).scale(0.9)
        formulas_sine_arrange_1.to_edge(DOWN,buff=0.3)
        formulas_sine_arrange_1.to_edge(LEFT,buff=1)
        formulas_sine_arrange_2.to_edge(DOWN,buff=0.3)
        formulas_sine_arrange_2.to_edge(RIGHT,buff=1)
        sine_law.align_to(formulas_sine_arrange_1,DOWN)
        triangle.set_x(0)
        center_vertices = triangle.get_center_of_edges()
        labels = VGroup(*[
            TexMobject(label,**self.tex_map).move_to(point) for label,point in zip(["C","B","A"],center_vertices)
        ])
        fs1 = formulas_sine_1
        fs2 = formulas_sine_2
        # ------------------------------
        h1 = TexMobject("h_1",**self.tex_map)
        h2 = TexMobject("h_2",**self.tex_map)
        x = TexMobject("x",**self.tex_map)
        h1_line = self.get_h(d2,d1,d3)
        h2_line = DashedLine(d3.get_center()+RIGHT*0.09,[d3.get_x()+0.09,d2.get_y()-0.09,0])
        h3_line = DashedLine(d2.get_center()+RIGHT*0.09,h2_line.get_end())
        rec_1 = Square().set_width(0.25)
        rec_1 = VMobject().set_points_as_corners([rec_1.get_corner(v) for v in [UR,UL,DL]])
        rec_2 = rec_1.deepcopy()
        rec_1.next_to(h2_line.get_end(),UL,buff=0)
        rec_2.rotate(h1_line.get_angle())
        rec_2.next_to(h1_line.get_end(),DL,buff=0)
        rec_2.shift(DOWN*0.1+RIGHT*0.05)
        x.next_to(h3_line,DOWN,0.1)
        h1.next_to(h1_line,RIGHT,0.1)
        h1.shift(LEFT*0.15)
        h2.next_to(h2_line,RIGHT,0.1)
        # h2_line.rotate(PI,about_point=h2_line.get_start())
        # ------------------------------
        alpha_arc = ArcBetweenVectors(0.3,d1,d3,d2)
        beta_arc = ArcBetweenVectors(1.7,d2,d3,d1)
        gamma_arc = ArcBetweenVectors(1,d1,d2,d3)
        alpha_p_arc = ArcBetweenVectors(0.4,Dot(h2_line.get_end()),d3,d2)
        gamma_arc.rotate(gamma_arc.get_angle()*0.9,about_point=gamma_arc.get_arc_center())
        alpha = LabelFromArc(alpha_arc,labels[0].get_width()*0.7,"\\alpha",distance_proportion=1.9,**self.tex_map)
        beta = LabelFromArc(beta_arc,labels[0].get_width()*1.1,"\\beta",distance_proportion=1.9,**self.tex_map)
        gamma = LabelFromArc(gamma_arc,labels[0].get_width()*1.1,"\\gamma",distance_proportion=1.9,**self.tex_map)
        alpha_p = LabelFromArc(alpha_p_arc,labels[0].get_width()*1.1,"\\alpha'",distance_proportion=1.9,**self.tex_map)
        alpha.shift(LEFT*0.25+DOWN*0.1)
        but = TexMobject("{\\rm sin}(\\pi-\\alpha)={\\rm sin}(\\alpha)",**self.tex_map)
        but.to_corner(UL)
        t1 = Polygon(
            d1.get_center(),d2.get_center(),h1_line.get_end(),
            color=ORANGE,stroke_width=0,fill_opacity=0
        )
        t2 = Polygon(
            d2.get_center(),d3.get_center(),h1_line.get_end(),
            color=ORANGE,stroke_width=0,fill_opacity=0
        )
        t3 = Polygon(
            d2.get_center(),h3_line.get_end(),h2_line.get_start(),
            color=ORANGE,stroke_width=0,fill_opacity=0
        )
        t4 = Polygon(
            d1.get_center(),h3_line.get_end(),h2_line.get_start(),
            color=ORANGE,stroke_width=0,fill_opacity=0
        )
        def show_triange(t):
            t.set_fill(None,0.3)
            return t
        def hide_triange(t):
            t.set_fill(None,0)
            return t
        self.add(t1,t2,t3,t4)
        # - SHOW CREATIONS
        self.add_foreground_mobject(triangle)
        self.play(
            ShowCreation(triangle,rate_func=linear),
            LaggedStart(*list(map(Write,labels)),lag_ratio=0.8),
            run_time=2.5
        )
        self.wait()
        self.play(
            LaggedStart(*[
                TransformFromCopy(m1,m2)
                for m1,m2 in zip(labels[::-1],[alpha,beta,gamma])
            ],lag_ratio=0.7),
            LaggedStart(*list(map(ShowCreation,[alpha_arc,beta_arc,gamma_arc])),lag_ratio=0.7),
            run_time=3.5
        )
        self.wait()
        self.play(LaggedStart(*list(map(Write,[h1_line,h1,rec_2])),lag_ratio=0.5))
        # - TRANSFORMATIONS
        C,B,A = labels
        self.play(ApplyFunction(show_triange,t1))
        self.wait()
        self.play(
            LaggedStart(
                TransformFromCopy(beta[0],fs1[0][1]),
                TransformFromCopy(h1[0],fs1[0][-4]),
                TransformFromCopy(C[0],fs1[0][-2]),
                lag_ratio=0.7
            ),
            LaggedStart(*[Write(fs1[0][i]) for i in [0,2,-3]]),
            run_time=5
        )
        self.wait()
        self.play(ApplyFunction(hide_triange,t1))
        self.wait()
        self.play(ApplyFunction(show_triange,t2))
        self.wait()
        self.play(
            LaggedStart(
                TransformFromCopy(gamma[0],fs1[1][1]),
                TransformFromCopy(h1[0],fs1[1][-4]),
                TransformFromCopy(B[0],fs1[1][-2]),
                lag_ratio=0.7
            ),
            LaggedStart(*[Write(fs1[1][i]) for i in [0,2,-3]]),
            run_time=5
        )
        self.wait()
        self.play(ApplyFunction(hide_triange,t2))
        #  - - - - - - - -
        self.wait()
        self.play(
            LaggedStart(
                TransformFromCopy(fs1[0][-2],fs1[2][0]),
                AnimationGroup(
                    TransformFromCopy(fs1[0][0],fs1[2][2]),
                    TransformFromCopy(fs1[0][1],fs1[2][3]),
                    lag_ratio=0
                ),
                TransformFromCopy(fs1[0][2],fs1[2][4]),
                TransformFromCopy(fs1[0][-4],fs1[2][-1]),
                lag_ratio=0.3
            ),
            # LaggedStart(*[Write(fs1[1][i]) for i in [0,2,-3]]),
            run_time=5
        )
        self.wait()
        self.play(
            LaggedStart(
                TransformFromCopy(fs1[1][-2],fs1[3][0]),
                AnimationGroup(
                    TransformFromCopy(fs1[1][0],fs1[3][2]),
                    TransformFromCopy(fs1[1][1],fs1[3][3]),
                    lag_ratio=0
                ),
                TransformFromCopy(fs1[1][2],fs1[3][4]),
                TransformFromCopy(fs1[1][-4],fs1[3][-1]),
                lag_ratio=0.3
            ),
            # LaggedStart(*[Write(fs1[1][i]) for i in [0,2,-3]]),
            run_time=5
        )
        self.wait()
        self.play(
            TransformFromCopy(fs1[2][:4],fs1[4][:4]),
            TransformFromCopy(fs1[3][:4],fs1[4][-4:]),
            Write(fs1[4][4]),
            run_time=5
        )
        self.wait()
        self.play(
            LaggedStart(
                TransformFromCopy(fs1[4][0],fs1[5][1]),
                TransformFromCopy(fs1[4][-2:],fs1[5][3:5]),
                TransformFromCopy(fs1[4][-4],fs1[5][-5]),
                TransformFromCopy(fs1[4][2:4],fs1[5][-3:-1]),
                lag_ratio=0.5
            ),
            # TransformFromCopy(fs1[4][-2:],fs1[5][3:5]),
            # TransformFromCopy(fs1[3][:4],fs1[4][-4:]),
            LaggedStart(
                Write(fs1[5][2]),
                Write(fs1[5][-4]),
                Write(fs1[5][6]),
                lag_ratio=0.5
            ),
            run_time=5
        )
        self.wait()
        # ------------------------------
        self.play(LaggedStart(*list(map(Write,[h2_line,h2,h3_line,x,rec_1])),lag_ratio=0.5))
        self.wait()
        self.play(Write(alpha_p),Write(alpha_p_arc))
        self.wait()
        self.play(Write(but))
        self.wait()
        self.play(Indicate(but),Indicate(alpha_p),Indicate(alpha_p_arc),run_time=3)
        self.wait()
        self.play(ApplyFunction(show_triange,t3))
        self.wait()
        self.play(
            LaggedStart(
                TransformFromCopy(alpha_p[0],fs2[0][1]),
                TransformFromCopy(h2[0],fs2[0][-4]),
                TransformFromCopy(B[0],fs2[0][-2]),
                lag_ratio=0.7
            ),
            LaggedStart(*[Write(fs2[0][i]) for i in [0,2,-3]]),
            run_time=5
        )
        self.wait()
        self.play(ApplyFunction(hide_triange,t3))
        self.wait()
        self.play(ApplyFunction(show_triange,t4))
        self.wait()
        self.play(
            LaggedStart(
                TransformFromCopy(beta[0],fs2[1][1]),
                TransformFromCopy(h2[0],fs2[1][-4]),
                TransformFromCopy(A[0],fs2[1][-2]),
                lag_ratio=0.7
            ),
            LaggedStart(*[Write(fs2[1][i]) for i in [0,2,-3]]),
            run_time=5
        )
        self.wait()
        self.play(ApplyFunction(hide_triange,t4))
        # ------------------------------
        self.play(
            LaggedStart(*[FadeIn(f) for f in fs2[2:]],lag_ratio=0.5),
            run_time=8
        )
        self.wait()
        # self.add(sine_law)
        self.play(
            ReplacementTransform(fs1[-1],sine_law[:len(fs1[-1])]),
            ReplacementTransform(fs2[-1],sine_law[-len(fs2[-1]):]),
            run_time=2.5
        )
        sine_law.save_state()
        self.wait()
        self.play(
            Succession(
                FadeToColor(sine_law,YELLOW),
                Restore(sine_law)
            ),
            AnimationGroup(
                ShowCreationThenDestructionAround(sine_law.copy()),
                ShowCreationThenDestructionAround(sine_law.copy()),
                lag_ratio=1
            )
        )
        # self.add(but,h1_line,h2_line,h3_line,rec_1,rec_2,x,h1,h2,alpha_p_arc,alpha_p)
        # self.add(labels,alpha,beta,gamma)
        # self.add(alpha_arc,beta_arc,gamma_arc)
        # self.add(triangle,formulas_sine_1,formulas_sine_2,sine_law)
        # self.add_foreground_mobject(triangle)
        self.wait()
        
    def get_h(self, dot, d1, d2,invert=True):
        line = Line(d1.get_center(),d2.get_center())
        vector = line.get_unit_vector()
        sign = 1 if invert else -1
        normal_vector = rotate_vector(vector,sign*PI/2)
        def get_distance_point_line(line,dot):
            x_0, y_0, z_0 = dot.get_center()
            X_0 = line.point_from_proportion(0)
            X_1 = line.point_from_proportion(1)
            x_1, y_1, z_1 = X_0
            x_2, y_2, z_2 = X_1
            return abs((x_2-x_1)*(y_1-y_0)-(x_1-x_0)*(y_2-y_1)/get_norm(line.get_vector()))
        distance = get_distance_point_line(line,dot)
        return DashedLine(dot.get_center(),dot.get_center()+distance*normal_vector)

# --------------------------------------------------------
# --------------------------------------------------------
# --------------------------------------------------------

class CosineLaw(Scene):
    def construct(self):
        # THIS IS YOUR TASK
        pass