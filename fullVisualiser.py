
# =============================================================================
# single visualiser
# =============================================================================
import matplotlib.pyplot as plt
import matplotlib.image as img
from skimage import io
import os
import numpy as np
import time
from dataPreproces import load_data


histoImages, masks = load_data()

###################
imageNumber = 131
###################
imageName = histoImages[imageNumber]
imageIndex = imageName.replace('.jpg', '').replace('Data/Train Imgs/', '')

#verify how many truthmap are present for the selected image

truthMaps = masks[imageNumber,:]

# make the figure
plt.figure()
plt.figure(figsize=[14,14])
ima = io.imread(imageName)
plt.subplot(3,3,2)
io.imshow(ima)
for i in range(len(truthMaps)):
    if truthMaps[i] != 'NoGT':
        im = io.imread(truthMaps[i])
        #print(im.shape, im.min(), im.max(), im.dtype)
        plt.subplot(3,3,i+4)
        plt.imshow(im,vmin = 0, vmax = 6) #les limites sont 0=> benign, 6 grade 5
        plt.colorbar()

# if not os.path.exists('Figures'):
#     os.makedirs('Figures')
plt.savefig(str('Figures/'+str(imageIndex)+'.png'))
# plt.close()

# plt.figure()
# im = io.imread(truthMaps[2])
# io.imshow(im, vmin=0, vmax=6) #les limites sont 0=> benign, 6 grade 5
# print("Present grades:" + str(set(im.flatten())))
