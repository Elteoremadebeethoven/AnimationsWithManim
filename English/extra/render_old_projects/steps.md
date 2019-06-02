# Learn Manim by yourself.
This tutorial works with [this manim version (feb/03/19)](https://github.com/3b1b/manim/tree/3b088b12843b7a4459fe71eba96b70edafb7aa78). 

## 1. Download this files.
### 1.1 Download this image with the name "generic.png" and place it in ```media/designs/raster_images```

<p align="center"><img src ="/English/extra/render_old_projects/archivos/generic.png" width="400" /></p>

### 1.2 Download this image with the name "generic.svg" and place it in ```media/designs/svg_images```

<p align="center"><img src ="/English/extra/render_old_projects/archivos/generic.svg" width="400" /></p>

### 1.3 Copy the three .svg files from ```manimlib/files``` to ```media/designs/svg_images```

### 1.4 Download [this sound file](https://drive.google.com/open?id=1V_LpJoidm2tAVVBusKaHlky2-MLehTuM) with the name "generic_sound.wav" and place it in ```media/designs/sounds```


## 2. Modify the following files:

### 2.1 ```manimlib/mobject/coordinate_systems.py``` Add this code in the line 54:

```python3
    def get_axis(self, min_val, max_val, axis_config):
        new_config = merge_config([
            axis_config,
            {"x_min": min_val, "x_max": max_val},
            self.number_line_config,
        ])
        return NumberLine(**new_config)
```
<p align="center"><img src ="/English/extra/render_old_projects/capturas/coord_syst.png" width="700" /></p>


### 2.2 Add this line in ```manimlib/mobject/svg/svg_mobject.py```

```python3
            os.path.join(SVG_IMAGE_DIR, "generic.svg")
```

<p align="center"><img src ="/English/extra/render_old_projects/capturas/capt2.png" width="700" /></p>

### 2.3 Open ```manimlib/mobject/types/image_mobject.py``` and replaces the selected part of the left side with the code that is on the right side.



<p align="center"><img src ="/English/extra/render_old_projects/capturas/capt3.png"/></p>

Código:
```python3
            path=self.select_image(filename_or_array)
            #path = get_full_raster_image_path(filename_or_array)
            image = Image.open(path).convert(self.image_mode)
            self.pixel_array = np.array(image)
        else:
            self.pixel_array = np.array(filename_or_array)
        self.change_to_rgba_array()
        if self.invert:
            self.pixel_array[:, :, :3] = 255 - self.pixel_array[:, :, :3]
        AbstractImageMobject.__init__(self, **kwargs)

    def select_image(self,file_name):
        extensions=[".jpg", ".png", ".gif"]
        possible_paths = [file_name]
        possible_paths += [
            os.path.join(RASTER_IMAGE_DIR, file_name + extension)
            for extension in ["", *extensions]
        ]
        possible_paths+=[os.path.join(RASTER_IMAGE_DIR, "generic.png")]
        for path in possible_paths:
            if os.path.exists(path):
                return path
```

### 2.4 Open ```manimlib/for_3b1b_videos/pi_creature.py``` and replaces the selected part of the left side with the code that is on the right side.


<p align="center"><img src ="/English/extra/render_old_projects/capturas/capt4.png"/></p>

Código:
```python3
                "PiCreatures_plain.svg"
```

### 2.5 Open ```manimlib/mobject/svg/drawings.py``` and replaces the selected part of the left side with the code that is on the right side.

<p align="center"><img src ="/English/extra/render_old_projects/capturas/capt5.png"/></p>

Códigos:
```python3
        "file_name": "Bubbles_speech.svg",
```
------------------------------------
```python3
            SVGMobject.__init__(self,file_name="Bubbles_speech" ,**kwargs)
```

### 2.6 Open ```manimlib/once_useful_constructs/light.py``` and add this code in the 21 line:

```python3
from manimlib.utils.space_ops import get_norm
```

<p align="center"><img src ="/English/extra/render_old_projects/capturas/capt6.png" width="700"/></p>

### 2.7 Open ```manimlib/scene/three_d_scene.py``` and replache the 149 with this line:

```python3
        if self.camera_config["pixel_width"] == PRODUCTION_QUALITY_CAMERA_CONFIG["pixel_width"]:
```

<p align="center"><img src ="/English/extra/render_old_projects/capturas/capt7.png"/></p>

### 2.7 Open ```manimlib/utils/sounds.py``` and make the changes shown in the code above:

<p align="center"><img src ="/English/extra/render_old_projects/capturas/sound.png"/></p>


```python3
# Add this code below line 41
def select_sound(sound_file_name):
    try_sound=os.path.join(SOUND_DIR, sound_file_name)
    if os.path.exists(try_sound):
        return sound_file_name
    else:
        return "generic_sound"

# Locate the cursor at the end of line 36, create a new line and paste the following:
        select_sound(sound_file_name),
```
