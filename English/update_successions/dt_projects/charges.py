from manimlib.imports import *

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
        "anim_time": 18,
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

        self.play(
            *list(map(GrowArrow, vector_field)),
            *list(map(GrowFromCenter, particles))
        )
        self.wait()
        vector_field.add_updater(update_vector_field),
        particles.add_updater(update_particles),
        self.add(
            vector_field,
            particles
        )
        # Animation time:
        self.wait(self.anim_time)

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