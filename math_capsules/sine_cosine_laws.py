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

 
    def get_tex(self, tex,scale=1,buff=1,invert_dir=False,invert_texto=False,remove_rot=True,**moreargs):
        linea_referencia=Line(self[0][0].get_start(),self[0][-1].get_end())
        texto=TexMobject(tex,**moreargs)
        ancho=texto.get_height()/2
        if invert_texto:
            inv=PI
        else:
            inv=0
        if remove_rot:
            texto.scale(scale).move_to(self)
        else:
            texto.rotate(linea_referencia.get_angle()).scale(scale).move_to(self)
            texto.rotate(inv)
        if invert_dir:
            inv=-1
        else:
            inv=1
        texto.shift(self.direccion*(buff+1)*ancho)
        return texto

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

class SineCosineLaws(Scene):
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
                "y": GOLD_B,
                "h_1": YELLOW_B,
                "h_2": BLUE_B,
            }
        }
    }
    def construct(self):
        self.wait(0.5)
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
        cosa_t = ["\\,{\\rm cos}","\\alpha"]
        cosb_t = ["\\,{\\rm cos}","\\beta"]
        cosc_t = ["\\,{\\rm cos}","\\gamma"]
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
        self.all_mobs = VGroup(
            fs1,fs2,labels,t1,t2,t3,t4,alpha,beta,gamma,alpha_arc,beta_arc,gamma_arc,
            but,h1,h2,rec_1,rec_2,h1_line,h2_line,h3_line,x,sine_law,alpha_p,alpha_p_arc
        )
        self.funcs = [show_triange,hide_triange]
        self.remove_foreground_mobject(triangle)
        self.bring_to_front(triangle)
        self.laws = VGroup()
        self.sine_law()
        self.add(h1,h2,x,alpha_p,alpha_p_arc,rec_1,rec_2,h1_line,h2_line,h3_line)
        self.cosine_mobs = [labels,t1,t2,t3,t4,alpha,beta,gamma,h1,h2,x,alpha_p,h2_line]
        self.cosine_utils = [cosa_t,cosb_t,cosc_t,frac_string,frac_strings]
        self.cosine_law_A()
        self.cosine_law_B()
        self.cosine_law_C()
        self.laws.generate_target()
        laws = self.laws.target
        for i in laws[:-1]:
            i.set_width(laws[-1].get_width())
        laws.arrange(DOWN)
        laws.set_fill(None,1)
        laws.shift(DOWN*0.5)
        self.play(MoveToTarget(self.laws))
        self.wait()
        sine_law.shift(UP*0.7)
        self.play(*[Write(mob) for mob in sine_law if mob.get_width() > 0.01])

        self.wait()
    
    def sine_law(self):
        fs1,fs2,labels,t1,t2,t3,t4,alpha,beta,gamma,alpha_arc,beta_arc,gamma_arc,but,h1,h2,rec_1,rec_2,h1_line,h2_line,h3_line,x,sine_law,alpha_p,alpha_p_arc = self.all_mobs
        # - TRANSFORMATIONS
        show_triange,hide_triange = self.funcs
        C,B,A = labels
        # ----------------- Sine la
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
        self.wait()
        self.remove(sine_law)
        self.play(FadeOut(VGroup(fs1,fs2,but)))
        self.wait()
        
    def cosine_law_A(self):
        labels,t1,t2,t3,t4,alpha,beta,gamma,h1,h2,x,alpha_p,h2_line = self.cosine_mobs
        C,B,A = labels
        cosa_t,cosb_t,cosc_t,frac_string,frac_strings = self.cosine_utils
        show_triange,hide_triange = self.funcs
        strings = [
            ["A","^2=","(","C","+","x",")","^2","+","{h_2}","^2"],
            ["A","^2=","C","^2","+","2","C","x","+","x^2","+","{h_2}","^2"],
            ["A","^2=","C","^2","+","2","C","x","+","B^2"],
            ["A","^2=","B","^2","+","C^2","+","2","C","x"],
            ["A","^2=","B","^2","+","C^2","+","2","C","B",*cosa_t],
            ["A","^2=","B","^2","+","C^2","-","2","B","C",*cosa_t],
        ]
        f = VGroup(*[
            TexMobject(*f,**self.tex_map)
            for f in strings
        ])
        for mob in f[:2]:
            # mob[-1].set_color(self.tex_map["tex_to_color_map"]["h_2"])
            mob[-1].align_to(mob[-3][-1],LEFT)
        f.arrange(DOWN)
        for mob in f[1:]:
            mob.align_to(f[0],LEFT)
            # mob.align_to(f[0],DOWN)
        f.to_edge(DOWN,buff=1)
        f.shift(LEFT)
        f.shift(DOWN)
        n = VGroup(*[self.get_label_numbers(fi) for fi in f])
        # self.add(f,n)
        # ---------------- Animations
        self.play(ApplyFunction(show_triange,t4))
        self.wait()
        LAG = 0.4
        h2_c = h2.copy()
        self.play(
            LaggedStart(
                *[
                    TransformFromCopy(mob,f[0][i])
                    for mob,i in zip([A,C,x],[0,3,5])
                ],
                ApplyMethod(h2_c.move_to,f[0][10]),
                lag_ratio=LAG,
            ),
            LaggedStart(
                Animation(Mobject()),
                Animation(Mobject()),
                Animation(Mobject()),
                Animation(Mobject()),
                *[Write(f[0][i]) for i in [1,2,4,6,7,8,9,12]],
                lag_ratio=LAG*2,
            ),
            run_time=7
        )
        self.wait()
        self.play(ApplyFunction(hide_triange,t4))
        LAG = 0.4
        self.play(
            LaggedStart(
                *[
                    ReplacementTransform(f[0][i].copy(),f[1][j])
                    for i,j in zip(
                        [0,1,3,3,4,4,5,5,7,7,7 ,8 ,10,12],
                        [0,1,2,6,4,8,7,9,3,5,10,11,13,15]
                    )
                ],
                # ApplyMethod(h2.copy().move_to,f[0][10]),
                lag_ratio=0,
            ),
            run_time=7
        )
        brace = Brace(f[1][9:-2],DOWN)
        self.play(GrowFromCenter(brace))
        # self.play(LaggedStart(FocusOn(t3),FocusOn(t3),lag_ratio=0.4))
        self.play(ApplyFunction(show_triange,t3))
        self.play(*[Indicate(mob,run_time=2) for mob in [x,B,h2]])
        B2 = brace.get_tex("B^2")[0]
        B2[0].set_color(self.tex_map["tex_to_color_map"]["B"])
        self.play(Write(B2))
        self.play(
            LaggedStart(
                *[
                    ReplacementTransform(f[1][i].copy(),f[2][j])
                    for i,j in zip(
                        [*range(9)],
                        [*range(9)],
                    )
                ],
                lag_ratio=0,
            ),
            run_time=2
        )
        self.play(ReplacementTransform(B2,f[2][9:]),FadeOut(brace))
        # F 2 - 3
        self.wait(0.5)
        f[3].align_to(f[2],UP)
        self.play(
            *[
                ReplacementTransform(f[2][i],f[3][j])
                for i,j in zip([*range(len(f[2]))],[0,1,5,6,4,8,9,10,7,2,3])
            ],
            run_time=2.5
        )
        but = TexMobject("{\\rm cos}(\\pi\\pm \\alpha)=-{\\rm cos}\\alpha",tex_to_color_map={"\\alpha":RED_A})
        but.to_corner(UL)
        c1 = TexMobject("-","{\\rm cos}","\\alpha","=","{","x","\\over","B","}",**self.tex_map)
        c1[-1].set_color(ORANGE)
        c1.to_edge(RIGHT)
        c1.shift(DOWN)
        c2 = TexMobject("-","B",*cosa_t,"=","x",**self.tex_map)
        c2.move_to(c1).align_to(c1,LEFT).shift(LEFT*c1[0].get_width())
        self.play(Write(but),run_time=2.5)
        self.wait()
        self.play(Write(VGroup(*[c for c in c1 if c.get_width() > 0.1])))
        self.play(ApplyFunction(hide_triange,t3))
        self.wait()
        # self.add(c1,c2)
        # print
        self.play(
            *[ReplacementTransform(c1[i],c2[j]) for i,j in zip(
                                                                [0,1,2,3,5,7],
                                                                [0,2,3,4,5,1]
            )],
            FadeOut(c1[6]),
            run_time=2
        )
        f[4].next_to(f[3],DOWN,aligned_edge=LEFT)
        self.wait()
        self.play(
            *[TransformFromCopy(f[3][i],f[4][j]) for i,j in zip(range(10),range(10))],
            run_time=2
        )
        self.wait()
        self.play(
            *[
                TransformFromCopy(c2[i],f[4][j])
                for i,j in zip([1,2,3],[10,11,12]
            )],
            ApplyMethod(c2[0].move_to,f[4][7]),
            FadeOut(f[4][7]),
            run_time=2
        )
        f[4][7].become(c2[0])
        self.wait()
        f[5].align_to(f[4],UP)
        self.play(*[
            ReplacementTransform(f[4][i],f[5][j])
            for i,j in zip([*range(len(f[4]))],[*range(9),10,9,11,12])
        ])
        self.wait()
        f4 = f[5].copy()
        f4.fade(0.5)
        self.play(Write(f4,stroke_width=6),FadeToColor(f[4],YELLOW,rate_func=there_and_back,run_time=2))
        self.wait()
        self.remove(f4,f[4])
        self.remove(c2[0])
        self.play(
            f[5].scale,0.8,
            f[5].to_corner,DR,{"buff":0.1},
        )
        self.play(
            f[5].set_fill,None,0.5,
            FadeOut(VGroup(*[f[i] for i in [0,1,3]])),
            FadeOut(c2[1:]),FadeOut(h2_c),FadeOut(but)
        )
        self.remove(c2[0])
        self.laws.add(f[5])
        # ---------------------
        # self.add(brace)

    def cosine_law_C(self):
        labels,t1,t2,t3,t4,alpha,beta,gamma,h1,h2,x,alpha_p,h2_line = self.cosine_mobs
        C,B,A = labels
        cosa_t,cosb_t,cosc_t,frac_string,frac_strings = self.cosine_utils
        show_triange,hide_triange = self.funcs
        strings = [
            ["C","^2=","(","A","-","y",")","^2","+","{h_1}","^2"],
            ["C","^2=","A","^2","-","2","A","y","+","y","^2","+","{h_1}","^2"],
            ["C","^2=","A","^2","-","2","A","y","+","B^2"],
            ["C","^2=","A","^2","+","B^2","-","2","A","y"],
            ["C","^2=","A","^2","+","B^2","-","2","A","B",*cosc_t],
        ]
        p1,p2,p3 = t2.get_vertices()
        y_masure = MeasureDistance(Line(p3,h2_line.get_start()),buff=0.2)
        y = y_masure.get_tex("y",**self.tex_map)
        # self.add(y_masure,y)
        # self.add(*[Dot(p) for p in [p2,p3]])
        f = VGroup(*[
            TexMobject(*f,**self.tex_map)
            for f in strings
        ])
        for mob in f[:2]:
            # mob[-1].set_color(self.tex_map["tex_to_color_map"]["h_2"])
            mob[-1].align_to(mob[-3][-1],LEFT)
        f.arrange(DOWN)
        for mob in f[1:]:
            mob.align_to(f[0],LEFT)
            # mob.align_to(f[0],DOWN)
        f.to_edge(DOWN,buff=1)
        f.shift(LEFT)
        # f.shift(DOWN)
        n = VGroup(*[self.get_label_numbers(fi) for fi in f])
        # self.add(f,n)
        # ---------------- Animations
        self.play(LaggedStartMap(FadeIn,y_masure),Write(y))
        self.play(ApplyFunction(show_triange,t1))
        self.wait()
        LAG = 0.4
        h2_c = h1.copy()
        self.play(
            LaggedStart(
                *[
                    TransformFromCopy(mob,f[0][i])
                    for mob,i in zip([C,A,y],[0,3,5])
                ],
                ApplyMethod(h2_c.move_to,f[0][10]),
                lag_ratio=LAG,
            ),
            LaggedStart(
                Animation(Mobject()),
                Animation(Mobject()),
                Animation(Mobject()),
                Animation(Mobject()),
                *[Write(f[0][i]) for i in [1,2,4,6,7,8,9,12]],
                lag_ratio=LAG*2,
            ),
            run_time=7
        )
        self.wait()
        # self.add(n,f)
        self.play(ApplyFunction(hide_triange,t1))
        LAG = 0.4
        self.play(
            LaggedStart(
                *[
                    ReplacementTransform(f[0][i].copy(),f[1][j])
                    for i,j in zip(
                        [0,1,3,3,4,4,5,5,7,7,7 ,8 ,10,12],
                        [0,1,2,6,4,8,7,9,3,5,10,11,13,15]
                    )
                ],
                # ApplyMethod(h2.copy().move_to,f[0][10]),
                lag_ratio=0,
            ),
            run_time=7
        )
        brace = Brace(f[1][9:-2],DOWN)
        self.play(GrowFromCenter(brace))
        # self.play(LaggedStart(FocusOn(t3),FocusOn(t3),lag_ratio=0.4))
        self.play(ApplyFunction(show_triange,t2))
        self.play(*[Indicate(mob,run_time=2) for mob in [y,B,h1]])
        B2 = brace.get_tex("B^2")[0]
        B2[0].set_color(self.tex_map["tex_to_color_map"]["B"])
        self.play(Write(B2))
        self.play(
            LaggedStart(
                *[
                    ReplacementTransform(f[1][i].copy(),f[2][j])
                    for i,j in zip(
                        [*range(9)],
                        [*range(9)],
                    )
                ],
                lag_ratio=0,
            ),
            run_time=2
        )
        self.play(ReplacementTransform(B2,f[2][9:]),FadeOut(brace))
        # F 2 - 3
        self.wait(0.5)
        f[3].align_to(f[2],UP)
        self.play(
            *[
                ReplacementTransform(f[2][i],f[3][j])
                for i,j in zip([*range(len(f[2]))],[0,1,2,3,7,8,9,10,4,5,6])
            ],
            run_time=2.5
        )
        c1 = TexMobject("{\\rm cos}","\\gamma","=","{","y","\\over","B","}",**self.tex_map)
        c1[-1].set_color(ORANGE)
        c1.to_edge(RIGHT)
        c1.shift(DOWN)
        c2 = TexMobject("B",*cosc_t,"=","y",**self.tex_map)
        c2.move_to(c1).align_to(c1,LEFT).shift(LEFT*c1[0].get_width())
        self.play(Write(VGroup(*[c for c in c1 if c.get_width() > 0.1])))
        self.play(ApplyFunction(hide_triange,t2))
        self.wait()
        self.play(
            *[ReplacementTransform(c1[i],c2[j]) for i,j in zip([0,1,2,4,6],[1,2,3,4,0])],
            FadeOut(c1[5]),
            run_time=2
        )
        f[4].next_to(f[3],DOWN,aligned_edge=LEFT)
        self.wait()
        self.play(
            *[TransformFromCopy(f[3][i],f[4][j]) for i,j in zip(range(10),range(10))],
            run_time=2
        )
        self.wait()
        self.play(
            *[TransformFromCopy(c2[i],f[4][j]) for i,j in zip([0,1,2],[10,11,12])],
            run_time=2
        )
        self.wait()
        self.play(FadeOut(c2))
        self.wait()
        f4 = f[4].copy()
        f4.set_fill(None,0)
        self.play(Write(f4,stroke_width=6),FadeToColor(f[4],YELLOW,rate_func=there_and_back,run_time=2))
        self.wait()
        self.laws.add(f[4])
        self.remove(h2_c)
        self.play(FadeOut(f[:4]))
        # self.remove(f4,f[4])
        # self.play(f[5].to_corner,DL)
        # ---------------------
        # self.add(brace)
        
    def cosine_law_B(self):
        labels,t1,t2,t3,t4,alpha,beta,gamma,h1,h2,x,alpha_p,h2_line = self.cosine_mobs
        C,B,A = labels
        cosa_t,cosb_t,cosc_t,frac_string,frac_strings = self.cosine_utils
        show_triange,hide_triange = self.funcs
        strings = [
            ["B","^2","=","x","^2","+","h_2","^2",],
            ["B","^2","=","x","^2","+","A","^2","-","(","C","+","x",")","^2"],
            ["B","^2","=","x","^2","+","A","^2","-","C","^2","-","2","C","x","-","x","^2"],
            ["B","^2","=","A","^2","-","C","^2","-","2","C","x"],
            ["B","^2","=","A","^2","-","C","^2","-","2","C","(","A",*cosb_t,"-","C",")"],
            ["B","^2","=","A","^2","-","C","^2","-","2","C","A",*cosb_t,"+","2","C","^2"],
            ["B","^2","=","A","^2","+","C","^2","-","2","A","C",*cosb_t],
        ]
        c_string = [
            ["A","^2","=","h_2","^2","+","(C","+","x",")","^2"],
            ["A","^2","-","(C","+","x",")","^2","=","h_2","^2"],
            [*cosb_t,"=",*frac_strings(["C","+","x"],["A"])],
            ["A",*cosb_t,"-","C","=","x"]
        ]
        # self.add(y_masure,y)
        # self.add(*[Dot(p) for p in [p2,p3]])
        f = VGroup(*[
            TexMobject(*i,**self.tex_map)
            for i in strings
        ])
        c = VGroup(*[
            TexMobject(*i,**self.tex_map)
            for i in c_string
        ])
        # f[1].remove(f[1][-1])
        for mob,i in zip([f[0],c[0],c[1]],[7,4,11]):
            mob[i][0].set_color(BLUE_B)
            ex = mob[i-1][-1]
            ex.set_color(WHITE)
            mob[i-1].remove(ex)
            mob.add(ex)
        f.arrange(DOWN)
        for mob in f[1:]:
            mob.align_to(f[0],LEFT)
            # mob.align_to(f[0],DOWN)
        f.to_edge(DOWN,buff=0.2)
        f.to_edge(LEFT,buff=0.2)
        c.arrange(DOWN)
        c.to_edge(RIGHT,buff=0.1)
        c.shift(DOWN*1.3)
        c[0].shift(UP*0.3)
        c[1].align_to(c[0][:5],RIGHT)
        c[1].align_to(c[0],UP)
        # f.shift(LEFT)
        # f.shift(DOWN)
        n = VGroup(*[self.get_label_numbers(fi) for fi in f])
        n2 = VGroup(*[self.get_label_numbers(fi) for fi in c])
        # self.add(f,c)
        # -----------------------------------------------------
        # -----------------------------------------------------
        self.play(ApplyFunction(show_triange,t3))
        self.wait()
        LAG = 0.4
        h2_c = h1.copy()
        f.shift(DOWN*0.5+RIGHT*2)
        self.play(
            LaggedStart(
                *[
                    TransformFromCopy(mob,f[0][i])
                    for mob,i in zip([B,x],[0,3])
                ],
                AnimationGroup(   
                    TransformFromCopy(h2[0][0],f[0][6]),
                    TransformFromCopy(h2[0][1],f[0][7]),
                    lag_ratio=0
                ),
                lag_ratio=LAG,
            ),
            LaggedStart(
                Animation(Mobject()),
                Animation(Mobject()),
                Animation(Mobject()),
                Animation(Mobject()),
                *[Write(f[0][i]) for i in [1,2,4,5,8]],
                lag_ratio=LAG*2,
            ),
            run_time=7
        )
        self.wait()
        # self.add(n,f)
        self.play(ApplyFunction(hide_triange,t3))
        self.wait()
        self.play(ApplyFunction(show_triange,t4))
        self.wait()
        self.play(
            LaggedStart(
                *[
                    TransformFromCopy(mob,c[0][i])
                    for mob,i in zip([A],[0])
                ],
                AnimationGroup(   
                    TransformFromCopy(h2[0][0],c[0][3]),
                    TransformFromCopy(h2[0][1],c[0][4]),
                    lag_ratio=0
                ),
                *[
                    TransformFromCopy(mob,c[0][i])
                    for mob,i in zip([C,x],[7,9])
                ],
                lag_ratio=LAG,
            ),
            LaggedStart(
                Animation(Mobject()),
                Animation(Mobject()),
                Animation(Mobject()),
                Animation(Mobject()),
                *[Write(c[0][i]) for i in [1,2,12,5,6,8,10,11]],
                lag_ratio=LAG*2,
            ),
            run_time=7
        )
        self.wait()
        self.play(*[
            ReplacementTransform(c[0][i],c[1][j])
            for i,j in zip(range(len(c[0])),[0,1,9,10,11,2,3,4,5,6,7,8,12])
        ],run_time=3)
        self.wait()
        self.play(*[TransformFromCopy(f[0][i],f[1][j])
            for i,j in zip(range(6),range(6))
        ])
        self.wait()
        self.play(*[TransformFromCopy(c[1][i],f[1][j])
            for i,j in zip(range(9),range(6,15))
        ],run_time=3.5)
        self.wait()
        self.play(ApplyFunction(hide_triange,t4))
        self.wait()
        self.play(c[1].to_edge,RIGHT,c[1].fade,1)
        self.wait()
        self.play(*[ReplacementTransform(f[1][i].copy(),f[2][j])
            for i,j in zip([*range(9),10,10,11,11,12,12,14,14,14],
                           [*range(9),9, 13,11,15,14,16,10,12,17]
                    )
        ],run_time=3.5)
        self.wait()
        self.play(*[
            ApplyMethod(f[2][i].fade,0.7)
            for i in [3,4,15,16,17]
        ])
        self.wait()
        self.play(*[ReplacementTransform(f[2][i].copy(),f[3][j])
            for i,j in zip([*range(3),*range(6,15)],
                           [*range(len(f[3]))]
                    )
        ],run_time=3.5)
        self.wait()
        # --------- Show cos beta = (c+x) / a
        self.play(ApplyFunction(show_triange,t4))
        self.wait()
        self.play(
            LaggedStart(
                Write(c[2][0]),
                TransformFromCopy(beta,c[2][1]),
                Animation(Mobject()),
                Write(c[2][2]),
                TransformFromCopy(C,c[2][4]),
                Animation(Mobject()),
                Write(c[2][5]),
                TransformFromCopy(x,c[2][6]),
                Animation(Mobject()),
                Write(c[2][7]),
                TransformFromCopy(A,c[2][8]),
                lag_ratio=0.4
            ),
            run_time=10
        )
        self.wait()
        c[3].shift(LEFT*abs(c[2][2].get_x()-c[3][5].get_x()))
        c[3].align_to(c[2][1],UP)
        self.play(
            FadeOut(c[2][7]),
            *[
            ReplacementTransform(c[2][i],c[3][j])
            for i,j in zip(
                [0,1,2,4,5,6,8],
                [1,2,5,4,3,6,0]
            )
        ],run_time=4)
        # ---------------- Trabsfirn 2Cx to 2C(Acos beta + C)
        self.wait()
        self.play(
            *[TransformFromCopy(f[3][i],f[4][j]) for i,j in zip(range(11),range(11))],
            *[Write(f[4][i]) for i in [11,17]],
            *[TransformFromCopy(c[3][i],f[4][j]) for i,j in zip(range(5),range(12,17))],
            run_time=4
        )
        self.wait()
        self.play(ApplyFunction(hide_triange,t4))
        self.play(c[3].to_edge,RIGHT,c[3].fade,1)
        # ---------------- Expand 2C(Acos beta + C)
        self.wait()
        self.play(
            *[ReplacementTransform(f[4][i].copy(),f[5][j]) for i,j in zip(range(9),range(9))],
            *[ReplacementTransform(f[4][i].copy(),f[5][j]) for i,j in zip(
                [9,9, 10,10,12,13,14,15,16],
                [9,15,10,16,11,12,13,14,16])
            ],
            AnimationGroup(
                Animation(Mobject()),
                Animation(Mobject()),
                Write(f[5][-1]),
                lag_ratio=1
            ),
            run_time=4
        )
        # ------------------------------ LAST
        f[6].align_to(f[5],UP)
        self.wait()
        self.play(*[ShowCreationThenDestructionAround(i,run_time=2.3) for i in [f[5][6:8],f[5][15:]]])
        self.wait()
        self.play(
            *[
                ReplacementTransform(f[5][i],f[6][j])
                for i,j in zip(
                    [*range(10),10,11,12,13,14,16,17],
                    [*range(10),11,10,12,13, 5,6 ,7]
                )
            ],
            FadeOut(f[5][15]),
            run_time=4
        )
        # ------ Show
        f4 = f[6].copy()
        f4.set_fill(None,0)
        self.wait()
        self.play(Write(f4,stroke_width=6),FadeToColor(f[6],YELLOW,rate_func=there_and_back,run_time=2))
        self.wait()
        self.play(
            f[6].scale,0.8,
            f[6].next_to,self.laws[-1],UP,0.2,
            f[6].align_to,self.laws[-1],LEFT,
            f[6].set_fill,None,0.5
        )
        self.laws.add(f[6])
        self.play(FadeOut(f[:5]))

    
    def get_label_numbers(self,formula,**tex_kwargs):
        n = VGroup()
        for i,e in enumerate(formula):
            t = Text(f"{i}",font="DejaVu").set_height(0.2)
            t.next_to(e,DOWN,0)
            if e.get_width() > 0.01:
                n.add(t)
            # else:
            #     n.add(t)
        return n
    
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
