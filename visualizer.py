import matplotlib.pyplot as plt
import matplotlib.image as img
from skimage import io
import os
import numpy as np
import time

tic = time.perf_counter()

def create_images(path):
    slices = [(path + '/' + s) for s in os.listdir(path)]
    return slices

MapsDir = os.listdir('Data/')
histoImages = create_images('Data/' + MapsDir[-1]) # create list of HE images
groundTruths = []  # create list of list of maps
for h in range(len(MapsDir)-1):
    groundTruths.append(create_images('Data/' + MapsDir[h]))

for i in range(len(histoImages)):
    ###################
    imageNumber = i
    ###################
    
    imageName = histoImages[imageNumber]
    imageIndex = imageName.replace('.jpg', '').replace('Data/' + MapsDir[-1] + '/', '')
    # print(imageIndex)
    
    #verify how many truthmap are present for the selected image
    
    truthMaps = []
    truthMapsList = []
    for j in range(len(MapsDir)-1):
        for k in range(len(groundTruths[j])):
            if imageIndex in groundTruths[j][k]:
                truthMaps.append(groundTruths[j][k])
                truthMapsList.append(j+1)
                break
    # print("Number of truthMaps: " + str(len(truthMaps)) + " from experts " + str(truthMapsList))
    
    # make the figure
    plt.figure()
    plt.figure(figsize=[14,14])
    ima = io.imread(imageName)
    plt.subplot(3,3,1)
    io.imshow(ima)
    for l in range(len(truthMaps)):
        im = io.imread(truthMaps[l])
        plt.subplot(3,3,l+2)
        io.imshow(im, vmin=0, vmax=6) #les limites sont 0=> benign, 6 grade 5

    # if not os.path.exists('Figures'):
    #     os.makedirs('Figures')
    plt.savefig(str('Figures/'+str(imageIndex)+'.png'))
    plt.close()
    
toc = time.perf_counter()
print('toc-tic: ' + str(toc-tic))
print('process time: '+ str(time.process_time()))
# im = io.imread(truthMaps[0])
# print("Present grades:" + str(set(im.flatten())))

