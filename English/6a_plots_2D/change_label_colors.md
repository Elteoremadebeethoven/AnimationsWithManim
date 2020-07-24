# Change labels colors in `GraphScene`

Add this to the `CONFIG` dictionary:
```python
    "x_label_color":RED,
    "y_label_color":BLUE
```
In the `setup_axes` method change the lines
```python
            x_label = TextMobject(self.x_axis_label)
            # and
            y_label = TextMobject(self.y_axis_label)
```
with
```python
            x_label = TextMobject(self.x_axis_label,color=self.x_label_color)
            # and
            y_label = TextMobject(self.y_axis_label,color=self.y_label_color)
```
Result:

<p align="center"><img src ="/English/6a_plots_2D/gifs/ChanceColorLabels.png" /></p>
