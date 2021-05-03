from manimlib import *

#               _                 _       
#    __ _ _ __ (_)_ __ ___   __ _| |_ ___ 
#   / _` | '_ \| | '_ ` _ \ / _` | __/ _ \
#  | (_| | | | | | | | | | | (_| | ||  __/
# (_)__,_|_| |_|_|_| |_| |_|\__,_|\__\___|

class AnimateMethod(Scene):
    def construct(self):
        sq = Square()
        sq.save_state()
        self.add(sq)

        # New form
        self.play(
            sq.animate.to_edge(DOWN,buff=1)
        )
        self.wait()

        self.play(Restore(sq))
        self.wait()
        # Old form still works
        self.play(
            sq.to_edge,DOWN,{"buff": 1}
        )
        self.wait()

        # Multiple methods
        self.play(
            sq.animate
                .scale(2)
                .set_color(ORANGE)
                .to_corner(UR,buff=1)
        )
        self.wait()
        
#  _           _       _         _            
# (_)___  ___ | | __ _| |_ ___  | |_ _____  __
# | / __|/ _ \| |/ _` | __/ _ \ | __/ _ \ \/ /
# | \__ \ (_) | | (_| | ||  __/ | ||  __/>  < 
# |_|___/\___/|_|\__,_|\__\___|  \__\___/_/\_\


#class IsolateTex1(Scene):  # THIS IS DEPRECATED, use isolate instead
    # def construct(self):
        #t1 = Tex("{{x}}")
        #t2 = Tex("{{x}} - {{x}}")
        #VGroup(t1,t2)\
        #    .scale(3)\
        #    .arrange(DOWN)

        #self.add(t1)
        #self.wait()
        #self.play(
        #    TransformMatchingTex(t1,t2),
        #    run_time=4
        #)
        #self.wait()


class IsolateTex1v2(Scene):
    def construct(self):
        isolate_tex = ["x"]
        t1 = Tex("x",isolate=isolate_tex)
        t2 = Tex("x - x",isolate=isolate_tex)
        VGroup(t1,t2)\
            .scale(3)\
            .arrange(DOWN)

        self.add(t1)
        self.wait()
        self.play(
            TransformMatchingTex(t1,t2),
            run_time=4
        )
        self.wait()


class IsolateTex1v3(Scene):
    def construct(self):
        t1 = Tex("x")
        t2 = Tex("x - x")
        VGroup(t1,t2)\
            .scale(3)\
            .arrange(DOWN)

        self.add(t1)
        self.wait()
        self.play(
            # If the formula is complex this animation will not work.
            TransformMatchingShapes(t1,t2),
            run_time=4
        )
        self.wait()


class IsolateTex2(Scene):
    def construct(self):
        isolate_tex = ["x","y","3","="]
        t1 = Tex("x+y=3",isolate=isolate_tex)
        t2 = Tex("x=3-y",isolate=isolate_tex)
        VGroup(t1,t2)\
            .scale(3)
        t2.align_to(t1,LEFT)

        self.add(t1)
        self.wait()
        self.play(
            TransformMatchingTex(
                t1,t2,
                # Try removing this dictionary
                key_map={
                    "+":"-"
                }
            ),
            run_time=4
        )
        self.wait()

class IsolateTex3(Scene):
    def construct(self):
        isolate_tex = ["a","b","c","="]
        t1 = Tex("a\\times b = c",isolate=isolate_tex)
        t2 = Tex("a = { c \\over b }",isolate=isolate_tex)
        VGroup(t1,t2)\
            .scale(3)
        t2.align_to(t1,LEFT)

        self.add(t1)
        self.wait()
        self.play(
            TransformMatchingTex(
                t1,t2,
                key_map={
                    "\\times":"\\over"
                }
            ),
            run_time=4
        )
        self.wait()


#  _____         _     _____                     __
# |  ___|_ _  __| | __|_   _| __ __ _ _ __  ___ / _| ___  _ __ _ __ ___  
# | |_ / _` |/ _` |/ _ \| || '__/ _` | '_ \/ __| |_ / _ \| '__| '_ ` _ \ 
# |  _| (_| | (_| |  __/| || | | (_| | | | \__ \  _| (_) | |  | | | | | |
# |_|  \__,_|\__,_|\___||_||_|  \__,_|_| |_|___/_|  \___/|_|  |_| |_| |_|


class FadeTransformExample(Scene):
    def construct(self):
        m1 = Text("Hello world").to_corner(UL)
        m2 = Text("I'm FadeTransform").to_corner(DR)

        self.add(m1)
        self.wait()
        self.play(
            # Equivalent to ReplacementTransform
            FadeTransform(m1,m2),
            run_time=4
        )


class ExtrangeTransform(Scene):
    def construct(self):
        t1 = Tex("e^","\\frac{-it\\pi}{\\omega}")
        t2 = Tex("\\frac{-it\\pi}{\\omega}")
        VGroup(t1,t2)\
            .scale(3)\
            .arrange(DOWN,buff=2)
            
        self.add(t1,t2.copy().fade(0.8))
        self.wait()
        self.play(
            TransformFromCopy(t1[-1],t2[0]),
            run_time=6
        )
        self.wait()

class ExtrangeTransformFixed(Scene):
    def construct(self):
        t1 = Tex("e^","\\frac{-it\\pi}{\\omega}")
        t2 = Tex("\\frac{-it\\pi}{\\omega}")
        VGroup(t1,t2)\
            .scale(3)\
            .arrange(DOWN,buff=2)
            
        self.add(t1,t2.copy().fade(0.8))
        self.wait()
        self.play(
            FadeTransformPieces(t1[-1].copy(),t2[0]),
            run_time=4
        )
        self.wait()


#   ____                 _     ____
#  / ___|_ __ __ _ _ __ | |__ / ___|  ___ ___ _ __   ___ 
# | |  _| '__/ _` | '_ \| '_ \\___ \ / __/ _ \ '_ \ / _ \
# | |_| | | | (_| | |_) | | | |___) | (_|  __/ | | |  __/
#  \____|_|  \__,_| .__/|_| |_|____/ \___\___|_| |_|\___|
#                 |_|                                    

class AxesExample(Scene):
    def construct(self):
        X_MIN = -5
        X_MAX = 5
        # You can have multiple Axes
        axes_config = {
            # [min, max, step]
            "x_range": [X_MIN,X_MAX,0.5],
            "y_range": [-3,3,1],
            "height": FRAME_HEIGHT - 2,
            "width": FRAME_WIDTH - 2,
            "axis_config": {
                "include_tip": True,
                "numbers_to_exclude": [0],
            },
            "x_axis_config": {
                # see manimlib/mobjects/number_line.py
                "line_to_number_buff": 0.5,
                "line_to_number_direction": UP,
                "color": RED
            },
            "y_axis_config": {
                "decimal_number_config": {
                    # see manimlib/mobjects/numbers.py
                    "num_decimal_places": 1,
                },
            },
        }
        axes = Axes(**axes_config)
        axes.add_coordinate_labels(font_size=20)
        graph = axes.get_graph(
            lambda x: np.sin(x),
            x_min=X_MIN,
            x_max=X_MAX
        )
        
        self.add(axes,graph)

#  _____ _                   ____  ____
# |_   _| |__  _ __ ___  ___|  _ \/ ___|  ___ ___ _ __   ___ 
#   | | | '_ \| '__/ _ \/ _ \ | | \___ \ / __/ _ \ '_ \ / _ \
#   | | | | | | | |  __/  __/ |_| |___) | (_|  __/ | | |  __/
#   |_| |_| |_|_|  \___|\___|____/|____/ \___\___|_| |_|\___|


# New 3D mobjects
class Sphere(Surface):
    CONFIG = {
        "radius": 1,
        "u_range": (0, TAU),
        "v_range": (0, PI),
    }

    def uv_func(self, u, v):
        return self.radius * np.array([
            np.cos(u) * np.sin(v),
            np.sin(u) * np.sin(v),
            -np.cos(v)
        ])


class Torus(Surface):
    CONFIG = {
        "u_range": (0, TAU),
        "v_range": (0, TAU),
        "r1": 3,
        "r2": 1,
    }

    def uv_func(self, u, v):
        P = np.array([math.cos(u), math.sin(u), 0])
        return (self.r1 - self.r2 * math.cos(v)) * P - math.sin(v) * OUT



class ThreeDSceneExample(Scene):
    CONFIG = {
        "camera_class": ThreeDCamera,
    }

    def construct(self):
        surface_text = Text("For 3d scenes, try using surfaces")
        surface_text.fix_in_frame()
        surface_text.to_edge(UP)
        self.add(surface_text)
        self.wait(0.1)

        torus1 = Torus(r1=1, r2=1)
        torus2 = Torus(r1=3, r2=1)
        sphere = Sphere(radius=3, resolution=torus1.resolution)

        # Set perspective
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=-30 * DEGREES,
            phi=70 * DEGREES,
        )
        torus2.mesh = SurfaceMesh(torus2)
        sphere.mesh = SurfaceMesh(sphere)
        
        surface = sphere
        surface.save_state()
        self.play(
            ShowCreation(surface)
        )
        self.wait()
        self.play(
            Transform(surface,torus1)
        )
        self.wait()
        self.play(
            Transform(surface,torus2)
        )
        self.wait()
        
        
        self.play(Write(torus2.mesh))
        self.wait()
        
        self.play(
            Restore(surface),
            ReplacementTransform(
                torus2.mesh,
                sphere.mesh
            )
        )
        self.wait()


class ThreeDScene(Scene):
    CONFIG = {
        "camera_class": ThreeDCamera,
    }
    def setup(self):
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=-30 * DEGREES,
            phi=70 * DEGREES,
        )
        self.frame = frame

class Functions3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        para_hyp = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u**2-v**2
            ]),
            v_range=(-2,2),
            u_range=(-2,2),
            opacity=0.5,
            color=RED,
            resolution=(15, 32)
        )
        para_hyp.mesh = SurfaceMesh(para_hyp)
        func = Tex("x^2-y^2=z")
        func.fix_in_frame()
        func.to_corner(DL)

        self.play(ShowCreation(axes))
        
        self.play(
            ShowCreation(para_hyp),
            ShowCreation(para_hyp.mesh),
            run_time=3
        )

        # Set perspective
        frame = self.frame
        self.play(
            # Move camera frame during the transition
            frame.animate.increment_phi(10 * DEGREES),
            frame.animate.increment_theta(60 * DEGREES),
            run_time=3
        )
        # Add ambient rotation
        frame.add_updater(lambda m, dt: m.increment_theta(-0.1 * dt))
        self.wait(3)

        self.play(Write(func))
        self.wait(3)

        light = self.camera.light_source
        self.add(light)
        light.save_state()
        self.play(light.animate.move_to(3 * IN), run_time=5)
        self.play(light.animate.shift(10 * OUT), run_time=5)
        self.wait(3)

        self.play(Restore(light))
        self.wait(3)
