from manimlib.imports import *

class MeasureDistance(VGroup):
    CONFIG = {
        "color":RED_B,
        "buff":0.3,
        "lateral":0.3,
        "invert":False,
        "dashed_segment_length":0.09,
        "dashed":True,
        "ang_arrows":30*DEGREES,
        "size_arrows":0.2,
        "stroke":2.4,
    }
    def __init__(self,mob,**kwargs):
        VGroup.__init__(self,**kwargs)
        if self.dashed==True:
            medicion=DashedLine(ORIGIN,mob.get_length()*RIGHT,dashed_segment_length=self.dashed_segment_length).set_color(self.color)
        else:
            medicion=Line(ORIGIN,mob.get_length()*RIGHT)
        medicion.set_stroke(None,self.stroke)
        pre_medicion=Line(ORIGIN,self.lateral*RIGHT).rotate(PI/2).set_stroke(None,self.stroke)
        pos_medicion=pre_medicion.copy()
        pre_medicion.move_to(medicion.get_start())
        pos_medicion.move_to(medicion.get_end())
        angulo=mob.get_angle()
        matriz_rotacion=rotation_matrix(PI/2,OUT)
        vector_unitario=mob.get_unit_vector()
        direccion=np.matmul(matriz_rotacion,vector_unitario)
        self.direccion=direccion
 
        self.add(medicion,pre_medicion,pos_medicion)
        self.rotate(angulo)
        self.move_to(mob)
 
        if self.invert==True:
            self.shift(-direccion*self.buff)
        else:
            self.shift(direccion*self.buff)
        self.set_color(self.color)
        self.tip_point_index = -np.argmin(self.get_all_points()[-1, :])
 
    def add_tips(self):
        linea_referencia=Line(self[0][0].get_start(),self[0][-1].get_end())
        vector_unitario=linea_referencia.get_unit_vector()
        punto_final1=self[0][-1].get_end()
        punto_inicial1=punto_final1-vector_unitario*self.size_arrows
        punto_inicial2=self[0][0].get_start()
        punto_final2=punto_inicial2+vector_unitario*self.size_arrows
        lin1_1=Line(punto_inicial1,punto_final1).set_color(self[0].get_color()).set_stroke(None,self.stroke)
        lin1_2=lin1_1.copy()
        lin2_1=Line(punto_inicial2,punto_final2).set_color(self[0].get_color()).set_stroke(None,self.stroke)
        lin2_2=lin2_1.copy()
        lin1_1.rotate(self.ang_arrows,about_point=punto_final1,about_edge=punto_final1)
        lin1_2.rotate(-self.ang_arrows,about_point=punto_final1,about_edge=punto_final1)
        lin2_1.rotate(self.ang_arrows,about_point=punto_inicial2,about_edge=punto_inicial2)
        lin2_2.rotate(-self.ang_arrows,about_point=punto_inicial2,about_edge=punto_inicial2)
        return self.add(lin1_1,lin1_2,lin2_1,lin2_2)

    def get_text(self, text,scale=1,buff=0.1,invert_dir=False,invert_texto=False,remove_rot=False,**moreargs):
        linea_referencia=Line(self[0][0].get_start(),self[0][-1].get_end())
        texto=TextMobject(text,**moreargs)
        ancho=texto.get_height()/2
        inv = PI if invert_texto else 0
        if remove_rot:
            texto.scale(scale).move_to(self)
        else:
            texto.rotate(linea_referencia.get_angle()).scale(scale).move_to(self)
            texto.rotate(inv)
        invert_dir = -1 if invert_dir else 1
        texto.shift(self.direccion*(buff+1)*ancho*inv)
        return texto

class AnimationRectangle(VGroup):
    CONFIG = {
        "height": 0.7,
        "width": 8,
        "rectangle_config": {
            "stroke_width": 11,
            "color": WHITE
        },
        "lag_rectangle_config": {
            "color": YELLOW_D
        },
        "number_buff": 0.3
    }
    def  __init__(self,lag_ratio=0.5,**kwargs):
        digest_config(self, kwargs)
        self.lag_ratio     = ValueTracker(lag_ratio)
        self.rectangle     = self.get_rectangle()
        self.lag_rectangle = self.get_lag_rectangle()
        self.lag_rectangle.add_updater(
            lambda mob: mob.become(
                self.get_lag_rectangle()
            )
        )
        self.lag_number = self.get_lag_number()

        super().__init__(
            self.lag_rectangle,
            self.rectangle,
            self.lag_number
        )

    def get_rectangle(self):
        return Rectangle(
            width=self.width,
            height=self.height,
            fill_opacity=0,
            **self.rectangle_config
        )

    def get_lag_rectangle(self):
        if self.lag_ratio == 0:
            self.lag_ratio = 0.00001
        lag_width = self.width * self.lag_ratio.get_value()
        lag_rectangle = Rectangle(
            width=lag_width,
            height=self.height,
            stroke_width=0,
            fill_opacity=1,
            **self.lag_rectangle_config
        )
        lag_rectangle.next_to(
            self.rectangle.get_left(),
            RIGHT,buff=0
        )
        return lag_rectangle

    def get_lag_number(self):
        number = Integer(
            self.lag_ratio.get_value(),
            unit="\\%",
        )
        number.add_updater(self.get_lag_number_updater())
        return number

    def get_lag_number_updater(self):
        def update(mob):
            mob.match_height(self.rectangle)
            mob.scale(0.5)
            mob.set_value(int(self.lag_ratio.get_value()*100))
            mob.next_to(self.lag_rectangle, RIGHT, buff=self.number_buff)
        return update

    def get_lag_ratio(self):
        return self.lag_ratio

class SuccessionsExplanation(Scene):
    CONFIG = {
        "anim_widths": [1.5,2.5,4,3.5],
        "lag_ratios": [0, 0.2, 0.4, 0.6, 1]
    }
    def construct(self):
        value_tracker = ValueTracker(self.lag_ratios[0])
        lag_ratio_dn = DecimalNumber(0).add_updater(
            lambda dn: dn.set_value(
                value_tracker.get_value()
            )
        )
        lag_tex = TextMobject("\\tt lag\\_ratio = ")
        VGroup(lag_tex, lag_ratio_dn).arrange(RIGHT,buff=0.4).to_edge(UP)
        lag_ratio_dn.shift(UP*0.07)
        # SET ANIM RECTS
        anim_rects = VGroup(*[
            AnimationRectangle(value_tracker.get_value(), width=width)
            for width in self.anim_widths
        ])
        anim_rects.arrange(DOWN,aligned_edge=LEFT)
        anim_rects.to_edge(LEFT)
        anim_rects.to_edge(DOWN,buff=1)
        # Arrange anim rects
        anim_rects.add_updater(lambda vg: self.arrange_anim_rects(vg))
        # Full animation
        full_anim = self.get_full_animation(anim_rects)
        full_anim_tex = TextMobject("Full animation")
        # run_time
        run_time_arrow = MeasureDistance(
            Line(anim_rects[0].get_corner(UL), anim_rects[0].get_corner(UR)),
            buff=0.25
        ).add_tips()
        run_time_tex = run_time_arrow.get_text("\\tt run\\_time",color=RED_B)
        run_time_tex.shift(UP*0.5)
        # Animations tex
        anim_tex = VGroup(*[
            TextMobject(f"Animation {i+1}").next_to(ar)
            for i,ar in zip(range(len(anim_rects)),anim_rects)
        ])
        # ANIMS
        self.play(
            LaggedStartMap(FadeIn, [*anim_rects]),
            LaggedStartMap(FadeIn, anim_tex)
        )
        self.wait(3)
        self.play(GrowFromCenter(run_time_arrow),run_time=2)
        self.play(FadeInFrom(run_time_tex,UP))
        self.wait(3)
        self.play(
            *list(map(FadeOut, [run_time_arrow,run_time_tex,*anim_tex]))
        )
        self.wait()
        full_anim_tex.move_to(full_anim)
        self.play(
            FadeInFromDown(full_anim),
            FadeInFromDown(full_anim_tex),
        )
        full_anim.add_updater(
            lambda mob: mob.become(
                self.get_full_animation(anim_rects)
            )
        )
        full_anim_tex.add_updater(lambda tex: tex.move_to(full_anim))
        self.add(full_anim,full_anim_tex)
        self.wait()
        self.play(
            Write(VGroup(lag_tex,lag_ratio_dn))
        )
        self.add(anim_rects,full_anim,full_anim_tex)

        for lag_ratio in self.lag_ratios[1:]:
            self.play(*[
                ApplyMethod(ar.lag_ratio.set_value, lag_ratio)
                for ar in anim_rects
                ],
                value_tracker.set_value, lag_ratio,
                run_time=3
            )
            self.wait(5)
        self.wait(5)

    def arrange_anim_rects(self, anim_rects):
        for i in range(1,len(anim_rects)):
            anim_rects[i].set_x(anim_rects[i-1].lag_rectangle.get_right()[0])
            anim_rects[i].shift(
                (anim_rects[i].get_width()/2) * RIGHT
            )

    def get_full_animation(self, anim_rects):
        new_anim_rects = VGroup(*[
            ar[:-1] for ar in anim_rects
        ])
        coord_left  = new_anim_rects.get_corner(UL) + UP
        coord_right = new_anim_rects.get_corner(UR) + UP

        return Polygon(
            coord_left, coord_left + UP,
            coord_right + UP, coord_right,
            stroke_width=11, fill_opacity=0,
            stroke_opacity=1, color=WHITE
        )