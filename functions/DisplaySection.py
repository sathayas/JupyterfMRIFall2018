import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt

def show_plane(x):
    '''
    Function to show a slice (provided as a 2D array)
    '''
    plt.imshow(x, cmap="gray")
    plt.gca().set_axis_off()


def show_section(xImg, section, xSlice):
    '''
    Function to return a 2D array of a slice from a 3D array.
    Slice orientation can be specified by the user.
    '''
    if section=='xy':
        tmpImg = xImg[:,:,xSlice]
    elif section=='xz':
        tmpImg = xImg[:,xSlice,:]
    else:
        tmpImg = xImg[xSlice,:,:]
    show_plane(np.rot90(tmpImg))

def load_nii_data(f_nii):
    '''
    Functio to load an NIfTI image and returns the data matrix
    as an array.
    '''
    nii = nib.load(f_nii)
    X = nii.get_data()
    return X
