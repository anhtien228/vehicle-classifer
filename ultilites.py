import numpy as np
import h5py

####################################################

def print_data_shape(train_images, train_labels, test_images, test_labels):
    print("Train shape:", train_images.shape)
    print("Train labels shape:", train_labels.shape)
    print("Test shape:", test_images.shape)
    print("Test label shape:", test_labels.shape)

####################################################
# Plotting function 