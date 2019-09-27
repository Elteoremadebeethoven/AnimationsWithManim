class TikzMobject(TextMobject):
    CONFIG = {
        "stroke_width": 3,
        "fill_opacity": 0,
        "stroke_opacity": 1,
    }

class ExampleTikz(Scene):
    def construct(self):
        circuit = TikzMobject(r"""
            \begin{circuitikz}[american voltages]
            \draw
              (0,0) to [short, *-] (6,0)
              to [V, l_=$\mathrm{j}{\omega}_m \underline{\psi}^s_R$] (6,2) 
              to [R, l_=$R_R$] (6,4) 
              to [short, i_=$\underline{i}^s_R$] (5,4) 
              (0,0) to [open,v^>=$\underline{u}^s_s$] (0,4) 
              to [short, *- ,i=$\underline{i}^s_s$] (1,4) 
              to [R, l=$R_s$] (3,4)
              to [L, l=$L_{\sigma}$] (5,4) 
              to [short, i_=$\underline{i}^s_M$] (5,3) 
              to [L, l_=$L_M$] (5,0); 
              \end{circuitikz}
            """
            )
        self.play(Write(circuit))
        self.wait()
