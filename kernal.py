import numpy as np
import scipy
from scipy import misc
import matplotlib.pyplot as plt
from PIL import Image

image = np.asarray(Image.open('./images/raw/image.jpg').convert('L'))

def convolude(image, kernal):
    if len(image)>1024 or len(image[0])>512:
        image = resize(image)

    (dim_x, dim_y) = np.shape(image)
    newImage= np.zeros(image.shape) #the new image. the same size as the image I will filter
    for i in range(1,dim_x-1): #the range starts from 1 to avoid the column and row of zeros, and ends before the last col and row of zeros
        for j in range(1,dim_y-1):
            newImage.setflags(write=1)
            imageEntry= image[i-1:i+2, j-1:j+2]
          #  print("image entry: " + str(imageEntry))
          #  print("kernal: " + str(kernal))
            if len(imageEntry) == 3 and len(imageEntry[0]) == 3:
                valor = np.sum(imageEntry*kernal)    #Matrix 3x3 is filled with the elements around each [i, j] entry of the array
                newImage[i, j] = valor

        newImage = threshold(newImage, 128)
    return newImage

def rowSum(image):
    (dim_x, dim_y) = np.shape(image)
    print(dim_x, dim_y)
    kernal = [[1] * dim_y, [2] * dim_y, [1] * dim_y] # for some reason y is the x dim
    sumVector= np.zeros(dim_y) #the new image. the same size as the image I will filter

    for i in range(1,dim_y-1): #the range starts from 1 to avoid the column and row of zeros, and ends before the last col and row of zeros
        sumVector.setflags(write=1)
        imageEntry= image[i-1:i+2, 0:dim_x]

        valor = np.sum(imageEntry*kernal)    #Matrix 3x3 is filled with the elements around each [i, j] entry of the array
        sumVector[i] = valor

    return sumVector

def resize(image): #returns an image in the same aspect ratio with a maximum height of 1024 and width of 512
    size = 300, 400
    im = Image.fromarray(image).resize(size)
    im.save('resized.jpg')
    return np.asarray(im)

def threshold(image, thresh):
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] > thresh:
                image[i][j] = 255
            else:
                image[i][j] = 0
    return image

def rankRows(vector, n):
    max = [-1] * n
    for i in range(len(vector)):
        added = False
        j = 0
        while not added and j < n:
            if vector[max[j]] < vector[i]:
                added = True
                max[j] = i
            j += 1
    return max


ker1 = np.array([[-1, -2, -1],   #3x3 kernel
[0, 0, 0],
[1,2,1]])

#newImage= convolude(image, ker1)
testim= np.asarray(Image.open('./test.jpg').convert('L'))

rows = rowSum(testim)
rows = rankRows(rows, 5)

newtest = testim.copy()
newtest.setflags(write=1)
for i in rows:
    for pix in range(len(newtest[i])):
        newtest[i][pix] = 255
Image.fromarray(newtest).save('newtest.jpg')

print(rows)
#im = Image.fromarray(newImage).convert('L')
#im.save('./test.jpg')


#plt.imshow(imagen_nueva)  #Show new image
#plt.gray()
#plt.show()
