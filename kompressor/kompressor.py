import os
from time import time
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin
from sklearn.datasets import load_sample_image
from sklearn.utils import shuffle
from time import time
from PIL import Image
import numpy as np


def recreate_image(codebook, labels, w, h):
    """Recreate the (compressed) image from the code book & labels"""
    d = codebook.shape[1]
    image = np.zeros((w, h, d))
    label_idx = 0
    for i in range(w):
        for j in range(h):
            image[i][j] = codebook[labels[label_idx]]
            label_idx += 1
    return image


def compress_image(path, n_colors = 512):
    """compress image by replacing the colors to the cluster center color"""

    #TODO: exit  gracefully
    img = np.asarray(Image.open(path), dtype=np.float64)/255

    # reshape, 1 color is represented by 3 values, RGB
    w, h, d = img.shape
    image_array = np.reshape(img, (w*h, d))

    #TODO: Train set is can be tuned
    train_len = 2 * n_colors
    if n_colors < 512:
        train_len = 1000
    
    t0 = time()
    print(f"[LOG]: Fitting model on a small sub-sample of the data")
    image_array_sample = shuffle(image_array, random_state=0)[:n_colors]
    kmeans = KMeans(n_clusters= n_colors, random_state=0).fit(image_array_sample)
    print(f"[LOG]: done in {time()-t0:.3f}s.")

    # Get labels for all points
    # TODO: Add progress bar for predicting the labels
    print(f"[LOG]: Predicting color indices on the full image (k-means)")
    t0 = time()
    labels = kmeans.predict(image_array)
    print(f"[LOG]: done in {time()-t0:.3f}s.")


    print(f"[LOG]: Creating new image.")
    t0 = time()
    # This result is between 0-1
    compressed = recreate_image(kmeans.cluster_centers_, labels, w, h)
    # convert range between 0- 255
    compressed = np.array(compressed * 255, 'uint8')
    compressed_img = Image.fromarray(compressed, 'RGB')
    filename, ext = os.path.split(path)[-1].split('.')
    compressed_img.save(f'{filename}_compressed_{n_colors}c.{ext}')
    print(f"[LOG]: done in {time()-t0:.3f}s.")


def no_of_unique_colors(path):
    """count the no. of colors used in the image"""

    #TODO: exit gracefully if can't read the image
    im = np.asarray(Image.open(path))

    print(f"[LOG]: Counting the no. of unique colors")
    t0 = time()
    colors = set()
    w, h, _ = im.shape
    print(f"Dimension {w}x{h}")
    for i in range(w):
        for j in range(h):
            colors.add(tuple(im[i][j]))

    print(f"No of unique colors : {len(colors)}")
    print(f"[LOG]: done in {time()-t0:.3f}s.")
