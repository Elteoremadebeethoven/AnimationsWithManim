from manimlib.imports import *

class SuccessionExample1(Scene):
    def construct(self):
        number_line=NumberLine(x_min=-2,x_max=2)
        text=TextMobject("Text")\
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
                        Animation(Mobject(),run_time=2.1),
                        Write(text),lag_ratio=1
                    )
            )
        self.wait()

class SuccessionExample2(Scene):
    def construct(self):
        number_line=NumberLine(x_min=-2,x_max=2)
        triangle=RegularPolygon(3,start_angle=-PI/2)\
                   .scale(0.2)\
                   .next_to(number_line.get_left(),UP,buff=SMALL_BUFF)
        text_1=TextMobject("1")\
               .next_to(number_line.get_tick(-1),DOWN)
        text_2=TextMobject("2")\
               .next_to(number_line.get_tick(0),DOWN)
        text_3=TextMobject("3")\
               .next_to(number_line.get_tick(1),DOWN)
        text_4=TextMobject("4")\
               .next_to(number_line.get_tick(2),DOWN)

        self.add(number_line)
        self.play(ShowCreation(triangle))
        self.wait(0.3)
        
        self.play(
                    ApplyMethod(triangle.shift,RIGHT*4,rate_func=linear,run_time=4),
                    AnimationGroup(
                        Animation(Mobject(),run_time=1),
                        Write(text_1),lag_ratio=1
                    ),
                    AnimationGroup(
                        Animation(Mobject(),run_time=2),
                        Write(text_2),lag_ratio=1
                    ),
                    AnimationGroup(
                        Animation(Mobject(),run_time=3),
                        Write(text_3),lag_ratio=1
                    ),
                    AnimationGroup(
                        Animation(Mobject(),run_time=4),
                        Write(text_4),lag_ratio=1
                    )
            )

        self.wait()

class SuccessionExample2Compact(Scene):
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
                        Animation(Mobject(),run_time=i+1),
                        Write(numbers[i]),lag_ratio=1
                    )for i in range(4)],
            )

        self.wait()

class SuccessionExample3(Scene):
    def construct(self):
        number_line=NumberLine(x_min=-2,x_max=2)
        text_1=TextMobject("Theorem of")\
             .next_to(number_line,DOWN)
        text_2=TextMobject("Beethoven")\
             .next_to(number_line,DOWN)
        dashed_line=DashedLine(
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
                        ReplacementTransform(text_1,text_2),lag_ratio=1
                    )
            )

        self.wait()
