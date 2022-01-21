# References: https://github.com/opencv/opencv/blob/master/samples/python/kmeans.py, https://code.likeagirl.io/finding-dominant-colour-on-an-image-b4e075f98097

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def find_histogram(clt):
    """
    create a histogram with k clusters
    :param: clt
    :return:hist
    """
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)
    hist = hist.astype("float")
    hist /= hist.sum()
    return hist

def plot_colors(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0
    for (percent, color) in zip(hist, centroids):
        		# plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX
   		# return the bar chart
    return bar

cap = cv.VideoCapture(0)
clt = KMeans(n_clusters=3) #cluster number
plt.show()


while(1):
 		#Take each frame
	_, frame = cap.read()
    	#Draw and crop a fixed rectangle n the center of the image
	cv.rectangle(frame,(400,150),(800,550),(0,0,255),2)
	crop = frame[400:800, 150:550] 
		#Use Kmeans to find the dominant color 
	img = crop.reshape((crop.shape[0] * crop.shape[1],3))
	clt.fit(img)
	hist = find_histogram(clt)
	bar = plot_colors(hist, clt.cluster_centers_)
  		#Graph the histogram 
	plt.clf()
	plt.axis("off")
	plt.imshow(bar)
	plt.pause(1)
	cv.imshow('frame',frame)
	k = cv.waitKey(5) & 0xFF
	if k == 27:
		break