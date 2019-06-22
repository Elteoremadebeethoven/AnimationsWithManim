# Copy the following commands:

## manimlib/constans.py
```python3
CUSTOM_QUALITY_CAMERA_CONFIG = {
    "pixel_height": 720,
    "pixel_width": 1280,
    "frame_rate": 10,
}
```
```python3
def set_custom_quality(height,fps):
    video_parameters=[
        ("pixel_height",height),
        ("pixel_width",int(height*16/9)),
        ("frame_rate",fps)
    ]
    for v_property,v_value in video_parameters:
        CUSTOM_QUALITY_CAMERA_CONFIG[v_property]=v_value
```

## manimlib/config.py

```python3
parser.add_argument(
            "-k","--custom_quality",
            action="store_true",
            help="Custom size in file",
        ),
        parser.add_argument(
            "-x","--fps",
            help="Custom fps",
        ),
```
```python3
  "fps": args.fps,
```
```python3
  if args.low_quality:
        camera_config.update(manimlib.constants.LOW_QUALITY_CAMERA_CONFIG)
    elif args.medium_quality:
        camera_config.update(manimlib.constants.MEDIUM_QUALITY_CAMERA_CONFIG)
    elif args.custom_quality:
        try:
            manimlib.constants.CUSTOM_QUALITY_CAMERA_CONFIG["frame_rate"]=int(args.fps)
        except:
            pass
        camera_config.update(manimlib.constants.CUSTOM_QUALITY_CAMERA_CONFIG)
    else:
        camera_config.update(manimlib.constants.PRODUCTION_QUALITY_CAMERA_CONFIG)
```
