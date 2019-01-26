from PIL import Image
import glob, os
import numpy as np
counter = 0
for infile in glob.glob('./images/*/*'):
    print(infile)
    image = Image.open(infile)
    counter = counter + 1
    imarray = np.asarray(Image.open(infile))
    imarray.setflags(write=1)
    for row in imarray:
	print(row)
	for pixel in row:
            pixel[1], pixel[2] = pixel[2], pixel[1]
    imdifFace = Image.fromarray(imarray)
    imdifFace.save('./images/channel-swapped/chswapped' + str(counter) + '.jpg')

            
