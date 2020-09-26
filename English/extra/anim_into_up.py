from manimlib.imports import *

class ExampleFail(Scene):
    def construct(self):
        triangle = Triangle()
        square = Square()
        triangle.add_updater(lambda mob, dt: mob.shift(RIGHT * 0.1))
        # triangle anim
        anim1 = Write(triangle, run_time=1)
        # square anim
        anim2 = FadeIn(square, rate_func=there_and_back)
        self.add(triangle)
        turn_animation_into_updater(anim1)
        self.wait(0.4)
        self.add(square)
        turn_animation_into_updater(anim2)
        self.wait(3)

class ExamplePreSolution(Scene):
    def construct(self):
        triangle = Triangle()
        square = Square()
        frame = 1 / self.camera.frame_rate

        def update_triangle(mob, dt):
            if mob.get_x() < 3:
                mob.shift(RIGHT * frame)

        triangle.add_updater(update_triangle)
        anim1 = Write(triangle,run_time=1)
        anim2 = FadeIn(square,rate_func=there_and_back)
        self.add(triangle)
        turn_animation_into_updater(anim1)
        self.wait(0.4)
        self.add(square)
        turn_animation_into_updater(anim2, cycle=True)
        self.wait(3)


def update_move_mob_func(mob, end_coord, fps, run_time=2, func=linear):
    DISTANCE = get_norm(mob.get_center() - end_coord)
    VECTOR = end_coord - mob.get_center()
    UNIT_VECTOR = normalize(VECTOR)
    mob.start_time = 0
    mob.start_coord = mob.get_center()

    def update(mob, dt):
        mob.start_time += fps
        if mob.start_time < run_time:
            alpha = mob.start_time / run_time
            alpha_func = func(alpha)
            mob.move_to(mob.start_coord)
            mob.shift(UNIT_VECTOR * alpha_func * DISTANCE)

    return update

class Example(Scene):
    def construct(self):
        text = TextMobject("Hello world")
        fps = 1 / self.camera.frame_rate
        update_text = update_move_mob_func(
            text,
            [1, 2, 0], # End point
            fps, # fps
            func=smooth,
            run_time=3
        )
        text.add_updater(update_text)
        anim = Write(text, run_time=3)
        self.add(text)
        turn_animation_into_updater(anim)
        self.wait(5)

class Example2(Scene):
    def construct(self):
        triangle = Triangle()
        square = Square()
        triangle.add_updater(lambda mob, dt: mob.rotate(1 * DEGREES))
        anim1 = FadeToColor(triangle, RED)
        self.add(triangle)
        cycle_animation(
            anim1,
            run_time=3,
            rate_func=there_and_back
        )
        self.wait()
        self.play(Write(TextMobject("Hello world!",height=1)))
        self.wait(3)
        triangle.clear_updaters()
        self.play(FadeOut(triangle))
        self.wait(2)

# INTRO VIDEO
class IntroVid(Scene):
    def construct(self):
        text = TextMobject("Hello world!").scale(2)
        text.shift(LEFT * 2)
        frame = 1 / self.camera.frame_rate
        update_text = update_move_mob_func(
            text,
            text.get_center() + np.array([4, 0, 0]), # End point
            frame, # fps
            func=smooth,
            run_time=3
        )
        self.add(text)
        turn_animation_into_updater(anim)
        self.wait(5)
