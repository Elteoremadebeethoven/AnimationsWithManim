# Enable `submobject_mode` in the most recent version of Manim (jun/21)

## Open manimlib/animation/animation.py and add this parameters to Animation CONFIG:

```python3
        "submobject_mode": "None",
        "lag_factor": 2,
```

## Replace `get_sub_alpha`.

The [original code](https://github.com/3b1b/manim/blob/41792fdb5f9578c7e49455e19416b8474f29f2a8/manimlib/animation/animation.py#L130) is ([version of jun/21](https://github.com/3b1b/manim/tree/41792fdb5f9578c7e49455e19416b8474f29f2a8)):

```python3
    #manimlib/animation/animation.py, line 130-138
    def get_sub_alpha(self, alpha, index, num_submobjects):
        # TODO, make this more understanable, and/or combine
        # its functionality with AnimationGroup's method
        # build_animations_with_timings
        lag_ratio = self.lag_ratio
        full_length = (num_submobjects - 1) * lag_ratio + 1
        value = alpha * full_length
        lower = index * lag_ratio
        return np.clip((value - lower), 0, 1)
```

Replace with:

```python3
    def get_sub_alpha(self, alpha, index, num_submobjects):
        # TODO, make this more understanable, and/or combine
        # its functionality with AnimationGroup's method
        # build_animations_with_timings
        lag_ratio = self.lag_ratio
        full_length = (num_submobjects - 1) * lag_ratio + 1
        value = alpha * full_length
        lower = index * lag_ratio
        if self.submobject_mode in ["lagged_start", "smoothed_lagged_start"]:
            prop = float(index) / num_submobjects
            if self.submobject_mode is "smoothed_lagged_start":
                prop = smooth(prop)
            lf = self.lag_factor
            return np.clip(lf * alpha - (lf - 1) * prop, 0, 1)
        elif self.submobject_mode == "one_at_a_time":
            lower = float(index) / num_submobjects
            upper = float(index + 1) / num_submobjects
            return np.clip((alpha - lower) / (upper - lower), 0, 1)
        elif self.submobject_mode == "all_at_once":
            return alpha
        return np.clip((value - lower), 0, 1)
```
