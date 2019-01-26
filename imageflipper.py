from PIL import Image
import glob, os
import numpy as np
counter = 0
for infile in glob.glob('./images/*'):
    print(infile)
    image = Image.open(infile)
    counter = counter + 1
    flip_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    flip_image.save('./flipped-images/flipped' + str(counter) + '.jpg')
