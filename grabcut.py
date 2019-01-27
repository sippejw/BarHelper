import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image
infile = './images/raw/IMG_20190125_220113.jpg'
img = cv2.imread(infile)
mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65), np.float64)
fgdModel = np.zeros ((1,65), np.float64)
print(img)

newmask = cv2.imread('./grabcut-im/newmask.jpg',0)

mask[newmask==0] = 0
mask[newmask==255] = 1

mask, bgdModel, fgdModel = cv2.grabCut(img,mask,None,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_MASK)
print(mask)

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

Image.fromarray(img).save('./grabcut-im/test.jpg')

