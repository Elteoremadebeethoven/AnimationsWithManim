from big_ol_pile_of_manim_imports import *

class SoundTest(Scene):
    CONFIG = {"include_sound": True}
    def construct(self):
        title=TextMobject("Sound Test").to_edge(UP)
        self.wait()
        self.add_sound("sound",gain=-10)
        self.play(Write(title))
