from big_ol_pile_of_manim_imports import *

class Grafica1(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 5, #Subdivisiones de y
        "x_tick_frequency" : 1, #Subdivisiones de x
        "axes_color" : BLUE, #Color de los ejes XY
    }
    def construct(self):
        self.setup_axes(animate=True) #animate=True para animar al mostrar los ejes
        #Definición de gráfica
        grafica = self.get_graph(lambda x : x**2, # Función en numpy 
                                    color = GREEN,
                                    x_min = 2, # Dominio
                                    x_max = 4
                                    )
        #Animar creación de gráfica
        self.play(
        	ShowCreation(grafica),
            run_time = 2
        )
        self.wait()

class Grafica1v2(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 5,
        "x_tick_frequency" : 1,
        "axes_color" : BLUE, #     x y z
        "graph_origin" : np.array((0,0,0)) # Origen de la gráfica, se puede usar LEFT,...
    }
    def construct(self):
        self.setup_axes(animate=True)
        grafica = self.get_graph(lambda x : x**2, 
                                    color = GREEN,
                                    x_min = 2, 
                                    x_max = 4
                                    )
        self.play(
            ShowCreation(grafica),
            run_time = 2
        )
        self.wait()

class Grafica2(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 5,
        "axes_color" : BLUE,
        "x_axis_label" : "$t$",  # Etiqueta de eje x
        "y_axis_label" : "$f(t)$", # Etiqueta de eje y
    }
    def construct(self):
        self.setup_axes() #Ya no usar animate=True
        grafica = self.get_graph(lambda x : x**2, color = GREEN)
        self.play(
        	ShowCreation(grafica),
            run_time = 2
        )
        self.wait()
    # Modificación de los ejes
    def setup_axes(self):
        # Linea por defecto
        GraphScene.setup_axes(self) 
        # Parámetros de las etiquetas de los ejes
        #   Para x
        et_x_inicial = 0
        et_x_final = 7
        pasos_x = 1
        #   Para y
        et_y_inicial = 0
        et_y_final = 50
        pasos_y = 5
        # Posición de las etiquetas (siempre se definen antes de add_numbers)
        #   Para x
        self.x_axis.label_direction = DOWN #DOWN está por defecto así que se puede obviar
        #   Para y
        self.y_axis.label_direction = LEFT
        # Adición de las etiquetas
        #   Para x
        self.x_axis.add_numbers(*range(
                                        et_x_inicial,
                                        et_x_final+pasos_x,
                                        pasos_x
                                    ))
        #   Para y
        self.y_axis.add_numbers(*range(
                                        et_y_inicial,
                                        et_y_final+pasos_y,
                                        pasos_y
                                    ))
        #   Animación Write (se puede modificar a Show...)
        self.play(
            Write(self.x_axis),
            Write(self.y_axis)
        )

class Grafica3(GraphScene):
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
        grafica = self.get_graph(lambda x : x**2, color = GREEN)

        self.play(
            ShowCreation(grafica),
            run_time = 2
        )
        self.wait()

    def setup_axes(self):
        GraphScene.setup_axes(self)
        # Parámetros personalizados
        self.x_axis.add_numbers(*[0,2,5,4])
        # Parámetros de y
        et_y_inicial = 0
        et_y_final = 50
        pasos_y = 5
        self.y_axis.label_direction = LEFT
        self.y_axis.add_numbers(*range(
                                        et_y_inicial,
                                        et_y_final+pasos_y,
                                        pasos_y
                                    ))
        self.play(Write(self.x_axis),Write(self.y_axis))

class Grafica4(GraphScene):
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
        grafica = self.get_graph(lambda x : x**2, color = GREEN)

        self.play(
            ShowCreation(grafica),
            run_time = 2
        )
        self.wait()

    def setup_axes(self):
        GraphScene.setup_axes(self)
        self.x_axis.label_direction = UP
        self.x_axis.add_numbers(*[3.5,5,4]) #El 3.5 lo redondea a 4
        self.y_axis.label_direction = LEFT
        self.y_axis.add_numbers(*range(0, 50+5, 5))
        self.play(Write(self.x_axis),Write(self.y_axis))

class Grafica5(GraphScene):
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
        grafica = self.get_graph(lambda x : x**2, color = GREEN)

        self.play(
            ShowCreation(grafica),
            run_time = 2
        )
        self.wait()

    def setup_axes(self):
        GraphScene.setup_axes(self)
        self.x_axis.label_direction = UP
        valores_x = [
            (3.5,"3.5"), # (posición 3.5, etiqueta "3.5")
            (4.5,"\\frac{9}{2}") # (posición 4.5, etiqueta 9/2)
        ]
        self.x_axis_labels = VGroup() # Crea un grupo de objetos
        #   pos.   tex.
        for x_val, x_tex in valores_x:
            tex = TexMobject(x_tex) # Convierte etiqueta a TexMobject
            tex.scale(0.7) # Lo hace más pequeño
            tex.next_to(self.coords_to_point(x_val, 0), DOWN) #Lo situa en la cordenada
            self.x_axis_labels.add(tex) #Lo agrega al grupo de objetos
        self.play(
            Write(self.x_axis_labels), #Anima el grupo de objetos
            Write(self.x_axis),
            Write(self.y_axis)
        )

class Grafica6(GraphScene):
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
        grafica = self.get_graph(lambda x : x**2, color = GREEN)

        self.play(
            ShowCreation(grafica),
            run_time = 2
        )
        self.wait()

    def setup_axes(self):
        GraphScene.setup_axes(self)
        self.x_axis.label_direction = UP
        # Lista de etiquetas
        lista_x = ["0","0.5","1","1.5","2"]
        # Lista con valores de posiciones
        valor_decimal_x=[0,0.5,1,1.5,2]
        # Parejas de (posición,etiqueta)
        valores_x = [
            (i,j)
            for i,j in zip(valor_decimal_x,lista_x)
        ]
        self.x_axis_labels = VGroup()
        for x_val, x_tex in valores_x:
            tex = TexMobject(x_tex)
            tex.scale(0.7)
            tex.next_to(self.coords_to_point(x_val, 0), DOWN)
            self.x_axis_labels.add(tex)
        self.play(
            Write(self.x_axis_labels), #Anima el grupo de objetos
            Write(self.x_axis),
            Write(self.y_axis)
        )

class Grafica7(GraphScene):
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
        grafica = self.get_graph(lambda x : x**2, color = GREEN)

        self.play(
            ShowCreation(grafica),
            run_time = 2
        )
        self.wait()

    def setup_axes(self):
        GraphScene.setup_axes(self)
        self.x_axis.label_direction = UP
        # Parametros de posiciones
        valor_en_x = 0
        pasos_x = 0.5
        valor_fin_x = 7
        # Valores de posiciones
        valor_decimal_x=list(np.arange(valor_en_x,valor_fin_x+pasos_x,pasos_x))
        # Lista de etiquetas
        lista_x=[]
        for i in valor_decimal_x:
          lista_x.append("%.1f"%i)
        # Parejas de (posición,etiqueta)
        valores_x = [
            (i,j)
            for i,j in zip(valor_decimal_x,lista_x)
        ]
        self.x_axis_labels = VGroup()
        for x_val, x_tex in valores_x:
            tex = TexMobject(x_tex)
            tex.scale(0.7)
            tex.next_to(self.coords_to_point(x_val, 0), DOWN)
            self.x_axis_labels.add(tex)
        self.play(
            Write(self.x_axis_labels),
            Write(self.x_axis),
            Write(self.y_axis)
        )

class GraficaSenoCoseno1(GraphScene):
    CONFIG = {
        "y_max" : 1.5,
        "y_min" : -1.5,
        "x_max" : 3*PI/2,
        "x_min" : -3*PI/2,
        "y_tick_frequency" : 0.5,
        "x_tick_frequency" : PI/2,
        "graph_origin" : ORIGIN,
        "y_axis_label": None, #No escribe etiqueta de y
        "x_axis_label": None, #No escribe etiqueta de x
    }
    def construct(self):
        self.setup_axes()
        graficaSeno = self.get_graph(lambda x : np.sin(x), 
                                    color = GREEN,
                                    x_min=-4,
                                    x_max=4,
                                )
        graficaCoseno = self.get_graph(lambda x : np.cos(x), 
                                    color = GRAY,
                                    x_min=-PI,
                                    x_max=0,
                                )
        graficaSeno.set_stroke(width=3) # Grosor de linea
        graficaCoseno.set_stroke(width=2)
        # Anima una por una
        for grafica in (graficaSeno,graficaCoseno):
            self.play(
                    ShowCreation(grafica),
                    run_time = 2
                )
        self.wait()

    def setup_axes(self):
        GraphScene.setup_axes(self)
        #Grosor de ejes
        self.x_axis.set_stroke(width=2)
        self.y_axis.set_stroke(width=2)
        #Color de ejes
        self.x_axis.set_color(RED)
        self.y_axis.set_color(YELLOW)
        #Modificar posición de etiquetas x,y
        func = TexMobject("\\mbox{sen}\\theta")
        var = TexMobject("\\theta")
        func.set_color(BLUE)
        var.set_color(PURPLE)
        func.next_to(self.y_axis,UP)
        var.next_to(self.x_axis,RIGHT+UP)
        #Etiquetas del eje y
        self.y_axis.label_direction = LEFT*1.5
        self.y_axis.add_numbers(*[-1,1])
        #Parámetros de valores de posiciones en x
        valor_en_x = -3*PI/2
        pasos_x = PI/2
        valor_fin_x = 3*PI/2
        #Lista de valores de posiciones de x
        valor_decimal_x=list(np.arange(valor_en_x,valor_fin_x+pasos_x,pasos_x))
        #Lista de valores TexMobject de etiquetas en x
        lista_x=TexMobject("-\\frac{3\\pi}{2}", #   -3pi/2
                            "-\\pi", #              -pi 
                            "-\\frac{\\pi}{2}", #   -pi/2
                            "\\,", #                 0 (espacio)
                            "\\frac{\\pi}{2}", #     pi/2
                            "\\pi",#                 pi
                            "\\frac{3\\pi}{2}" #     3pi/2
                          )
        #Lista de (posición,etiqueta)
        valores_x = [(i,j)
            for i,j in zip(valor_decimal_x,lista_x)
        ]
        self.x_axis_labels = VGroup()
        for x_val, x_tex in valores_x:
            x_tex.scale(0.7) #No es necesario usar variable tex
            if x_val == -PI or x_val == PI: #si x es igual a -pi o pi
                x_tex.next_to(self.coords_to_point(x_val, 0), 2*DOWN) #coloca más abajo
            else: # Si eso no ocurre...
                x_tex.next_to(self.coords_to_point(x_val, 0), DOWN)
            self.x_axis_labels.add(x_tex)
        #Anima la aparición del conjunto
        self.play(*[Write(objeto)
            for objeto in [
                    self.y_axis,
                    self.x_axis,
                    self.x_axis_labels,
                    func,var
                ]
            ],
            run_time=2
        )

class GraficaSenoCoseno2(GraphScene):
    CONFIG = {
        "y_max" : 1.5,
        "y_min" : -1.5,
        "x_max" : 3*PI/2,
        "x_min" : -3*PI/2,
        "y_tick_frequency" : 0.5,
        "x_tick_frequency" : PI/2,
        "graph_origin" : ORIGIN,
        "y_axis_label": None, #No escribe etiqueta de y
        "x_axis_label": None, #No escribe etiqueta de x
    }
    def construct(self):
        self.setup_axes()
        graficaSeno = self.get_graph(lambda x : np.sin(x), 
                                    color = GREEN,
                                    x_min=-4,
                                    x_max=4,
                                )
        graficaCoseno = self.get_graph(lambda x : np.cos(x), 
                                    color = GRAY,
                                    x_min=-PI,
                                    x_max=0,
                                )
        graficaSeno.set_stroke(width=3) # Grosor de linea
        graficaCoseno.set_stroke(width=2)
        # Anima las dos juntas
        self.play(*[
                ShowCreation(grafica)
                for grafica in (
                        graficaSeno,
                        graficaCoseno,
                        )
            ],
            run_time = 2)

    def setup_axes(self):
        GraphScene.setup_axes(self)
        #Grosor de ejes
        self.x_axis.set_stroke(width=2)
        self.y_axis.set_stroke(width=2)
        #Color de ejes
        self.x_axis.set_color(RED)
        self.y_axis.set_color(YELLOW)
        #Modificar posición de etiquetas x,y
        func = TexMobject("\\mbox{sen}\\theta")
        var = TexMobject("\\theta")
        func.set_color(BLUE)
        var.set_color(PURPLE)
        func.next_to(self.y_axis,UP)
        var.next_to(self.x_axis,RIGHT+UP)
        #Etiquetas del eje y
        self.y_axis.label_direction = LEFT*1.5
        self.y_axis.add_numbers(*[-1,1])
        #Parámetros de valores de posiciones en x
        valor_en_x = -3*PI/2
        pasos_x = PI/2
        valor_fin_x = 3*PI/2
        #Lista de valores de posiciones de x
        valor_decimal_x=list(np.arange(valor_en_x,valor_fin_x+pasos_x,pasos_x))
        #Lista de valores TexMobject de etiquetas en x
        lista_x=TexMobject("-\\frac{3\\pi}{2}", #   -3pi/2
                            "-\\pi", #              -pi 
                            "-\\frac{\\pi}{2}", #   -pi/2
                            "\\,", #                 0 (espacio)
                            "\\frac{\\pi}{2}", #     pi/2
                            "\\pi",#                 pi
                            "\\frac{3\\pi}{2}" #     3pi/2
                          )
        #Lista de (posición,etiqueta)
        valores_x = [(i,j)
            for i,j in zip(valor_decimal_x,lista_x)
        ]
        self.x_axis_labels = VGroup()
        for x_val, x_tex in valores_x:
            x_tex.scale(0.7) #No es necesario usar variable tex
            if x_val == -PI or x_val == PI: #si x es igual a -pi o pi
                x_tex.next_to(self.coords_to_point(x_val, 0), 2*DOWN) #coloca más abajo
            else: # Si eso no ocurre...
                x_tex.next_to(self.coords_to_point(x_val, 0), DOWN)
            self.x_axis_labels.add(x_tex)
        #Anima la aparición del conjunto
        self.play(*[Write(objeto)
            for objeto in [
                    self.y_axis,
                    self.x_axis,
                    self.x_axis_labels,
                    func,var
                ]
            ],
            run_time=2
        )