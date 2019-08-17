class AudioTest(Scene):
    def construct(self):
        group_dots=VGroup(*[Dot()for _ in range(3)])
        group_dots.arrange_submobjects(RIGHT)
        for dot in group_dots:
            self.add_sound("click",gain=-10)
            self.add(dot)
            self.wait()
        self.wait()
 
class SVGTest(Scene):
    def construct(self):
        svg = SVGMobject("finger")
        #svg = SVGMobject("camera")
        self.play(DrawBorderThenFill(svg,rate_func=linear))
        self.wait()
 
class ImageTest(Scene):
    def construct(self):
        image = ImageMobject("note")
        self.play(FadeIn(image))
        self.wait()
