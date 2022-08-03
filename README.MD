# CategoryWalls

Takes the most prominent colour in an image and makes a sidebar in that colour in the top-left corner of that image.

Meant to be used as a hacky way to "colour-code" Windows 11 virtual desktops.

## Examples
### Blank example of how the wallpapers look in the desktop switcher
![Blank example](https://i.imgur.com/EHYI7U7)
### How I use this project to organize my desktops
![Radded's own setup](https://i.imgur.com/N1KKb5r)
### Same example as above but without the edited wallpapers
![Same as above but without the edited wallpapers](https://i.imgur.com/haXqbd2)

## Installation and usage instructions
1. Clone the repo with\
```git clone github.com/RaddedMC/CategoryWalls```

2. Install dependencies\
```pip -r requirements.txt```

3. Load your favourite wallpapers into `source-images`

4. Adjust resolution and edge thickness as you like in `pil-walls.py` under `### USER-CONFIGURABLES ###`

4. Run the script\
```python pil-walls.py```

5. See your images appear in `output-images`

6. Organize your Windows 11 virtual desktops!\
For each virtual desktop you have open, right-click on it, 'choose background', and pick one of the images in `output-images`