# Manim FAQs ([code](https://github.com/Elteoremadebeethoven/AnimationsWithManim/blob/master/English/extra/faqs/faqs.py))
## What is CONFIG
<p align="center"><img src ="/English/extra/faqs/gifs/WhatIsCONFIG.gif" width="800" /></p>

```python3
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
```

## Scene from another Scene
<p align="center"><img src ="/English/extra/faqs/gifs/SceneFromAnotherScene.gif" width="800" /></p>

```python3
class SceneFromAnotherScene(WhatIsCONFIG):
    CONFIG={
        "object_1":TextMobject("Another object"),
        "object_2":Circle(),
        "number":4,
        "vector":[-1,-1,0]
    }
```

## Change background color
<p align="center"><img src ="/English/extra/faqs/gifs/ChangeBackgroundColor.png" width="800" /></p>

```python3
class ChangeBackgroundColor(Scene):
    CONFIG={
        "camera_config":{"background_color":RED},
        "text":TexMobject(r"\frac{d}{dx}\Bigr|_{y=2}").scale(5)
    }
    def construct(self):
        self.add(self.text)
```

## Remove background stroke width of texts
<p align="center"><img src ="/English/extra/faqs/gifs/RemoveBackgroundStrokeWidth.png" width="800" /></p>

```python3
class RemoveBackgroundStrokeWidth(ChangeBackgroundColor):
    CONFIG={
        "text":TexMobject(
            r"\frac{d}{dx}\Bigr|_{y=2}",
            background_stroke_width=0, #<- Add this line
            ).scale(5)
    }
```

## Arrange Objects
<p align="center"><img src ="/English/extra/faqs/gifs/ArrangeObjects1.gif" width="800" /></p>

```python3
class ArrangeObjects(Scene):
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
```

## Change position and size of the camera
<p align="center"><img src ="/English/extra/faqs/gifs/ChangePositionAndSizeCamera.gif" width="800" /></p>

```python3
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
```

## Change position and size of the camera in other scenes
<p align="center"><img src ="/English/extra/faqs/gifs/ChangePositionAndSizeCameraInAnotherScene.gif" width="800" /></p>

```python3
class ChangePositionAndSizeCameraInAnotherScene(GraphScene,MovingCameraScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 5, 
        "x_tick_frequency" : 0.5, 
    }
    # Setup the scenes
    def setup(self):            
        GraphScene.setup(self)
        MovingCameraScene.setup(self)

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
```

## Linear transformation
<p align="center"><img src ="/English/extra/faqs/gifs/LinearTransformation.gif" width="800" /></p>

```python3
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
```

## Remove all objects in screen
<p align="center"><img src ="/English/extra/faqs/gifs/RemoveAllObjectsInScreen.gif" width="800" /></p>

```python3
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
```

## Zoomed scene example
<p align="center"><img src ="/English/extra/faqs/gifs/ZoomedSceneExample.gif" width="800" /></p>

```python3
class ZoomedSceneExample(ZoomedScene):
    CONFIG = {
        "zoom_factor": 0.3,
        "zoomed_display_height": 1,
        "zoomed_display_width": 6,
        "image_frame_stroke_width": 20,
        "zoomed_camera_config": {
            "default_frame_stroke_width": 3,
        },
    }

    def construct(self):
        # Set objects
        dot = Dot().shift(UL*2)

        image=ImageMobject(np.uint8([[ 0, 100,30 , 200],
                                     [255,0,5 , 33]]))
        image.set_height(7)
        frame_text=TextMobject("Frame",color=PURPLE).scale(1.4)
        zoomed_camera_text=TextMobject("Zommed camera",color=RED).scale(1.4)

        self.add(image,dot)

        # Set camera
        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        frame = zoomed_camera.frame
        zoomed_display_frame = zoomed_display.display_frame

        frame.move_to(dot)
        frame.set_color(PURPLE)

        zoomed_display_frame.set_color(RED)
        zoomed_display.shift(DOWN)

        # brackground zoomed_display
        zd_rect = BackgroundRectangle(
            zoomed_display,
            fill_opacity=0,
            buff=MED_SMALL_BUFF,
        )

        self.add_foreground_mobject(zd_rect)

        # animation of unfold camera
        unfold_camera = UpdateFromFunc(
            zd_rect,
            lambda rect: rect.replace(zoomed_display)
        )

        frame_text.next_to(frame,DOWN)

        self.play(
            ShowCreation(frame),
            FadeInFromDown(frame_text)
        )

        # Activate zooming
        self.activate_zooming()

        self.play(
            # You have to add this line
            self.get_zoomed_display_pop_out_animation(),
            unfold_camera
        )

        zoomed_camera_text.next_to(zoomed_display_frame,DOWN)
        self.play(FadeInFromDown(zoomed_camera_text))

        # Scale in     x   y  z
        scale_factor=[0.5,1.5,0]

        # Resize the frame and zoomed camera
        self.play(
            frame.scale,                scale_factor,
            zoomed_display.scale,       scale_factor,
            FadeOut(zoomed_camera_text),
            FadeOut(frame_text)
        )

        # Resize the frame
        self.play(
            frame.scale,3,
            frame.shift,2.5*DOWN
        )

        # Resize zoomed camera
        self.play(
            ScaleInPlace(zoomed_display,2)
        )


        self.wait()

        self.play(
            self.get_zoomed_display_pop_out_animation(),
            unfold_camera,
            # -------> Inverse
            rate_func=lambda t: smooth(1-t),
        )
        self.play(
            Uncreate(zoomed_display_frame),
            FadeOut(frame),
        )
        self.wait()
```
