from manimlib.imports import *

class OrderMobjects(Scene):
    def construct(self):
        mobs = VGroup(*[mob.set_height(4) for mob in [Square(),Circle(),Triangle()]])
        mobs.set_fill(opacity=1)
        for i in range(1,3):
            mobs[i].next_to(mobs[i-1].get_left(),RIGHT,buff=1)
        mobs.move_to(ORIGIN)
        self.add(*mobs)
        self.wait()
        # Array
        print(self.mobjects) # [Square, Circle, Rectangle]
        for mob in self.mobjects:
            name = mob.__class__.__name__
            print(f"Remove {name}")
            self.remove(mob)
            self.wait()
        self.wait()

"""
CONCLUSION
==========

Every time we use self.add(mob) we are
                  -------------
adding the objects to the self.mobjects 
                          -------------
array, depending on the order in which 

they appear in the array, they will also 

be on the screen.


It is important that when using the update 

functions you are aware of the order of your 

objects in self.mobjects, so that the animation 
           -------------
is displayed correctly.
"""

class OrderMobjects2(Scene):
    def construct(self):
        mobs = VGroup(*[mob.set_height(4) for mob in [Square(),Circle(),Triangle()]])
        mobs.set_fill(opacity=1)
        for i in range(1,3):
            mobs[i].next_to(mobs[i-1].get_left(),RIGHT,buff=1)
        mobs.move_to(ORIGIN)

        self.add(*mobs)
        self.wait()
        # Random reorganization
        random.shuffle(self.mobjects)
        self.wait()

# dt = 1 / fps

class AbstractDtScene(Scene):
    def setup(self):
        path = Line(LEFT*6, RIGHT*6)
        measure = VGroup()
        for i in range(61):
            proportion = 1 / 60
            line = Line(DOWN*0.3, UP*0.3, stroke_width=2)
            line.move_to(path.point_from_proportion(proportion*i))
            measure.add(line)
            if i in [15,30,60]:
                arrow = Arrow(UP,DOWN)
                arrow.next_to(line,UP,buff=0.1)
                text = Text(f"{i}",font="Arial",stroke_width=0)
                text.set_height(0.5)
                text.next_to(arrow,UP)
                self.add(arrow,text)
        measure.add(path)
        # Measure lines
        self.measure = measure
        self.measure.start = path.point_from_proportion(0)
        # Distance between every line
        self.dot_distance = path.point_from_proportion(1/60) - path.point_from_proportion(0)
        # dot at start
        self.dot = Dot(self.measure.start,color=RED)
        self.add(self.measure)

class DtExample1Fail(AbstractDtScene):
    def construct(self):
        def update_dot(mob):
            mob.shift(RIGHT * self.dot_distance)

        dot = self.dot
        dot.add_updater(update_dot)

        self.add(dot)
        self.wait()
        dot.clear_updaters()
        self.wait()

class DtExample1(AbstractDtScene):
    def construct(self):
        # Calculate dt:
        dt_calculate = 1 / self.camera.frame_rate
        print(f"dt calculate = {dt_calculate}")
        print("---------------------------------")
        def update_dot(mob,dt):
            print(f"n: {mob.counter} - dt : {dt}")
            mob.shift(RIGHT * self.dot_distance)
            mob.counter += 1

        dot = self.dot
        dot.counter = 0
        dot.add_updater(update_dot)
        self.add(dot)

        self.wait()
        dot.clear_updaters()
        self.wait()

class DtExample2(AbstractDtScene):
    CONFIG = {
        "velocity_factor": 15
    }
    def construct(self):
        # Calculate dt:
        self.dt_calculate = 1 / self.camera.frame_rate
        print(f"dt calculate = {self.dt_calculate}")
        print("---------------------------------")
        def update_dot(mob,dt):
            if dt == 0 and mob.counter==0:
                rate = self.velocity_factor * self.dt_calculate
                mob.counter += 1
            else:
                rate = dt * self.velocity_factor
            if dt > 0:
                mob.counter=0
            print(f"n: {mob.counter} - dt : {dt}")
            mob.shift(RIGHT * rate * self.dot_distance)
            mob.counter += 1

        dot = self.dot
        dot.counter = 0
        dot.add_updater(update_dot)
        self.add(dot)

        self.wait(2)
        dot.clear_updaters()
        self.wait()

def fix_update(mob,dt,velocity_factor,dt_calculate):
    if dt == 0 and mob.counter == 0:
        rate = velocity_factor * dt_calculate
        mob.counter += 1
    else:
        rate = dt * velocity_factor
    if dt > 0:
        mob.counter = 0
    return rate

class DtExample3(AbstractDtScene):
    def construct(self):
        # Calculate dt:
        self.dt_calculate = 1 / self.camera.frame_rate
        print(f"dt calculate = {self.dt_calculate}")
        print("---------------------------------")
        def update_dot(mob,dt):
            rate = fix_update(mob,dt,15,self.dt_calculate)
            print(f"n: {mob.counter} - dt : {dt}")
            mob.shift(RIGHT * rate * self.dot_distance)
            mob.counter += 1

        dot = self.dot
        dot.counter = 0
        dot.add_updater(update_dot)
        self.add(dot)

        self.wait(2)
        dot.clear_updaters()
        self.wait()

class UpdateFunctionWithDt1Fail(Scene):
    CONFIG={
        "amp": 2.3,
        "t_offset": 0,
        "rate": TAU/4,
        "sine_graph_config":{
            "x_min": -TAU/2,
            "x_max": TAU/2,
            "color": RED,
            },
    }
    def construct(self):
        def update_curve(c, dt):
            rate = self.rate * dt
            c.become(self.get_sin_graph(self.t_offset + rate))
            # Every frame, the t_offset increase rate / fps
            self.t_offset += rate

        c = self.get_sin_graph(0)
        self.play(ShowCreation(c))

        # PRINTS
        print(f"fps: {self.camera.frame_rate}")
        print(f"dt: {1 / self.camera.frame_rate}")
        print(f"rate: {self.rate / self.camera.frame_rate}")
        print(f"cy_start: {c.points[0][1]}")
        print(f"cy_end:   {c.points[-1][1]}")
        print(f"t_offset: {self.t_offset}\n")

        c.add_updater(update_curve)
        self.add(c)

        # The animation begins
        self.wait(4)
        
        c.remove_updater(update_curve)
        self.wait()

        print(f"cy_start:  {c.points[0][1]}")
        print(f"cy_end:    {c.points[-1][1]}")
        print(f"t_offset: {self.t_offset}\n")

    def get_sin_graph(self, dx):
        c = FunctionGraph(
                lambda x: self.amp * np.sin(x - dx),
                **self.sine_graph_config
                )
        return c

class UpdateFunctionWithDt1(Scene):
    CONFIG={
        "amp": 2.3,
        "t_offset": 0,
        "velocity_factor": TAU/4,
        "sine_graph_config":{
            "x_min": -TAU/2,
            "x_max": TAU/2,
            "color": RED,
            },
    }
 
    def construct(self):
        def update_curve(c, dt):
            rate = fix_update(c,dt,self.velocity_factor,self.dt_calculate)
            c.become(self.get_sin_graph(self.t_offset + rate))
            self.t_offset += rate
       
        c = self.get_sin_graph(0)
        c.counter = 0
        self.dt_calculate = 1 / self.camera.frame_rate
        self.play(ShowCreation(c))

        # PRINTS
        print(f"fps: {self.camera.frame_rate}")
        print(f"dt: {self.dt_calculate}")
        print(f"rate: {self.velocity_factor / self.camera.frame_rate}")
        print(f"cy_start: {c.points[0][1]}")
        print(f"cy_end:   {c.points[-1][1]}")
        print(f"t_offset: {self.t_offset}\n")

        c.add_updater(update_curve)
        self.add(c)

        # The animation begins
        self.wait(4)
        
        c.remove_updater(update_curve)
        self.wait()

        print(f"cy_start:  {c.points[0][1]}")
        print(f"cy_end:    {c.points[-1][1]}")
        print(f"t_offset: {self.t_offset}\n")

    def get_sin_graph(self, dx):
        c = FunctionGraph(
                lambda x: self.amp * np.sin(x - dx),
                **self.sine_graph_config
                )
        return c


class UpdateFunctionWithDt2(Scene):
    def construct(self):
        self.t_offset = 0
        orbit  = Ellipse(color=GREEN).scale(2.5)
        planet = Dot()
        text   = TextMobject("Update function")

        planet.move_to(orbit.point_from_proportion(0))

        def update_planet(mob,dt):
            rate = dt * 0.3
            mob.move_to(orbit.point_from_proportion((self.t_offset + rate)%1))
            self.t_offset += rate

        planet.add_updater(update_planet)
        self.add(orbit,planet)
        self.wait(4)
        self.play(Write(text))
        self.wait(4)
        planet.clear_updaters()
        self.wait(2)
        self.play(FadeOut(text))
        self.wait()
