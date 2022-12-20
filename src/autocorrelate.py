from scipy import signal
import numpy as np

def downsample(image, scale):
    return image[::scale, ::scale]


def autocorrelate(image):

    corr = signal.correlate2d(image, image, mode='full')
    return corr
