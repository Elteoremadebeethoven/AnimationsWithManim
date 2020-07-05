from manimlib.imports import *

class AnimationGroupExampleFail(Scene):
    def construct(self):
        dots = VGroup(*[Dot() for _ in range(10)])
        dots.arrange(RIGHT,buff=0.8)
        self.add(dots)
        for dot in dots:
            self.play(
                dot.scale,3,
                dot.set_color,RED,
                rate_func=there_and_back
            )
        self.wait(2)

class AnimationGroupExample(Scene):
    def construct(self):
        dots = VGroup(*[Dot() for _ in range(10)])
        dots.arrange(RIGHT, buff=0.8)
        self.add(dots)

        def dot_func(mob):
            mob.scale(3)
            mob.set_color(RED)
            return mob

        self.play(
            # Replace AnimationGroup with LaggedStart
            LaggedStart(
                *[
                   ApplyFunction(
                       dot_func,
                       dot,
                       rate_func=there_and_back
                    )
                   for dot in dots
                ] 
            )
        )
        self.wait(2)

class AbsctractScene(Scene):
    CONFIG = {
        "anim_kwargs": {"rate_func": there_and_back}
    }
    def setup(self):
        dots = VGroup(*[Dot() for _ in range(10)])
        dots.arrange(RIGHT, buff=0.8)
        # Save the state
        dots.save_state()

        def dot_func(mob):
            mob.scale(3)
            mob.set_color(RED)
            return mob

        self.dots = dots
        self.dot_func = dot_func
        self.add(self.dots)

# LaggedStart != LaggedStartMap (recent version)
# BUT LaggedStartMap (recent version) == LaggedStart (3/feb version)
class LaggedStartMapExample(AbsctractScene):
    def construct(self):
        self.play(
            LaggedStartMap(
                GrowFromCenter,
                self.dots
            )
        )
        self.wait()

class LaggedStartMapExample2(AbsctractScene):
    def construct(self):
        self.play(
            LaggedStartMap(
                GrowFromCenter,
                self.dots,
                rate_func=there_and_back
            )
        )
        self.wait()
        # What happens if remove the following line?
        self.dots.restore()
        self.play(
            LaggedStart(*[
                GrowFromCenter(
                    dot,
                    rate_func=there_and_back
                ) 
                for dot in self.dots
                ],
            )
        )
        # In summary, LaggedStartMap is a way
        # to run LaggedStart without applying
        # the spread (splat) operator.
        # But it only applies to animations 
        # that receive a Mobject as the only argument:
        # Examples: Write, FadeIn, GrowFromCenter, ShowCreation, MoveToTarget, etc.
        self.wait(2)

# Way to put more arguments in LaggedStartMap
class LaggedStartMapExample3(AbsctractScene):
    def construct(self):
        self.play(
            LaggedStartMap(
                FadeInFrom, # This receives 2 arguments:
                # Mobject and Direction
                self.dots,
                lambda mob: (mob, UP),
            )
        )
        self.wait()

class AnimationGroupExampleLagRatios(AbsctractScene):
    CONFIG = {
        "lag_ratios": list(np.arange(0,1.1,.1)) # (0, 0.1, 0.2 ... 1)
    }
    def construct(self):
        self.remove(self.dots)
        labels = VGroup(*[
            Text("lag_ratio: %.1f   -"%lg,stroke_width=0,font="Arial").set_height(0.4)
            for lg in self.lag_ratios
        ])
        set_dots = VGroup(*[
            self.dots.copy() for _ in self.lag_ratios
        ])
        set_dots.arrange(DOWN,buff=0.5)
        set_dots.to_edge(RIGHT)
        for label, dots in zip(labels,set_dots):
            label.next_to(dots,LEFT,buff=0.4)
    
        self.add(labels,set_dots)
        self.play(*[
            AnimationGroup(*[
                ApplyFunction(
                    self.dot_func,
                    dot,
                    rate_func=there_and_back
                ) 
                for dot in dots
                ],
                lag_ratio=lg
            )
            for dots,lg in zip(set_dots,self.lag_ratios)
        ])
        self.wait()

# Successions vs AnimationGroup
#      AnimationGroup
class AnimationGroupExample1(Scene):
    def construct(self):
        number_line = NumberLine(x_min=-2,x_max=2)
        text = TextMobject("Text")\
             .next_to(number_line,DOWN)
        dashed_line=DashedLine(
                                number_line.get_left(),
                                number_line.get_right(),
                                color=YELLOW,
                              ).set_stroke(width=11)

        self.add(number_line)
        self.wait(0.3)
        
        self.play(
                    LaggedStart(
                        *[ShowCreationThenDestruction(dashed_segment)
                        for dashed_segment in dashed_line],
                        run_time=5
                    ),
                    AnimationGroup(
                        Animation(Mobject(),run_time=2.1), # PAUSE
                        Write(text),lag_ratio=1
                    )
            )
        self.wait()

class AnimationGroupExample2(Scene):
    def construct(self):
        number_line = NumberLine(x_min=-2,x_max=2)
        triangle = RegularPolygon(3,start_angle=-PI/2)\
                   .scale(0.2)\
                   .next_to(number_line.get_left(),UP,buff=SMALL_BUFF)
        text_1 = TextMobject("1")\
               .next_to(number_line.get_tick(-1),DOWN)
        text_2 = TextMobject("2")\
               .next_to(number_line.get_tick(0),DOWN)
        text_3 = TextMobject("3")\
               .next_to(number_line.get_tick(1),DOWN)
        text_4 = TextMobject("4")\
               .next_to(number_line.get_tick(2),DOWN)

        self.add(number_line)
        self.play(ShowCreation(triangle))
        self.wait(0.3)
        
        self.play(
                    # Pauses are referenced to the beginning of the play
                    # ================================================== 
                    ApplyMethod(triangle.shift,RIGHT*4,rate_func=linear,run_time=4),
                    AnimationGroup(
                        Animation(Mobject(),run_time=1), # 1 second pause
                        Write(text_1),lag_ratio=1
                    ),
                    AnimationGroup(
                        Animation(Mobject(),run_time=2), # 2 seconds pause
                        Write(text_2),lag_ratio=1
                    ),
                    AnimationGroup(
                        Animation(Mobject(),run_time=3), # 3 seconds pause
                        Write(text_3),lag_ratio=1
                    ),
                    AnimationGroup(
                        Animation(Mobject(),run_time=4), # 4 seconds pause
                        Write(text_4),lag_ratio=1
                    )
            )
        self.wait()

class Pause(Animation):
    def __init__(self, duration):
        super().__init__(Mobject(), run_time=duration)

class AnimationGroupExample2Compact(Scene):
    def construct(self):
        number_line=NumberLine(x_min=-2,x_max=2)
        triangle=RegularPolygon(3,start_angle=-PI/2)\
                   .scale(0.2)\
                   .next_to(number_line.get_left(),UP,buff=SMALL_BUFF)
        numbers=VGroup(
             *[TextMobject("%s"%i)\
              .next_to(number_line.get_tick(i-2),DOWN) for i in range(1,5)]
            )

        self.add(number_line)
        self.play(ShowCreation(triangle))
        self.wait(0.3)
        
        self.play(
                    ApplyMethod(triangle.shift,RIGHT*4,rate_func=linear,run_time=4),
                    *[AnimationGroup(
                        # Animation(Mobject(),run_time=i+1), # <- This is a pause
                        Pause(i+1),
                        Write(numbers[i]),lag_ratio=1
                    )for i in range(4)],
            )
        self.wait()

class AnimationGroupExample3(Scene):
    def construct(self):
        number_line = NumberLine(x_min=-2,x_max=2)
        text_1 = TextMobject("Theorem of")\
             .next_to(number_line,DOWN)
        text_2 = TextMobject("Beethoven")\
             .next_to(number_line,DOWN)
        dashed_line = DashedLine(
                                number_line.get_left(),
                                number_line.get_right(),
                                color=YELLOW,
                              ).set_stroke(width=11)

        self.add(number_line,text_1)
        
        self.play(
                    LaggedStart(
                        *[ShowCreationThenDestruction(dashed_segment)
                        for dashed_segment in dashed_line],
                        run_time=5
                    ),
                    AnimationGroup(
                        Animation(Mobject(),run_time=2.1),
                        # Pause(2.1)
                        ReplacementTransform(text_1,text_2),lag_ratio=1
                    )
            )

        self.wait()

#       Successions
class AnimationGroupFail1(Scene):
    def construct(self):
        text1 = TextMobject("Theorem")
        text2 = TextMobject("of")
        text3 = TextMobject("Beethoven")
        for text in text1,text2,text3:
            text.scale(3)
        self.add(text1)
        self.play(
            AnimationGroup(
                ReplacementTransform(text1,text2),
                ReplacementTransform(text2,text3),
                lag_ratio=1
            )
        )
        self.wait()

class AnimationGroupFail2(Scene):
    def construct(self):
        text1 = TextMobject("Theorem")
        text2 = TextMobject("of")
        text3 = TextMobject("Beethoven")
        for text in text1,text2,text3:
            text.scale(3)
        self.add(text1)
        self.play(
            AnimationGroup(
                Transform(text1,text2),
                Transform(text1,text3),
                lag_ratio=1
            )
        )
        self.wait()

class Succession1(Scene):
    def construct(self):
        text1 = TextMobject("Theorem")
        text2 = TextMobject("of")
        text3 = TextMobject("Beethoven")
        for text in text1,text2,text3:
            text.scale(3)
        self.add(text1)
        self.play(
            Succession(
                Transform(text1,text2),
                Transform(text1,text3),
                lag_ratio=1.2
            )
        )
        self.wait()

# Real example

class ClockOrganization(VGroup):
    CONFIG = {
        "numbers" : 4,
        "radius" : 3.1,
        "color" : WHITE
    }
    def __init__(self, **kwargs):
        digest_config(self, kwargs, locals())
        self.generate_nodes()
        VGroup.__init__(self, *self.node_list,**kwargs)

    def generate_nodes(self):
        self.node_list = []
        for i in range(self.numbers):
            mobject = VMobject()
            number = TexMobject(str(i+1))
            circle = Circle(radius=0.4,color=self.color)
            mobject.add(number)
            mobject.add(circle)
            mobject.move_to(
                self.radius * np.cos((-TAU / self.numbers) * i + 17*TAU / 84) * RIGHT
                + self.radius * np.sin((-TAU / self.numbers) * i + 17*TAU / 84) * UP
            )
            self.node_list.append(mobject)

    def select_node(self, node):
        selected_node = self.node_list[node]
        selected_node.scale(1.2)
        selected_node.set_color(RED)

    def deselect_node(self, selected_node):
        node = self.node_list[selected_node]
        node.scale(0.8)
        node.set_color(self.color)

class ClockOrganizationScene(Scene):
    def construct(self):
        test = ClockOrganization(numbers=21)
        self.add(test)
        animation_steps = []
        num_circ = 15
        for i in range(num_circ):
            thing = test.deepcopy()
            thing.select_node((19+i)%test.numbers-1)
            animation_steps.append(thing)
        anims = []
        theta = 180 * DEGREES / num_circ
        lag_constant = 5
        for i in range(1,num_circ):
            test.node_list[(19+i)%test.numbers-1].generate_target()
            test.node_list[(19+i)%test.numbers-1].target.scale(1.2)
            test.node_list[(19+i)%test.numbers-1].target.set_color(RED)
            stop_smooth = lag_constant * np.sin(i*theta)
            anims.append(MoveToTarget(test.node_list[(19+i)%test.numbers-1],rate_func=there_and_back))
            anims.append(Animation(Mobject(),run_time=stop_smooth))
        self.play(
            AnimationGroup(*anims,lag_ratio=0.1)
            )
        self.wait()
