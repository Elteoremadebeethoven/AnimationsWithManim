# Conda installation
## Steps

You need to have LaTeX (MikTeX, TeXLive or MacTeX), FFmpeg and Sox installed.

1. Open your conda shell
2. Clone the repository: `git clone https://github.com/3b1b/manim.git`
3. Move to the repository: `cd manim`
4. Create the enviroment: `conda env create --file=environment.yml --name manimenv`
5. Wait for the installation to complete, and actiavate the enviroment with: `conda activate manimenv`
6. Run: `python -m manim example_scenes.py SquareToCircle -pl`

It may be that you need to install ffmpeg with x264 support, if that is the case try **some** of this lines:

```sh
conda install x264=='1!152.20180717' ffmpeg=4.0.2 -c conda-forge
# or
conda install -c conda-forge x264
```
