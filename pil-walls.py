# Radded's CategoryWalls
# Adds solid-colour edges to any image provided. Useful for colour-coding Windows 11 virtual desktops.


### IMPORTS ###
import os
from PIL import Image, ImageDraw
import multiprocessing
from termcolor import cprint as printColoured


### USER-CONFIGURABLES ###
sourcedirectory = os.path.abspath(os.getcwd()) + "/" + "source-images" + "/" # Just tied to the source-images folder so far
outputdirectory = os.path.abspath(os.getcwd()) + "/" + "output-images" + "/" # Just tied to the output-images folder so far
crop_resolution = (1920, 1080)
edge_thickness = 40 # Pixels


### HELPERS ###
def print_info_text():
    printColoured("Category Wallpaper generator for Windows 11", "red")
    printColoured("By Radded", "blue")

class categoryImage():
    source_image = ""
    final_image = ""
    path = ""
    name = ""
    color = ""

    def __init__(self, path, name):
        self.path = path
        self.name = name

    def process(self):
        printColoured("Starting processing of image " + self.path + "...", "cyan")
        self.load_source_image()
        self.colorgram_image()
        self.generate_categorized_image()
        self.save_image()

    def load_source_image(self):
        printColoured("Loading " + self.path + " ...", "white", "on_yellow")
        self.source_image = Image.open(self.path)
        print("Image " + self.path + " loaded!")

    def colorgram_image(self):
        import colorgram

        # Get colour
        printColoured("Getting color of image: " +self.path, "white", "on_magenta")
        self.color = colorgram.extract(self.path, 1)[0].rgb

        # Adjust colour
        rgb_scale_ratio = min(255/(self.color[0]+1), 255/(self.color[1]+1), 255/(self.color[2]+1))
        from math import ceil
        self.color = (
            ceil(rgb_scale_ratio*self.color[0]),
            ceil(rgb_scale_ratio*self.color[1]),
            ceil(rgb_scale_ratio*self.color[2])
        )

        print("Found color of image " + self.path + ": " + str(self.color))

    def generate_categorized_image(self):
        printColoured("Generating categorized version of: " + self.path, "white", "on_blue")

        # Generate ImageDraw
        working_image = Image.new("RGB", crop_resolution)
        working_image_draw = ImageDraw.Draw(working_image)

        # Rectangle background
        hex_code = '#%02X%02X%02X' % self.color
        working_image_draw.rectangle([(0,0), crop_resolution], fill=hex_code)

        # Resize original image
        from math import ceil
        resize_resolution = (crop_resolution[0] - edge_thickness, crop_resolution[1] - edge_thickness) # 80 minus 1920x1200
        resize_ratio = max(resize_resolution[0]/self.source_image.width, resize_resolution[1]/self.source_image.height)
        resize_resolution = [ceil(self.source_image.width*resize_ratio), ceil(self.source_image.height*resize_ratio)]
        self.source_image = self.source_image.resize(resize_resolution)

        # Overlay original image
        working_image.paste(self.source_image, (edge_thickness, edge_thickness))

        self.final_image = working_image
        print("Categorized version of " + self.path + " generated!")

    def save_image(self):
        printColoured("Saving image: " + self.path, "white", "on_green")
        self.final_image.save(outputdirectory + self.name)
        print(self.path + " saved!")


### CORE PROGRAM ###
def main():
    # Info text blah blah
    print_info_text()
    
    # Load images
    print()
    images = import_images()

    # Start images processing...
    print()
    printColoured("Begin image processing...", "cyan")
    multiprocess_start(images)

    # Once all processes finish, program is finished!
    print()
    printColoured("All processes FINISHED! Exiting...", "green")



### CORE SUBROUTINES ###

# Import wallpapers from source-images
def import_images():

    supported_formats = [".bmp", ".ico", ".jpeg", ".jpg", ".jfif", ".png", ".tiff", ".webp"]

    # Figure out what files are images
    printColoured("Importing image files from " + sourcedirectory, "blue")
    foldercontents = os.listdir(sourcedirectory)

    if len(foldercontents) == 0:
        printColoured("Please put photos in " + sourcedirectory + " !", "red")
        exit()

    # Make a list of those paths
    images = []
    for item in foldercontents:
        for filetype in supported_formats:
            if filetype in item:
                images.append(categoryImage(path = sourcedirectory + item, name = item))
                break

    return images


# Handle multiprocessing of images
def multiprocess_start(images):
    tasks = []

    # Start getting colours for images
    for image in images:
        ### IMPORTS ###
        p = multiprocessing.Process(target=image.process)
        tasks.append(p)
        p.start()

    # Join jobs -- execution will wait for all colours to be grabbed
    for job in tasks:
        job.join()

    return images


### THE OTHER THING ###
if __name__ == "__main__":
    main()