import json
import argparse
import subprocess

def createImage(image, name, x, y):
     # magick convert -resize 29x29^ -gravity center -extent 29x29 wasp.jpg Icon-Small.png
     print(name)
     extent = str(x) + "x" + str(y)
     resize = extent + "^"
     subprocess.run(["convert", "-resize", resize, "-gravity", "center", "-extent", extent, image, name])

configPath = "configs/"
outputPath = "output/"

parser = argparse.ArgumentParser(description='Generate placeholder images using imagemagick')
parser.add_argument("config")
parser.add_argument("image")
args = parser.parse_args()

# read config
file = open(configPath + args.config + ".json",)
data = json.load(file)
file.close()

# create a square image
squareImage = outputPath + "1024x1024.png"
createImage(args.image, squareImage, 1024, 1024)

# create all the other images
for image in data['images']:
     name = outputPath + image["x"] + "x" + image["y"] + ".png"
     createImage(squareImage, name, image["x"], image["y"])

