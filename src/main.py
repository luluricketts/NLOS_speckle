import os
import argparse

import imageio
import numpy as np
import matplotlib.pyplot as plt

from autocorrelate import downsample, autocorrelate
from phase_retrieval import fienup_phase_retrieval


parser = argparse.ArgumentParser()
parser.add_argument('--img', type=str, help='image filename under ../imgs')
parser.add_argument('--steps', type=int, default=300, help='number of iterations to run for phase retrieval')
parser.add_argument('--recon', action=argparse.BooleanOptionalAction)
parser.set_defaults(recon=True)
if __name__ == "__main__":
    args = parser.parse_args()
    dir_path = f'../imgs/{args.img}'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    path = f'../imgs/{args.img}.jpg'
    image = imageio.imread(path, as_gray=True)
    image = downsample(image, 20)
    corr = autocorrelate(image)

    betas = np.linspace(0.01, 3, 20)
    results = []
    if args.recon:
        magnitudes = np.abs(np.fft.fft2(corr))
        for b in betas:
            r = fienup_phase_retrieval(magnitudes, steps=args.steps, beta=b, verbose=True)
            results.append(r)

    plt.subplot(131)
    plt.imshow(image, cmap='gray')
    plt.title('Image')
    plt.subplot(132)
    plt.imshow(corr, cmap='gray')
    plt.title('Autocorrelation')
    plt.show()

    imageio.imwrite(os.path.join(dir_path, f'{args.img}corr.jpg'), corr)
    if args.recon:
        for res in range(len(results)):
            imageio.imwrite(os.path.join(dir_path, f'{args.img}recon_beta{betas[res]}.jpg'), results[res])

