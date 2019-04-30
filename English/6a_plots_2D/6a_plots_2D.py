from big_ol_pile_of_manim_imports import *


class PlotGraph(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 20,
        "x_max" : 7,
        "x_min" : 4,
        "y_tick_frequency" : 5, 
        "x_tick_frequency" : 0.5, 
        "axes_color" : BLUE,
        "y_labeled_nums": range(30,60,10),
        "x_labeled_nums": list(np.arange(4, 7.0+0.5, 0.5)),
        "x_label_decimal":1,
        "graph_origin": 3 * DOWN + 6 * LEFT,
        "x_label_direction":DOWN,
        "y_label_direction":RIGHT,
        "x_axis_label": None,
        "x_axis_width":10
    }

    def construct(self):
        self.setup_axes(animate=False) #animate=True to add animation
        self.x_axis.shift(LEFT*abs(self.y_axis[0].points[0]-self.x_axis[0].points[0]))
        self.y_axis.shift(DOWN*abs(self.y_axis[0].points[0]-self.x_axis[0].points[0]))
        self.y_axis_label_mob.next_to(self.y_axis[0].get_end(),UP)
        p=Dot().move_to(self.coords_to_point(self.x_min, self.y_min))
        self.add(p)
        graph = self.get_graph(lambda x : x**2, 
                                    color = GREEN,
                                    x_min = 5, 
                                    x_max = 7
                                    )

        self.play(
            ShowCreation(graph),
            run_time = 2
        )
        self.wait()


def Range(in_val,end_val,step=1):
    return list(np.arange(in_val,end_val+step,step))

class Plot1(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 5, 
        "x_tick_frequency" : 0.5, 
        "axes_color" : BLUE, 
        "y_labeled_nums": range(0,60,10),
        "x_labeled_nums": list(np.arange(2, 7.0+0.5, 0.5)),
        "x_label_decimal":1,
        "y_label_direction": RIGHT,
        "x_label_direction": UP,
        "y_label_decimal":3
    }
    def construct(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x : x**2,  
                                    color = GREEN,
                                    x_min = 2, 
                                    x_max = 4
                                    )
        self.play(
        	ShowCreation(graph),
            run_time = 2
        )
        self.wait()

class Plot1v2(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 5,
        "x_tick_frequency" : 1,
        "axes_color" : BLUE, 
        "graph_origin" : np.array((0,0,0))
    }
    def construct(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x : x**2, 
                                    color = GREEN,
                                    x_min = 2, 
                                    x_max = 4
                                    )
        self.play(
            ShowCreation(graph),
            run_time = 2
        )
        self.wait()

class Plot2(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 5,
        "axes_color" : BLUE,
        "x_axis_label" : "$t$",
        "y_axis_label" : "$f(t)$",
    }
    def construct(self):
        self.setup_axes()
        graph = self.get_graph(lambda x : x**2, color = GREEN)
        self.play(
        	ShowCreation(graph),
            run_time = 2
        )
        self.wait()

    def setup_axes(self):
        # Add this line
        GraphScene.setup_axes(self) 
        # Parametters of labels
        #   For x
        init_label_x = 2
        end_label_x = 7
        step_x = 1
        #   For y
        init_label_y = 20
        end_label_y = 50
        step_y = 5
        # Position of labels
        #   For x
        self.x_axis.label_direction = DOWN #DOWN is default
        #   For y
        self.y_axis.label_direction = LEFT
        # Add labels to graph
        #   For x
        self.x_axis.add_numbers(*range(
                                        init_label_x,
                                        end_label_x+step_x,
                                        step_x
                                    ))
        #   For y
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))
        #   Add Animation
        self.play(
            ShowCreation(self.x_axis),
            ShowCreation(self.y_axis)
        )

class Plot3(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 10,
        "axes_color" : BLUE,
    }
    def construct(self):
        self.setup_axes()
        graph = self.get_graph(lambda x : x**2, color = GREEN)

        self.play(
            ShowCreation(graph),
            run_time = 2
        )
        self.wait()

    def setup_axes(self):
        GraphScene.setup_axes(self)
        # Custom parametters
        self.x_axis.add_numbers(*[0,2,5,4])
        # Y parametters
        init_label_y = 0
        end_label_y = 50
        step_y = 5
        self.y_axis.label_direction = LEFT
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))
        self.play(Write(self.x_axis),Write(self.y_axis))

class Plot4(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 10,
        "axes_color" : BLUE,
    }
    def construct(self):
        self.setup_axes()
        graph = self.get_graph(lambda x : x**2, color = GREEN)

        self.play(
            ShowCreation(graph),
            run_time = 2
        )
        self.wait()

    def setup_axes(self):
        GraphScene.setup_axes(self)
        self.x_axis.label_direction = UP
        self.x_axis.add_numbers(*[3.5,5,4]) # 3.5 is rounded to 4
        self.y_axis.label_direction = LEFT
        self.y_axis.add_numbers(*range(0, 50+5, 5))
        self.play(Write(self.x_axis),Write(self.y_axis))

class Plot5(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 10,
        "x_tick_frequency" : 0.5,
        "axes_color" : BLUE,
    }
    def construct(self):
        self.setup_axes()
        graph = self.get_graph(lambda x : x**2, color = GREEN)

        self.play(
            ShowCreation(graph),
            run_time = 2
        )
        self.wait()

    def setup_axes(self):
        GraphScene.setup_axes(self)
        self.x_axis.label_direction = UP
        values_x = [
            (3.5,"3.5"), # (position 3.5, label "3.5")
            (4.5,"\\frac{9}{2}") # (position 4.5, label "9/2")
        ]
        self.x_axis_labels = VGroup() # Create a group named x_axis_labels
        #   pos.   tex.
        for x_val, x_tex in values_x:
            tex = TexMobject(x_tex) # Convert string to tex
            tex.scale(0.7) 
            tex.next_to(self.coords_to_point(x_val, 0), DOWN) #Put tex on the position
            self.x_axis_labels.add(tex) #Add tex in graph
        self.play(
            Write(self.x_axis_labels),
            Write(self.x_axis),
            Write(self.y_axis)
        )

class Plot6(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 10,
        "x_tick_frequency" : 0.5,
        "axes_color" : BLUE,
    }
    def construct(self):
        self.setup_axes()
        graph = self.get_graph(lambda x : x**2, color = GREEN)

        self.play(
            ShowCreation(graph),
            run_time = 2
        )
        self.wait()

    def setup_axes(self):
        GraphScene.setup_axes(self)
        self.x_axis.label_direction = UP
        # List of values of positions
        values_decimal_x=[0,0.5,1,1.5,3.35]
        # Transform positions to tex labels
        list_x = [*["%s"%i for i in values_decimal_x]]
        # List touples of (position,label)
        values_x = [
            (i,j)
            for i,j in zip(values_decimal_x,list_x)
        ]
        self.x_axis_labels = VGroup()
        for x_val, x_tex in values_x:
            tex = TexMobject(x_tex)
            tex.scale(0.7)
            tex.next_to(self.coords_to_point(x_val, 0), DOWN)
            self.x_axis_labels.add(tex)
        self.play(
            Write(self.x_axis_labels),
            Write(self.x_axis),
            Write(self.y_axis)
        )

class Plot7(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 10,
        "x_tick_frequency" : 0.5,
        "axes_color" : BLUE,
    }
    def construct(self):
        self.setup_axes()
        graph = self.get_graph(lambda x : x**2, color = GREEN)

        self.play(
            ShowCreation(graph),
            run_time = 2
        )
        self.wait()

    def setup_axes(self):
        GraphScene.setup_axes(self)
        self.x_axis.label_direction = UP
        # Additional parametters
        init_val_x = 0
        step_x = 0.5
        end_val_x = 7
        # Position of labels
        values_decimal_x=Range(init_val_x,end_val_x,step_x)
        # List of labels
        list_x=[*["%.1f"%i for i in values_decimal_x]]
        # List touples of (posición,etiqueta)
        values_x = [
            (i,j)
            for i,j in zip(values_decimal_x,list_x)
        ]
        self.x_axis_labels = VGroup()
        for x_val, x_tex in values_x:
            tex = TexMobject(x_tex)
            tex.scale(0.7)
            tex.next_to(self.coords_to_point(x_val, 0), DOWN)
            self.x_axis_labels.add(tex)
        self.play(
            Write(self.x_axis_labels),
            Write(self.x_axis),
            Write(self.y_axis)
        )

class PlotSinCos(GraphScene):
    CONFIG = {
        "y_max" : 1.5,
        "y_min" : -1.5,
        "x_max" : 3*PI/2,
        "x_min" : -3*PI/2,
        "y_tick_frequency" : 0.5,
        "x_tick_frequency" : PI/2,
        "graph_origin" : ORIGIN,
        "y_axis_label": None, # Don't write y axis label
        "x_axis_label": None,
    }
    def construct(self):
        self.setup_axes()
        plotSin = self.get_graph(lambda x : np.sin(x), 
                                    color = GREEN,
                                    x_min=-4,
                                    x_max=4,
                                )
        plotCos = self.get_graph(lambda x : np.cos(x), 
                                    color = GRAY,
                                    x_min=-PI,
                                    x_max=0,
                                )
        plotSin.set_stroke(width=3) # width of line
        plotCos.set_stroke(width=2)
        # Animation
        for plot in (plotSin,plotCos):
            self.play(
                    ShowCreation(plot),
                    run_time = 2
                )
        self.wait()

    def setup_axes(self):
        GraphScene.setup_axes(self)
        # width of edges
        self.x_axis.set_stroke(width=2)
        self.y_axis.set_stroke(width=2)
        # color of edges
        self.x_axis.set_color(RED)
        self.y_axis.set_color(YELLOW)
        # Add x,y labels
        func = TexMobject("\\sin\\theta")
        var = TexMobject("\\theta")
        func.set_color(BLUE)
        var.set_color(PURPLE)
        func.next_to(self.y_axis,UP)
        var.next_to(self.x_axis,RIGHT+UP)
        # Y labels
        self.y_axis.label_direction = LEFT*1.5
        self.y_axis.add_numbers(*[-1,1])
        #Parametters of x labels
        init_val_x = -3*PI/2
        step_x = PI/2
        end_val_x = 3*PI/2
        # List of the positions of x labels
        values_decimal_x=Range(init_val_x,end_val_x,step_x)
        # List of tex objects
        list_x=TexMobject("-\\frac{3\\pi}{2}", #   -3pi/2
                            "-\\pi", #              -pi 
                            "-\\frac{\\pi}{2}", #   -pi/2
                            "\\,", #                 0 (space)
                            "\\frac{\\pi}{2}", #     pi/2
                            "\\pi",#                 pi
                            "\\frac{3\\pi}{2}" #     3pi/2
                          )
        #List touples (position,label)
        values_x = [(i,j)
            for i,j in zip(values_decimal_x,list_x)
        ]
        self.x_axis_labels = VGroup()
        for x_val, x_tex in values_x:
            x_tex.scale(0.7)
            if x_val == -PI or x_val == PI: #if x is equals -pi or pi
                x_tex.next_to(self.coords_to_point(x_val, 0), 2*DOWN) #Put 2*Down
            else: # In another case
                x_tex.next_to(self.coords_to_point(x_val, 0), DOWN)
            self.x_axis_labels.add(x_tex)

        self.play(
            *[Write(objeto)
            for objeto in [
                    self.y_axis,
                    self.x_axis,
                    self.x_axis_labels,
                    func,var
                ]
            ],
            run_time=2
        )