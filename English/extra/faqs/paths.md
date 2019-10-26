# How to create paths in Manim with set of points
## Some useful functions:
```python
def coord(x,y,z=0):
    return np.array([x,y,z])

def getX(mob):
    return mob.get_center()[0]

def getY(mob):
    return mob.get_center()[1]
```

## Abstract class
This class is not a scene, it is the basis for creating our scenes.
```python
# Abstract class:
class PathScene(Scene):
    CONFIG = {
        "x_coords":[0,  1, 3,  -2, -3],
        "y_coords":[3, -2, 1, 2.5, -1]
    }
    """
    The setup method it is executed before the construct method, 
    so whatever they write in the setup method will be executed 
    before the construct method
    """
    def setup(self):
        self.screen_grid = ScreenGrid()
        # tuples = [(0,3),(1,-2)...]
        self.tuples = list(zip(self.x_coords,self.y_coords))

        dots,labels,numbers = self.get_all_mobs()
        self.add(self.screen_grid,dots,labels,numbers)

    def get_dots(self,coords):
        # This is called list comprehension, learn to use it here:
        # https://www.youtube.com/watch?v=AhSvKGTh28Q
        dots = VGroup(*[Dot(coord(x,y)) for x,y in coords])
        return dots

    def get_dot_labels(self,dots,direction=RIGHT):
        labels = VGroup(*[
            # This is called f-strings, learn to use it here:
            # https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
            TexMobject(f"({getX(dot)},{getY(dot)})",height=0.3)\
                      .next_to(dot,direction,buff=SMALL_BUFF) 
                      # This is called Multi-line statement, learn how to use it here:
                      # https://www.programiz.com/python-programming/statement-indentation-comments
            for dot in dots
            ])
        return labels

    def get_dot_numbers(self,dots):
        numbers = VGroup(*[
            TextMobject(f"{n}",height=0.2).next_to(dot,DOWN,buff=SMALL_BUFF)
            for n,dot in zip(range(1,len(dots)+1),dots)
            ])
        return numbers

    def get_all_mobs(self):
        dots = self.get_dots(self.tuples)
        labels = self.get_dot_labels(dots)
        numbers = self.get_dot_numbers(dots)
        return dots,labels,numbers
```

## Show Points
```python
class ShowPoints(PathScene):
    pass
```

<p align="center"><img src ="/English/extra/faqs/gifs/ShowPoints.png" width="800" /></p>

## Path as corners
```python
class PathAsCorners(PathScene):
    def construct(self):
        path = VMobject()
        path.set_points_as_corners([*[coord(x,y) for x,y in self.tuples]])
        self.add(path)
```

<p align="center"><img src ="/English/extra/faqs/gifs/PathAsCorners.png" width="800" /></p>

## Path smoothly
```python
class PathSmoothly(PathScene):
    def construct(self):
        path = VMobject()
        path.set_points_smoothly([*[coord(x,y) for x,y in self.tuples]])
        self.add(path)
```

<p align="center"><img src ="/English/extra/faqs/gifs/PathSmoothly.png" width="800" /></p>

## Bezier points of a path
```python
class PathBezierPoints(PathScene):
    def construct(self):
        path = VMobject()
        path.set_points_smoothly([*[coord(x,y) for x,y in self.tuples]])
        bezier_points = VGroup(*[Dot(coord,color=RED) for coord in path.points])
        self.add(path,bezier_points)
```

<p align="center"><img src ="/English/extra/faqs/gifs/PathBezierPoints.png" width="800" /></p>

## Append points
```python
class AppendPoints(PathScene):
    def construct(self):
        path = VMobject()
        path.set_points_as_corners([*[coord(x,y) for x,y in self.tuples]])
        self.add(path)
        self.wait()
        new_points = np.array([coord(-5,1),coord(-1,1)])
        new_dots = self.get_dots(new_points[:,:2])
        """       Special atention to this: ----
        This is an slice, see: https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/
        new_points = 
        [   Columns:
             0   1  2
            [-5  1  0]   <- Row 0
            [-1  1  0]   <- Row 1
                        ]
        So, the first ":" means all rows
        The ":2" means only take the elements from the first column to the second one,
        that is, the columns 0 and 1
        """
        new_labels = self.get_dot_labels(new_dots,UP)
        path.become(
            VMobject().set_points_as_corners([*path.points,*new_points])
        )
        # The most recent version have new methods that can do this more easy.
        VGroup(new_dots,new_labels).set_color(TEAL)
        self.add(new_dots,new_labels)
        self.wait(2)
```

<p align="center"><img src ="/English/extra/faqs/gifs/AppendPoints.gif" width="800" /></p>

## Change path style
```python
class TransformPathStyle(PathScene):
    def construct(self):
        path = VMobject()
        path.set_points_as_corners([*[coord(x,y) for x,y in self.tuples]])
        self.add(path)
        self.play(path.make_smooth)
        self.wait()
        """
        There are 3 methods:
            path.make_smooth()
            path.make_jagged()
            path.change_anchor_mode()
        """
```

<p align="center"><img src ="/English/extra/faqs/gifs/TransformPathStyle.gif" width="800" /></p>

More methods in the [current version](https://github.com/3b1b/manim/blob/master/manimlib/mobject/types/vectorized_mobject.py#L397)
