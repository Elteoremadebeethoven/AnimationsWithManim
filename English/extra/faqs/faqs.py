from big_ol_pile_of_manim_imports import *

# What is CONFIG? ----------------------------------------------
class WhatIsCONFIG(Scene):
    CONFIG={
        "object_1":TextMobject("Object 1"),
        "object_2":Square(),
        "number":3,
        "vector":[1,1,0]
    }
    def construct(self):
        self.play(
            Write(self.object_1)
        )
        self.play(
            self.object_1.scale,self.number
        )
        self.play(
            ReplacementTransform(
                self.object_1,
                self.object_2
            )
        )
        self.play(
            self.object_2.shift,self.vector
        )
        self.wait()

class SceneFromAnotherScene(WhatIsCONFIG):
    CONFIG={
        "object_1":TextMobject("Another object"),
        "object_2":Circle(),
        "number":4,
        "vector":[-1,-1,0]
    }
# -----------------------------------------------------------------
# Change the background color -------------------------------------
class ChangeBackgroundColor(Scene):
    CONFIG={
        "camera_config":{"background_color":RED},
        "text":TexMobject(r"\frac{d}{dx}\Bigr|_{y=2}").scale(5)
    }
    def construct(self):
        self.add(self.text)
# -----------------------------------------------------------------
# Remove background stroke width of texts
class RemoveBackgroundStrokeWidth(ChangeBackgroundColor):
    CONFIG={
        "text":TexMobject(
            r"\frac{d}{dx}\Bigr|_{y=2}",
            background_stroke_width=0, #<- Add this line
            ).scale(5)
    }
# Yoy can go to manimlib/mobject/svg/tex_mobject.py and change
# background_stroke_width=0 in the SingleStringTexMobject class.
# -----------------------------------------------------------------
# Arrange multiple objects
class ArrangeObjects1(Scene):
    def construct(self):
        text1 = TextMobject("You have")
        text2 = TextMobject("to use")
        text3 = TextMobject("\\tt VGroup")

        text_group = VGroup(
            text1,
            text2,
            text3
        )

        #         .arrange # <- For recent versions
        text_group.arrange_submobjects(
            DOWN, # <- Direction
            aligned_edge = LEFT,
            buff=0.4
        )

        self.add(text_group)
        self.wait()

        self.play(
            text_group.arrange_submobjects,UP,{"aligned_edge":RIGHT,"buff":2}
        )
        self.wait()

        self.play(
            text_group.arrange_submobjects,RIGHT,{"buff":0.4}
        )
        self.wait()
# -----------------------------------------------------------------
# How change the size of the camera -------------------------------
class ChangePositionAndSizeCamera(MovingCameraScene):
    def construct(self):
        text=TexMobject("\\nabla\\textbf{u}").scale(3)
        square=Square()

        # Arrange the objects
        VGroup(text,square).arrange_submobjects(RIGHT,buff=3)

        self.add(text,square)

        # Save the state of camera
        self.camera_frame.save_state()

        # Animation of the camera
        self.play(
            # Set the size with the width of a object
            self.camera_frame.set_width,text.get_width()*1.2,
            # Move the camera to the object
            self.camera_frame.move_to,text
        )
        self.wait()

        # Restore the state saved
        self.play(Restore(self.camera_frame))

        self.play(
            self.camera_frame.set_height,square.get_width()*1.2,
            self.camera_frame.move_to,square
        )
        self.wait()

        self.play(Restore(self.camera_frame))

        self.wait()
        

class ChangePositionAndSizeCameraInAnotherScene(GraphScene,MovingCameraScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 5, 
        "x_tick_frequency" : 0.5, 
    }
    def setup(self):            
        # You have to copy the setup of the scenes that you use
        # In this case, the setup from GrapScene and MovingCameraScene

        # This setup is from manimlib/scene/graph_scene.py
        self.default_graph_colors_cycle = it.cycle(self.default_graph_colors)

        self.left_T_label = VGroup()
        self.left_v_line = VGroup()
        self.right_T_label = VGroup()
        self.right_v_line = VGroup()

        # This setup is from manimlib/scene/moving_camera_scene.py
        Scene.setup(self)
        assert(isinstance(self.camera, MovingCamera))
        self.camera_frame = self.camera.frame
        return self

    def construct(self):
        self.setup_axes(animate=False)

        graph = self.get_graph(lambda x : x**2,  
                                    color = GREEN,
                                    x_min = 0, 
                                    x_max = 7
                                    )
        dot_at_start_graph=Dot().move_to(graph.points[0])
        dot_at_end_grap=Dot().move_to(graph.points[-1])

        self.add(graph,dot_at_end_grap,dot_at_start_graph)

        self.play(
            self.camera_frame.scale,.5,
            self.camera_frame.move_to,dot_at_start_graph
        )

        self.play(
            self.camera_frame.move_to,dot_at_end_grap
        )
        self.wait()

# -----------------------------------------------------------------
# Linear transformation example
class LinearTransformation(LinearTransformationScene):
    CONFIG = {
        "include_background_plane": True,
        "include_foreground_plane": True,
        "foreground_plane_kwargs": {
            "x_radius": FRAME_WIDTH,
            "y_radius": FRAME_HEIGHT,
            "secondary_line_ratio": 0
        },
        "background_plane_kwargs": {
            "color": GREY,
            "secondary_color": DARK_GREY,
            "axes_color": GREY,
            "stroke_width": 2,
        },
        "show_coordinates": False,
        "show_basis_vectors": True,
        "basis_vector_stroke_width": 6,
        "i_hat_color": X_COLOR,
        "j_hat_color": Y_COLOR,
        "leave_ghost_vectors": False,
    }
    def construct(self):
        mob = Circle()
        mob.move_to(RIGHT+UP*2)
        vector_array = np.array([[1], [2]])
        matrix = [[0, 1], [-1, 1]]

        self.add_transformable_mobject(mob)

        self.add_vector(vector_array)

        self.apply_matrix(matrix)

        self.wait()
# --------------------------------------------------------------------
class RemoveAllObjectsInScreen(Scene):
    def construct(self):
        self.add(
            VGroup(
                *[
                    VGroup(
                        *[
                            Dot()
                            for i in range(30)
                        ]
                    ).arrange_submobjects(RIGHT)
                    for j in range(10)
                ]
            ).arrange_submobjects(DOWN)
        )

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )

        self.wait()
