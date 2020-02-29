from manimlib.imports import *

class VectorFieldScene1(Scene):
    def construct(self):
        func = lambda p: np.array([
            p[0]/2,  # x
            p[1]/2,  # y
            0        # z
        ])
        # Normalized
        vector_field_norm = VectorField(func)
        # Not normalized
        vector_field_not_norm = VectorField(func, length_func=linear)
        self.play(*[GrowArrow(vec) for vec in vector_field_norm])
        self.wait(2)
        self.play(ReplacementTransform(vector_field_norm,vector_field_not_norm))
        self.wait(2)

# Other way
def functioncurlreal(p, velocity=0.05):
    x, y = p[:2]
    result =  - y * RIGHT + x * UP
    result *= velocity
    return result

class VectorFieldScene2(Scene):
    def construct(self):
        vector_field = VectorField(functioncurlreal)
        dot1 = Dot([1,1,0], color=RED)
        dot2 = Dot([2,2,0], color=BLUE)
        self.add(vector_field,dot1,dot2)
        self.wait()
        for dot in dot1,dot2:
            move_submobjects_along_vector_field(
                dot,
                lambda p: functioncurlreal(p,0.5)
            )
        self.wait(3)
        for dot in dot1,dot2:
            dot.clear_updaters()
        self.wait()

class VectorFieldScene3(Scene):
    def construct(self):
        vector_field = VectorField(
            lambda p: functioncurlreal(p,0.5),
            length_func = lambda norm: 0.6 * sigmoid(norm)
        )
        dot = Dot([2,3,0]).fade(1)
        some_vector = vector_field.get_vector(dot.get_center())
        some_vector.add_updater(
            lambda mob: mob.become(vector_field.get_vector(dot.get_center()))
        )
        self.add(vector_field,dot,some_vector)
        self.play(
            dot.shift,LEFT*4,
            run_time=3
        )
        self.play(
            dot.shift,DOWN*5,
            run_time=3
        )
        self.play(
            Rotating(dot, radians=PI, about_point=ORIGIN),
            run_time=5
        )
        self.wait()

# Electric field animation, 3Blue1Brown property
# This animation belongs to the file:
# https://github.com/3b1b/manim/blob/master/from_3b1b/old/div_curl.py#L1293
# This code is not my own, I simply updated it to the recent 
# version and documented it.
def get_force_field_func(*point_strength_pairs, **kwargs):
    radius = kwargs.get("radius", 0.5)

    def func(point):
        result = np.array(ORIGIN)
        for center, strength in point_strength_pairs:
            to_center = center - point
            norm = get_norm(to_center)
            if norm == 0:
                continue
            elif norm < radius:
                to_center /= radius**3
            elif norm >= radius:
                to_center /= norm**3
            to_center *= -strength
            result += to_center
        return result
    return func

class ElectricParticle(Circle):
    CONFIG = {
        "color": WHITE,
        "sign": "+",
    }
    def __init__(self, radius=0.5 ,**kwargs):
        digest_config(self, kwargs)
        super().__init__(
            stroke_color=WHITE,
            stroke_width=0.5,
            fill_color=self.color,
            fill_opacity=0.8,
            radius=radius
        )
        sign = TexMobject(self.sign)
        sign.set_stroke(WHITE, 1)
        sign.set_width(0.5 * self.get_width())
        sign.move_to(self)
        self.add(sign)

class Proton(ElectricParticle):
    CONFIG = {
        "color": RED_E,
    }

class Electron(ElectricParticle):
    CONFIG = {
        "color": BLUE_E,
        "sign": "-"
    }

class ChangingElectricField(Scene):
    CONFIG = {
        "vector_field_config": {},
        "num_particles": 6,
        "anim_time": 5,
    }
    def construct(self):
        particles = self.get_particles()
        vector_field = self.get_vector_field()

        def update_vector_field(vector_field):
            new_field = self.get_vector_field()
            vector_field.become(new_field)
            vector_field.func = new_field.func

        # The dt parameter will be explained in 
        # future videos, but here is a small preview.
        def update_particles(particles, dt):
            func = vector_field.func
            for particle in particles:
                force = func(particle.get_center())
                particle.velocity += force * dt
                particle.shift(particle.velocity * dt)

        vector_field.add_updater(update_vector_field),
        particles.add_updater(update_particles),
        self.add(
            vector_field,
            particles
        )
        # Animation time:
        self.wait(self.anim_time)
        # Suspend animation
        for mob in vector_field,particles:
            mob.suspend_updating()
        self.wait()
        # Restore animation
        for mob in vector_field,particles:
            mob.resume_updating()
        self.wait(3)


    def get_particles(self):
        particles = self.particles = VGroup()
        for n in range(self.num_particles):
            if n % 2 == 0:
                particle = Proton(radius=0.2)
                particle.charge = +1
            else:
                particle = Electron(radius=0.2)
                particle.charge = -1
            particle.velocity = np.random.normal(0, 0.1, 3)
            particles.add(particle)
            particle.shift(np.random.normal(0, 0.2, 3))

        particles.arrange_in_grid(buff=LARGE_BUFF)
        return particles

    def get_vector_field(self):
        func = get_force_field_func(*list(zip(
            list(map(lambda x: x.get_center(), self.particles)),
            [p.charge for p in self.particles]
        )))
        self.vector_field = VectorField(func, **self.vector_field_config)
        return self.vector_field
