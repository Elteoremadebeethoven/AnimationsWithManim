from manimlib.imports import *

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