from https://github.com/3b1b/manim/pull/1013

you can use it as follow.
save html file from https://tohtml.com/cpp/
```python
from manimlib.mobject.CodeMobject import *
code = CodeMobject("code.html",
                           coordinates=[-5,3],
                           run_time=3,
                           scale_factor=1.6,
                           line_spacing=0.2,
                           tab_spacing=0.6)
        #self.draw_code_all_lines_at_a_time(code)
        code.scale(1)
        self.play(Write(code),run_time=1)

    def draw_code_all_lines_at_a_time(self, code):
        self.play(*[Write(code[i]) for i in range(code.__len__())],run_time=code.run_time)
```
coordinate point is LEFT+UP corner. 
'code' is a 2d array of characters.
for example to access first 5 characters from line 2 use code[2][0:5]
code[2][0:5].set_color(RED)

Output will be looks like 
![Ceatures](https://raw.githubusercontent.com/NavpreetDevpuri/LyndaDownloader/master/screenshots/codex.png)

* It solves the following problems
1) display code with color highlighted
2) manage to print single LaTeX character '{' or '}' from https://github.com/3b1b/manim/issues/941#issuecomment-620319805
3) convert simple string to LaTeX string programmatically from https://github.com/3b1b/manim/issues/1010#issuecomment-620345024
