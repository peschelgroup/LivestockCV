# Gaussian blur device

import cv2
import os
import numpy as np
from LivestockCV.core import print_image
from LivestockCV.core import plot_image
from LivestockCV.core import params


def gaussian_blur(img, ksize, sigma_x=0, sigma_y=None):
    """Applies a Gaussian blur filter.

    Inputs:
    # img     = RGB or grayscale image data
    # ksize   = Tuple of kernel dimensions, e.g. (5, 5)
    # sigmax  = standard deviation in X direction; if 0, calculated from kernel size
    # sigmay  = standard deviation in Y direction; if sigmaY is None, sigmaY is taken to equal sigmaX

    Returns:
    img_gblur = blurred image

    :param img: numpy.ndarray
    :param ksize: tuple
    :param sigma_x: int
    :param sigma_y: str or int
    :return img_gblur: numpy.ndarray
    """

    img_gblur = cv2.GaussianBlur(img, ksize, sigma_x, sigma_y)

    params.device += 1
    if params.debug == 'print':
        print_image(img_gblur, os.path.join(params.debug_outdir, str(params.device) + '_gaussian_blur.png'))
    elif params.debug == 'plot':
        if len(np.shape(img_gblur)) == 3:
            plot_image(img_gblur)
        else:
            plot_image(img_gblur, cmap='gray')

    return img_gblur
