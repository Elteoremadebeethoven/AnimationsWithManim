old_version = True

if old_version:
    from big_ol_pile_of_manim_imports import *
else:
    from manimlib.imports import *
    
class EpicycloidSceneSimple(Scene):
    def construct(self):
       radius1 = 2.4
       radius2 = radius1/3
       self.epy(radius1,radius2)

    def epy(self,r1,r2):
        # Manim circle
        c1 = Circle(radius=r1,color=BLUE)
        # Small circle
        c2 = Circle(radius=r2,color=PURPLE).rotate(PI)
        c2.next_to(c1,RIGHT,buff=0)
        c2.start = c2.copy()
        # Dot
        # .points[0] return the start path coordinate
        # .points[-1] return the end path coordinate
        dot = Dot(c2.points[0],color=RED)
        # Line
        line = Line(c2.get_center(),dot.get_center()).set_stroke(BLACK,2.5)
        # Path
        path = VMobject(color=RED)
        # Path can't have the same coord twice, so we have to dummy point
        path.set_points_as_corners([dot.get_center(),dot.get_center()+UP*0.001])
        # Path group
        path_group = VGroup(line,dot,path)
        # Alpha, from 0 to 1:
        alpha = ValueTracker(0)
        
        self.play(ShowCreation(line),ShowCreation(c1),ShowCreation(c2),GrowFromCenter(dot))

        # update function of path_group
        def update_group(group):
            l,mob,previus_path = group
            mob.move_to(c2.points[0])
            old_path = path.copy()
            # See manimlib/mobject/types/vectorized_mobject.py
            old_path.append_vectorized_mobject(Line(old_path.points[-1],mob.get_center()))
            old_path.make_smooth()
            l.put_start_and_end_on(c2.get_center(),mob.get_center())
            path.become(old_path)

        # update function of small circle
        def update_c2(c):
            c.become(c.start)
            c.rotate(TAU*alpha.get_value(),about_point=c1.get_center())
            c.rotate(TAU*(r1/r2)*alpha.get_value(),about_point=c.get_center())

        path_group.add_updater(update_group)
        c2.add_updater(update_c2)
        self.add(c2,path_group)
        self.play(
                alpha.set_value,1,
                rate_func=linear,
                run_time=6
                )
        self.wait(2)
        c2.clear_updaters()
        path_group.clear_updaters()
        self.play(FadeOut(VGroup(c1,c2,path_group)))


class EpicycloidSceneComplete(Scene):
    CONFIG = {
            "camera_config": {"background_color":WHITE},
            "radius":2.4,
            "color_path":RED,
            "divisions":[3,4,5,6]
    }
    def construct(self):
        self.show_axes()
        self.show_animation()

    def show_axes(self,partition=3):
        step_size = self.radius/partition
        # See all options in manimlib/mobject/number_line.py
        x_axis = NumberLine(
                x_min = -step_size*7, 
                x_max = step_size*7.8,
                unit_size = step_size,
                include_tip = True,
                include_numbers = True,
                number_scale_val = 0.5,
                color=BLACK,
                exclude_zero_from_default_numbers = True,
                decimal_number_config = {"color":BLACK}
                )
        y_axis = NumberLine(
                x_min = -step_size*5, 
                x_max = step_size*5.5,
                unit_size = step_size,
                include_tip = True,
                include_numbers = True,
                number_scale_val = 0.5,
                color=BLACK,
                label_direction = UP,
                exclude_zero_from_default_numbers = True,
                decimal_number_config = {"color":BLACK}
                )
        y_axis.rotate(PI/2,about_point = ORIGIN)
        # rotate labels in y_axis
        for number in y_axis.numbers:
            number.rotate(-PI/2,about_point = number.get_center())

        self.play(Write(x_axis),Write(y_axis))
        self.wait()

    def show_animation(self):
        c = True
        for i in self.divisions:
            self.epy(self.radius,self.radius/i,c)
            c = False
        
    def epy(self,r1,r2,animation):
        # Manim circle
        c1 = Circle(radius=r1,color=BLUE)
        # Small circle
        c2 = Circle(radius=r2,color=BLACK).rotate(PI)
        c2.next_to(c1,RIGHT,buff=0)
        c2.start = c2.copy()
        # Dot
        dot = Dot(c2.point_from_proportion(0),color=self.color_path)
        # Line
        line = Line(c2.get_center(),dot.get_center()).set_stroke(BLACK,2.5)
        # Path
        path = VMobject(color=self.color_path)
        path.set_points_as_corners([dot.get_center(),dot.get_center()+UP*0.001])
        # Path group
        path_group = VGroup(line,dot,path)
        # Alpha
        alpha = ValueTracker(0)
        
        # If the animation start then shows the animation
        if animation:
            self.play(ShowCreation(line),ShowCreation(c1),ShowCreation(c2),GrowFromCenter(dot))
        else:
            self.remove(self.dot)
            self.add_foreground_mobjects(dot)
            self.play(ShowCreation(line),ShowCreation(c2))
            self.remove_foreground_mobjects(dot)
            self.add(c1,c2,path)

        # update function of path_group
        def update_group(group):
            l,mob,previus_path = group
            mob.move_to(c2.point_from_proportion(0))
            old_path = path.copy()
            old_path.append_vectorized_mobject(Line(old_path.points[-1],dot.get_center()))
            old_path.make_smooth()
            l.put_start_and_end_on(c2.get_center(),dot.get_center())
            path.become(old_path)

        # update function of small circle
        def update_c2(c):
            c.become(c.start)
            c.rotate(TAU*alpha.get_value(),about_point=c1.get_center())
            c.rotate(TAU*(r1/r2)*alpha.get_value(),about_point=c.get_center())

        path_group.add_updater(update_group)
        c2.add_updater(update_c2)
        self.add(c2,path_group)
        self.play(
                alpha.set_value,1,
                rate_func=linear,
                run_time=6
                )
        self.wait()
        c2.clear_updaters()
        path_group.clear_updaters()
        self.dot = dot
        self.play(FadeOut(path),FadeOut(c2),FadeOut(line))

# With alpha parameter in updater function

class EpicycloidSceneSimple_alpha(Scene):
    def construct(self):
       radius1 = 2.4
       radius2 = radius1/3
       self.epy(radius1,radius2)

    def epy(self,r1,r2):
        # Manim circle
        c1 = Circle(radius=r1,color=BLUE)
        # Small circle
        c2 = Circle(radius=r2,color=PURPLE).rotate(PI)
        c2.next_to(c1,RIGHT,buff=0)
        c2.start = c2.copy()
        # Dot
        dot = Dot(c2.points[0],color=YELLOW)
        # Line
        line = Line(c2.get_center(),dot.get_center()).set_stroke(BLACK,2.5)
        # Path
        path = VMobject(color=RED)
        path.set_points_as_corners([dot.get_center(),dot.get_center()+UP*0.001])
        # Path group
        path_group = VGroup(line,dot,path)
        
        self.play(ShowCreation(line),ShowCreation(c1),ShowCreation(c2),GrowFromCenter(dot))

        # update function of path_group
        def update_group(group):
            l,mob,previus_path = group
            mob.move_to(c2.points[0])
            old_path = path.copy()
            old_path.append_vectorized_mobject(Line(old_path.points[-1],dot.get_center()))
            old_path.make_smooth()
            l.put_start_and_end_on(c2.get_center(),dot.get_center())
            path.become(old_path)

        # update function of small circle
        def update_c2(c,alpha):
            c.become(c.start)
            c.rotate(TAU*alpha,about_point=c1.get_center())
            c.rotate(TAU*(r1/r2)*alpha,about_point=c.get_center())

        path_group.add_updater(update_group)
        self.add(path_group)
        
        self.play(
                UpdateFromAlphaFunc(c2,update_c2,rate_func=linear,run_time=6)
                )
        self.wait()


class EpicycloidSceneComplete_alpha(Scene):
    CONFIG = {
            "camera_config": {"background_color":WHITE},
            "radius":2.4,
            "color_path":RED,
            "divisions":[3,4,5,6]
    }
    def construct(self):
        self.show_axes()
        self.show_animation()

    def show_axes(self,partition=3):
        step_size = self.radius/partition
        # See all options in manimlib/mobject/number_line.py
        x_axis = NumberLine(
                x_min = -step_size*7, 
                x_max = step_size*7.8,
                unit_size = step_size,
                include_tip = True,
                include_numbers = True,
                number_scale_val = 0.5,
                color=BLACK,
                exclude_zero_from_default_numbers = True,
                decimal_number_config = {"color":BLACK}
                )
        y_axis = NumberLine(
                x_min = -step_size*5, 
                x_max = step_size*5.5,
                unit_size = step_size,
                include_tip = True,
                include_numbers = True,
                number_scale_val = 0.5,
                color=BLACK,
                label_direction = UP,
                exclude_zero_from_default_numbers = True,
                decimal_number_config = {"color":BLACK}
                )
        y_axis.rotate(PI/2,about_point = ORIGIN)
        # rotate labels in y_axis
        for number in y_axis.numbers:
            number.rotate(-PI/2,about_point = number.get_center())

        self.play(Write(x_axis),Write(y_axis))
        self.wait()

    def show_animation(self):
        c = True
        for i in self.divisions:
            self.epy(self.radius,self.radius/i,c)
            c = False
        
    def epy(self,r1,r2,animation):
        # Manim circle
        c1 = Circle(radius=r1,color=BLUE)
        # Small circle
        c2 = Circle(radius=r2,color=BLACK).rotate(PI)
        c2.next_to(c1,RIGHT,buff=0)
        c2.start = c2.copy()
        # Dot
        dot = Dot(c2.points[0],color=self.color_path)
        # Line
        line = Line(c2.get_center(),dot.get_center()).set_stroke(BLACK,2.5)
        # Path
        path = VMobject(color=self.color_path)
        path.set_points_as_corners([dot.get_center(),dot.get_center()+UP*0.001])
        # Path group
        path_group = VGroup(line,dot,path)
        
        # If the animation start then shows the animation
        if animation:
            self.play(ShowCreation(line),ShowCreation(c1),ShowCreation(c2),GrowFromCenter(dot))
        else:
            self.remove(self.dot)
            self.add_foreground_mobjects(dot)
            self.play(ShowCreation(line),ShowCreation(c2))
            self.remove_foreground_mobjects(dot)
            self.add(c1,c2,path)

        # update function of path_group
        def update_group(group):
            l,mob,previus_path = group
            mob.move_to(c2.points[0])
            old_path = path.copy()
            old_path.append_vectorized_mobject(Line(old_path.points[-1],dot.get_center()))
            old_path.make_smooth()
            l.put_start_and_end_on(c2.get_center(),dot.get_center())
            path.become(old_path)

        # update function of small circle
        def update_c2(c,alpha):
            c.become(c.start)
            c.rotate(TAU*alpha,about_point=c1.get_center())
            c.rotate(TAU*(r1/r2)*alpha,about_point=c.get_center())

        path_group.add_updater(update_group)
        self.add(path_group)
        
        self.play(
                UpdateFromAlphaFunc(c2,update_c2,rate_func=linear,run_time=5)
                )
        self.wait()
        self.dot = dot
        self.play(FadeOut(path),FadeOut(c2),FadeOut(line))
