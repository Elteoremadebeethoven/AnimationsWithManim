from manimlib.imports import *

class CheckSVG(Scene):
    CONFIG={
    "camera_config":{"background_color": WHITE},
    "svg_type":"svg",
    "get_cero":False,
    "file":"",
    "text":None,
    "scale":None,
    "width":None,
    "height":None,
    "color":BLACK,
    "angle":0,
    "flip":False,
    "flip_edge":UP,
    "fill_opacity": 1,
    "fill_color": None,
    "stroke_color": None,
    "stroke_opacity":1,
    "stroke_width": 3,
    "number_type":"Font",
    "sheen_factor":None,
    "sheen_direction":None,
    "gradient_color":False,
    "gradient_colors":[BLUE,RED,GREEN],
    "cycle_color":False,
    "cycle_colors":[RED,BLUE,GREEN,YELLOW,PINK,ORANGE,PURPLE,TEAL,GRAY],
    "numbers_scale":0.5,
    "show_numbers": False,
    "animation": False,
    "remove": [],
    "direction_numbers": UP,
    "color_numbers": GOLD,
    "space_between_numbers":0,
    "show_elements":[],
    "color_element":BLUE,
    "set_size":"width",
    "remove_stroke":[],
    "show_stroke":[],
    "show_stroke_stroke":1,
    "warning_color":RED,
    "wait_time":3,
    "show_removers":True,
    "background_stroke_width":0
    }
    def construct(self):
        pre_imagen = self.get_svg()
        if self.get_cero:
            self.imagen=pre_imagen[0]
        else:
            self.imagen=pre_imagen

        # Style
        self.imagen.set_color(color=self.color)\
                   .set_style(
                  fill_opacity=self.fill_opacity,
                  stroke_color=self.stroke_color,
                  stroke_width=self.stroke_width,
                  stroke_opacity=self.stroke_opacity,
                  sheen_factor=self.sheen_factor,
                  sheen_direction=self.sheen_direction,
                )
        if self.gradient_color:
            self.imagen.set_color_by_gradient(*self.gradient_colors)
        if self.cycle_color:
            get_cycle_color=it.cycle(self.cycle_colors)
            for obj in self.imagen:
                obj.set_color(next(get_cycle_color))

        # Size settings
        if self.width!=None:
            self.imagen.set_width(self.width)
        elif self.height!=None:
            self.imagen.set_height(self.height)
        elif self.scale!=None:
            self.imagen.scale(self.scale)
        else:
            self.imagen.set_width(FRAME_WIDTH)
            if self.imagen.get_height()>FRAME_HEIGHT:
                self.imagen.set_height(FRAME_HEIGHT)

        # Orientation
        self.imagen.rotate(self.angle)
        if self.flip==True:
            self.imagen.flip(self.flip_edge)

        for st in self.remove_stroke:
            self.imagen[st].set_stroke(None,0)
        for st in self.show_stroke:
            self.imagen[st].set_stroke(None,self.show_stroke_stroke)

        self.personalize_image()

        if self.show_numbers==True:
            self.print_formula(self.imagen.copy(),
                self.numbers_scale,
                self.direction_numbers,
                self.remove,
                self.space_between_numbers,
                self.color_numbers)

        if self.animation==True:
            self.play(DrawBorderThenFill(self.imagen))
        elif self.show_numbers==False:
            self.add(self.imagen)

        self.wait(self.wait_time)
        self.return_elements(self.imagen,self.show_elements)

    def get_svg(self):
        if self.svg_type == "svg":
            try:
                pre_imagen = SVGMobject("%s"%self.file)
            except:
                pre_imagen = self.custom_object()
        elif self.svg_type == "text":
            pre_imagen = self.import_text()
        else:
            pre_imagen = self.custom_object()
        return pre_imagen

    def import_text(self):
        return self.text

    def custom_object(self):
        return VGroup()

    def personalize_image(self):
        pass

    def print_formula(self,text,inverse_scale,direction,exception,buff,color):
        text.set_color(self.warning_color)
        self.add(text)

        for j in range(len(text)):
            permission_print=True
            for w in exception:
                if j==w:
                    permission_print=False
            if permission_print:
                self.add(self.imagen[j])

        if self.show_removers:
            for obj in exception:
                self.add_foreground_mobject(text[obj])

        c=0
        for j in range(len(text)):
            permission_print=True
            if self.number_type=="TextMobject":
                element = TexMobject("%d" %c,color=color,
                background_stroke_width=self.background_stroke_width)
            else:
                element = Text("%d" %c).set_color(color)
            element.scale(inverse_scale)
            element.next_to(text[j],direction,buff=buff)
            for w in exception:
                if j==w:
                    permission_print=False
            if permission_print:
                self.add_foreground_mobjects(element)
            c = c + 1 

    def return_elements(self,formula,adds):
        for i in adds:
            self.add_foreground_mobjects(formula[i].set_color(self.color_element),
                TexMobject("%d"%i,color=self.color_element,background_stroke_width=0)\
                .scale(self.numbers_scale)\
                .next_to(formula[i],self.direction_numbers,buff=self.space_between_numbers)
                )

class CheckText(CheckSVG):
    CONFIG={
    "svg_type":"text",
    "get_cero":True,
    }

class CheckSVGNumbers(CheckSVG):
    CONFIG={
    "show_numbers": True,
    }

class CheckTextNumbers(CheckText):
    CONFIG={
    "show_numbers": True,
    }

class CheckSVGPoints(CheckSVGNumbers):
    CONFIG={
    "camera_config":{"background_color": BLACK},
    "color":WHITE,
    "show_element_points":[],
    "background_stroke_width":4,
    "shadow_point_number":3,
    "points_colors":[RED,BLUE,GREEN],
    "point_radius":0.05,
    "size_points_numbers":0.09,
    "number_point_direction":UP,
    "number_point_buff":0
    }
    def personalize_image(self):
        cycle_colors=it.cycle(self.points_colors)
        for n_obj in self.show_element_points:
            for obj in self.imagen[n_obj]:
                count=0
                for point in obj.points:
                    next_color=next(cycle_colors)
                    punto=Dot(color=next_color,radius=self.point_radius)
                    punto.move_to(point)
                    if self.number_type=="TextMobject":
                        number_point=Text("%d"%count,
                        color=punto.get_color(),
                        background_stroke_width=self.shadow_point_number
                        )
                    else:
                        number_point=Text("%d"%count)
                        number_point.match_color(punto)
                    number_point.set_height(self.size_points_numbers)\
                                .next_to(punto,
                                    self.number_point_direction,
                                    buff=self.number_point_buff
                                    )
                    self.add_foreground_mobjects(punto,number_point)
                    count+=1


    def print_formula(self,text,inverse_scale,direction,exception,buff,color):
        text.set_color(self.warning_color)
        self.add(text)

        for j in range(len(text)):
            permission_print=True
            for w in exception:
                if j==w:
                    permission_print=False
            if permission_print:
                self.add(self.imagen[j])

        if self.show_removers:
            for obj in exception:
                self.add_foreground_mobject(text[obj])

        c=0
        for j in range(len(text)):
            permission_print=True
            if self.number_type=="TextMobject":
                element = TexMobject("%d:%d"%(c,len(text.points)),color=color,
                background_stroke_width=self.background_stroke_width)
            else:
                element = Text("%d:%d"%(c,len(text.points))).set_color(color)
            element.scale(inverse_scale)
            element.next_to(text[j],direction,buff=buff)
            for w in exception:
                if j==w:
                    permission_print=False
            if permission_print:
                self.add_foreground_mobjects(element)
            c = c + 1 
