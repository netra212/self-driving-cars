import random
import numpy as np
import cv2
import os

xs = []
ys = []

# points to the end of the last batch. 
train_batch_pointer = 0
val_batch_pointer = 0

# read data.txt
data_path = "/Users/netrakc/Desktop/self-driving-cars/data/driving_dataset"
data_dir = os.listdir(os.path.join(data_path, "data.txt"))
with open("data_dir") as f:
    for line in f:
        xs.append("data/driving_dataset")

