from manimlib.imports import *

class ExampleRateFunc(Scene):
    def construct(self):
        path = Line(LEFT*5,RIGHT*5)
        dot = Dot(path.get_start())
        self.add(path,dot)
        self.play(
            # This works with any animation
            MoveAlongPath(
                dot,path,
                rate_func=lambda t: smooth(1-t),
                # rate_func = smooth <- by default
                run_time=4 # 4 sec
            )
        )
        self.wait()

class ExampleRateFunc2(Scene):
    def construct(self):
        text = TextMobject("Hello world!").scale(3)
        self.play(Write(
            text,
            rate_func=lambda t: smooth(1-t)
        ))
        self.wait()

# Install via pip:
# matplotlib
# pandas
# sklearn
import matplotlib.pyplot as plt 
import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures 

class ExampleRateFuncCustom(Scene):
    def construct(self):
        datas = pd.read_csv('data.csv')
        print(datas)
        X = datas.iloc[:, 0:1].values
        y = datas.iloc[:, 1].values
        poly = PolynomialFeatures(degree = 8)
        X_poly = poly.fit_transform(X)
        poly.fit(X_poly, y)
        lin = LinearRegression()
        lin.fit(X_poly, y)
        plt.scatter(X, y, color = 'blue') 
  
        plt.plot(X, lin.predict(poly.fit_transform(X)), color = 'red') 
        plt.title('Polynomial Regression') 
        plt.xlabel('Time') 
        plt.ylabel('Animation progression %') 
        plt.show() 
        # See manimlib/utils/bezier.py
        reg_func = bezier(lin.predict(poly.fit_transform(X)))

        path = Line(LEFT*5,RIGHT*5)
        dot = Dot(path.get_start())
        self.add(path,dot)
        self.play(
            MoveAlongPath(
                dot,path,
                rate_func=reg_func,
                run_time=4
            )
        )
        self.wait()

# Custom

def custom_time(t,partitions,start,end,func):
    duration = end - start
    fragment_time = 1 / partitions
    start_time = start * fragment_time
    end_time = end * fragment_time
    duration_time = duration * fragment_time
    def fix_time(x):
        return (x - start_time) / duration_time
    if t < start_time: 
        return func(fix_time(start_time))
    elif start_time <= t < end_time:
        return func(fix_time(t))
    else:
        return func(fix_time(end_time))

def Custom(partitions,start,end,func=smooth):
    return lambda t: custom_time(t,partitions,start,end,func)

class CustomRateFunc(Scene):
    def construct(self):
        c = Circle().scale(2)
        s = Square().scale(2)
        l = Line(DOWN,UP).scale(2)
        time = DecimalNumber(self.time).add_updater(lambda m: m.set_value(self.time))
        time.to_corner(DL)
        self.add(time)
        self.play(
            # 6 partitions, that is (total_time = 4):
            # ShowCreation starts at t=(0/6)*total_time=0s and end t=(5/6)*total_time=3.333s
            ShowCreation(c,  rate_func=Custom(6,0,5)),
            # FadeIn starts at t=(2/6)*total_time=1.3333s and end t=(4/6)*total_time=2.6666s
            FadeIn(s,        rate_func=Custom(6,2,4,func=there_and_back)),
            # GrowFromCenter starts at t=(4/6)*total_time=2.6666s and end t=(6/6)*total_time=4s
            GrowFromCenter(l,rate_func=Custom(6,4,6)),
            run_time=4 # <- total_time
            )
        self.wait()

# COMPARATION
class TestPath(VGroup):
    def __init__(self,name,**kwargs):
        super().__init__(**kwargs)
        self.name = name.__name__
        self.func = name
        self.title = Text(f"{self.name}",font="Monaco",stroke_width=0)
        self.title.set_height(0.24)
        self.line = Line(LEFT*5,RIGHT*5)
        self.dot = Dot(self.line.get_start())
        self.title.next_to(self.line,LEFT,buff=0.3)
        self.add(self.title,self.line,self.dot)

class RateFunctions(Scene):
    CONFIG = {
        "rate_functions": [
            smooth,
            linear,
            rush_into,
            rush_from,
            slow_into,
            double_smooth,
            there_and_back,
            running_start,
            wiggle,
            lingering,
            exponential_decay
        ],
        "rt": 3
    }
    def construct(self):
        time_ad = [*[Text("%d"%i,font="Arial",stroke_width=0).to_corner(UL) for i in range(1,4)]][::-1]
        
        rf_group = VGroup(*[
            TestPath(rf)
            for rf in self.rate_functions
        ])
        for rf in rf_group:
            rf.title.set_color(TEAL)
            rf.line.set_color([RED,BLUE,YELLOW])
        rf_group.arrange(DOWN,aligned_edge=RIGHT)
        init_point = rf_group[0].line.get_start()
        init_point[0] = 0
        end_point = rf_group[-1].line.get_end()
        brace = Brace(rf_group[-1].line,DOWN,buff=0.5)
        brace_text = brace.get_text("\\tt run\\_time = %d"%self.rt).scale(0.8)
        end_point[0] = 0

        div_lines = VGroup()
        div_texts = VGroup()
        for i in range(11):
            proportion = i / 10
            text = TexMobject("\\frac{%s}{10}"%i)
            text.set_height(0.5)
            coord_proportion = rf_group[0].line.point_from_proportion(proportion)
            coord_proportion[1] = 0
            v_line = DashedLine(
                init_point + coord_proportion + UP*0.5,
                end_point  + coord_proportion + DOWN*0.5,
                stroke_opacity=0.5
            )
            text.next_to(v_line,UP,buff=0.1)
            div_texts.add(text)
            div_lines.add(v_line)
        self.add(rf_group,div_lines,div_texts,brace,brace_text)
        for i in range(3):
            self.add(time_ad[i])
            self.wait()
            self.remove(time_ad[i])
        self.play(*[
            MoveAlongPath(vg.dot,vg.line,rate_func=vg.func)
            for vg in rf_group 
            ],
            run_time=self.rt
        )
        self.wait(2)
