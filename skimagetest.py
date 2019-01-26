import numpy as np
#import matplotlib
#matplotlib.use('MacOSX')
#import matplotlib.pyplot as plt
from PIL import Image
from skimage import data, img_as_float, img_as_ubyte
from skimage.segmentation import (morphological_chan_vese, morphological_geodesic_active_contour, inverse_gaussian_gradient, checkerboard_level_set)
#print(plt.get_backend())


def store_evolution_in(lst):
    """Returns a callback function to store the evolution of the level sets in
    the given list.
    """

    def _store(x):
        lst.append(np.copy(x))

    return _store


imarray = np.asarray(Image.open("./images/bottle.jpg"))

# Morphological ACWE
image = img_as_float(imarray)
print(image)
intimage = img_as_ubyte(image)
Image.fromarray(intimage).save('./results/t1.jpg', 'JPEG')
# Initial level set
init_ls = checkerboard_level_set(image.shape, 6)
# List with intermediate results for plotting the evolution
evolution = []
callback = store_evolution_in(evolution)

gimage = inverse_gaussian_gradient(image)
print("-------STARTING--------")
ls = morphological_geodesic_active_contour(gimage, 100, init_ls,
                                           smoothing=1, balloon=-1,
                                           threshold=0.69,
                                           iter_callback=callback)
print("-------  DONE  --------")
print(ls)
intls = img_as_ubyte(ls)
Image.fromarray(intls).save('./results/ls.jpg', 'JPEG')
print("evolution array\n" + evolution)

#fig, axes = plt.subplots(2, 2, figsize=(8, 8))
#ax = axes.flatten()
#
#ax[0].imshow(image, cmap="gray")
#ax[0].set_axis_off()
#ax[0].contour(ls, [0.5], colors='r')
#ax[0].set_title("Morphological ACWE segmentation", fontsize=12)
#
#ax[1].imshow(ls, cmap="gray")
#ax[1].set_axis_off()
#contour = ax[1].contour(evolution[2], [0.5], colors='g')
#contour.collections[0].set_label("Iteration 2")
#contour = ax[1].contour(evolution[7], [0.5], colors='y')
#contour.collections[0].set_label("Iteration 7")
#contour = ax[1].contour(evolution[-1], [0.5], colors='r')
#contour.collections[0].set_label("Iteration 35")
#ax[1].legend(loc="upper right")
#title = "Morphological ACWE evolution"
#ax[1].set_title(title, fontsize=12)
#fig.tight_layout()
