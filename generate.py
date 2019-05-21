import argparse
import subprocess

def createImage(image, name, x, y):
     # magick convert -resize 29x29^ -gravity center -extent 29x29 wasp.jpg Icon-Small.png
     print(name)
     extent = str(x) + 'x' + str(y)
     resize = extent + '^'
     
     subprocess.run(["magick", "convert", "-resize", resize, "-gravity", "center", "-extent", extent, image, name])

parser = argparse.ArgumentParser(description='Generate iOS icons using imagemagick')
parser.add_argument('image')
args = parser.parse_args()

# create appicon directory
subprocess.run(["mkdir", "AppIcon.appiconset"])

# copy metadata json, this is hard coded to match the generated image filenames
subprocess.run(["cp", "Contents.json", "AppIcon.appiconset/Contents.json"])

# create a square image
squareImage = 'AppIcon.appiconset/ios-marketing.png'
createImage(args.image, squareImage, 1024, 1024)

# create all the other images
createImage(squareImage, 'AppIcon.appiconset/iphone-20@2x.png', 40, 40)
createImage(squareImage, 'AppIcon.appiconset/iphone-20@3x.png', 60, 60)
createImage(squareImage, 'AppIcon.appiconset/iphone-29@2x.png', 58, 58)
createImage(squareImage, 'AppIcon.appiconset/iphone-29@3x.png', 87, 87)
createImage(squareImage, 'AppIcon.appiconset/iphone-40@2x.png', 80, 80)
createImage(squareImage, 'AppIcon.appiconset/iphone-40@3x.png', 120, 120)
createImage(squareImage, 'AppIcon.appiconset/iphone-60@2x.png', 120, 120)
createImage(squareImage, 'AppIcon.appiconset/iphone-60@3x.png', 180, 180)
createImage(squareImage, 'AppIcon.appiconset/ipad-20.png', 20, 20)
createImage(squareImage, 'AppIcon.appiconset/ipad-20@2x.png', 40, 40)
createImage(squareImage, 'AppIcon.appiconset/ipad-29.png', 29, 29)
createImage(squareImage, 'AppIcon.appiconset/ipad-29@2x.png', 58, 58)
createImage(squareImage, 'AppIcon.appiconset/ipad-40.png', 40, 40)
createImage(squareImage, 'AppIcon.appiconset/ipad-40@2x.png', 80, 80)
createImage(squareImage, 'AppIcon.appiconset/ipad-76.png', 76, 76)
createImage(squareImage, 'AppIcon.appiconset/ipad-76@2x.png', 152, 152)
createImage(squareImage, 'AppIcon.appiconset/ipad-83.5@2x.png', 167, 167)
