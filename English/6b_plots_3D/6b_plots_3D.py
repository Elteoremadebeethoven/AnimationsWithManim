from big_ol_pile_of_manim_imports import *

#There seems to be no change between Scene and ThreeDScene
class CameraPosition1(ThreeDScene):
    def construct(self):
        circulo=Circle()
        self.play(ShowCreation(circulo))
        self.wait()

'''
We have to add this line:

    def get_axis(self, min_val, max_val, axis_config):
        new_config = merge_config([
            axis_config,
            {"x_min": min_val, "x_max": max_val},
            self.number_line_config,
        ])
        return NumberLine(**new_config)

in manimlib/mobject/coordinate_systems.py

Use: 
self.set_camera_orientation(phi,theta,distance,gamma) 
to change the camera position
You can change the domain with:
ThreeDAxes(
    x_min.
    x_max,
    y_min,
    y_max,
    z_min,
    z_max
)
'''

class CameraPosition2(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle=Circle()
        self.set_camera_orientation(phi=0 * DEGREES)
        self.play(ShowCreation(circle),ShowCreation(axes))
        self.wait()

class CameraPosition3(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle=Circle()
        self.set_camera_orientation(phi=80 * DEGREES,theta=45*DEGREES)
        self.play(ShowCreation(circle),ShowCreation(axes))
        self.wait()

class CameraPosition4(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle=Circle()
        self.set_camera_orientation(phi=80 * DEGREES,theta=45*DEGREES,distance=6)
        self.play(ShowCreation(circle),ShowCreation(axes))
        self.wait()

class CameraPosition5(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle=Circle()
        self.set_camera_orientation(phi=80 * DEGREES,theta=45*DEGREES,distance=6,gamma=30*DEGREES)
        self.play(ShowCreation(circle),ShowCreation(axes))
        self.wait()

#------ Move camera

class MoveCamera1(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle=Circle()
        self.play(ShowCreation(circle),ShowCreation(axes))
        self.move_camera(phi=30*DEGREES,theta=-45*DEGREES,run_time=3)
        self.wait()

class MoveCamera2(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle=Circle()
        self.set_camera_orientation(phi=80 * DEGREES)           
        self.play(ShowCreation(circle),ShowCreation(axes))
        self.begin_ambient_camera_rotation(rate=0.1)            #Start move camera
        self.wait(5)
        self.stop_ambient_camera_rotation()                     #Stop move camera
        self.move_camera(phi=80*DEGREES,theta=-PI/2)            #Return the position of the camera
        self.wait()

#----------- Funciones parametricas


class ParametricCurve1(ThreeDScene):
    def construct(self):
        curve1=ParametricFunction(
                lambda u : np.array([
                1.2*np.cos(u),
                1.2*np.sin(u),
                u/2
            ]),color=RED,t_min=-TAU,t_max=TAU,
            )
        curve2=ParametricFunction(
                lambda u : np.array([
                1.2*np.cos(u),
                1.2*np.sin(u),
                u
            ]),color=RED,t_min=-TAU,t_max=TAU,
            )
        axes = ThreeDAxes()

        self.add(axes)

        self.set_camera_orientation(phi=80 * DEGREES,theta=-60*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1) 
        self.play(ShowCreation(curve1))
        self.wait()
        self.play(Transform(curve1,curve2),rate_func=there_and_back,run_time=3)
        self.wait()

# Add this in the object: .set_shade_in_3d(True)

class ParametricCurve2(ThreeDScene):
    def construct(self):
        curve1=ParametricFunction(
                lambda u : np.array([
                1.2*np.cos(u),
                1.2*np.sin(u),
                u/2
            ]),color=RED,t_min=-TAU,t_max=TAU,
            )
        curve2=ParametricFunction(
                lambda u : np.array([
                1.2*np.cos(u),
                1.2*np.sin(u),
                u
            ]),color=RED,t_min=-TAU,t_max=TAU,
            )

        curve1.set_shade_in_3d(True)
        curve2.set_shade_in_3d(True)

        axes = ThreeDAxes()

        self.add(axes)

        self.set_camera_orientation(phi=80 * DEGREES,theta=-60*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1) 
        self.play(ShowCreation(curve1))
        self.wait()
        self.play(Transform(curve1,curve2),rate_func=there_and_back,run_time=3)
        self.wait()


class ParametricCurve2(ThreeDScene):
    def construct(self):
        curve1=ParametricFunction(
                lambda u : np.array([
                1.2*np.cos(u),
                1.2*np.sin(u),
                u/2
            ]),color=RED,t_min=-TAU,t_max=TAU,
            )
        curve2=ParametricFunction(
                lambda u : np.array([
                1.2*np.cos(u),
                1.2*np.sin(u),
                u
            ]),color=RED,t_min=-TAU,t_max=TAU,
            )

        curve1.set_shade_in_3d(True)
        curve2.set_shade_in_3d(True)

        axes = ThreeDAxes()

        self.add(axes)

        self.set_camera_orientation(phi=80 * DEGREES,theta=-60*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1) 
        self.play(ShowCreation(curve1))
        self.wait()
        self.play(Transform(curve1,curve2),rate_func=there_and_back,run_time=3)
        self.wait()

#----- Surfaces
class SurfacesAnimation(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        cylinder = ParametricSurface(
            lambda u, v: np.array([
                np.cos(TAU * v),
                np.sin(TAU * v),
                2 * (1 - u)
            ]),
            resolution=(6, 32)).fade(0.5) #Resolution of the surfaces

        paraboloid = ParametricSurface(
            lambda u, v: np.array([
                np.cos(v)*u,
                np.sin(v)*u,
                u**2
            ]),v_max=TAU,
            checkerboard_colors=[PURPLE_D, PURPLE_E],
            resolution=(10, 32)).scale(2)

        para_hyp = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u**2-v**2
            ]),v_min=-2,v_max=2,u_min=-2,u_max=2,checkerboard_colors=[BLUE_D, BLUE_E],
            resolution=(15, 32)).scale(1)

        cone = ParametricSurface(
            lambda u, v: np.array([
                u*np.cos(v),
                u*np.sin(v),
                u
            ]),v_min=0,v_max=TAU,u_min=-2,u_max=2,checkerboard_colors=[GREEN_D, GREEN_E],
            resolution=(15, 32)).scale(1)

        hip_one_side = ParametricSurface(
            lambda u, v: np.array([
                np.cosh(u)*np.cos(v),
                np.cosh(u)*np.sin(v),
                np.sinh(u)
            ]),v_min=0,v_max=TAU,u_min=-2,u_max=2,checkerboard_colors=[YELLOW_D, YELLOW_E],
            resolution=(15, 32))

        ellipsoid=ParametricSurface(
            lambda u, v: np.array([
                1*np.cos(u)*np.cos(v),
                2*np.cos(u)*np.sin(v),
                0.5*np.sin(u)
            ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[TEAL_D, TEAL_E],
            resolution=(15, 32)).scale(2)

        sphere = ParametricSurface(
            lambda u, v: np.array([
                1.5*np.cos(u)*np.cos(v),
                1.5*np.cos(u)*np.sin(v),
                1.5*np.sin(u)
            ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)).scale(2)


        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)


        self.add(axes)
        self.play(Write(sphere))
        self.wait()
        self.play(ReplacementTransform(sphere,ellipsoid))
        self.wait()
        self.play(ReplacementTransform(ellipsoid,cone))
        self.wait()
        self.play(ReplacementTransform(cone,hip_one_side))
        self.wait()
        self.play(ReplacementTransform(hip_one_side,para_hyp))
        self.wait()
        self.play(ReplacementTransform(para_hyp,paraboloid))
        self.wait()
        self.play(ReplacementTransform(paraboloid,cylinder))
        self.wait()
        self.play(FadeOut(cylinder))

#---- Text on 3D
class Text3D1(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES,theta=-45*DEGREES)
        text3d=TextMobject("This is a 3D text").scale(2)
        self.add(axes,text3d)

# This text appears in XY plane, to rotate:

class Text3D2(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES,theta=-45*DEGREES)
        text3d=TextMobject("This is a 3D text").scale(2).set_shade_in_3d(True) 
        text3d.rotate(PI/2,axis=RIGHT)
        self.add(axes,text3d)

# To see the text in the traditional form:
class Text3D3(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES,theta=-45*DEGREES)
        text3d=TextMobject("This is a 3D text")

        self.add_fixed_in_frame_mobjects(text3d) #<----- Add this
        text3d.to_corner(UL)

        self.add(axes)
        self.begin_ambient_camera_rotation()
        self.play(Write(text3d))

        sphere = ParametricSurface(
            lambda u, v: np.array([
                1.5*np.cos(u)*np.cos(v),
                1.5*np.cos(u)*np.sin(v),
                1.5*np.sin(u)
            ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)).scale(2)

        self.play(LaggedStart(ShowCreation,sphere))
        self.wait(2)



