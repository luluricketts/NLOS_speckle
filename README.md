# NLOS_speckle
15633 Final Project: Non Line of Sight Imaging with Laser Speckle Photography 

Author: Lulu Ricketts

## Install dependencies

```
pip install -r requirements.txt
```

## Capturing Images

You can use ```capture.sh``` to capture images when your camera is connected to your laptop using gphoto2. From ```src```, run:

```
./capture.sh {filename}
```

Filename is the name of the file with the extension omitted. The default shutter speed is set to 1/4000, which you can change within the file if needed.


## Autocorrelation and Reconstruction

Run ```main.py``` to compute the reconstruction of a speckle image (.jpg extension). You can also skip reconstruction and only compute and save the autocorrelation by toggling the ```--no-recon``` flag.

```
python3 main.py --img [filename] [--recon|--no-recon] --steps [int]
```

Here, steps is an integer specifying the number of iterations to perform phase retrieval for (default 300), and the filename is without the extension. 

By default, a directory with the same name as the file will be created, which is where all the results are stored, including the autocorrelation and reconstruction. If the ```--recon``` flag is specified, the phase retrieval algorithm will be run with 20 beta values spanning the range [0.1, 3], saving them all in the created directory.

## Results 

All my results are stored in the ```imgs``` directory, a video recording and the corresponding writeup are under the ```deliverables``` directory.


## References/Acknowledgements

For a full list of references, please refer to the references section of the report (in deliverables directory).

* Phase retrieval algorithm: https://github.com/tuelwer/phase-retrieval/blob/master/
* Acknowledgements: Ioannis Gkioulekas and Dorian Chan for their advisement on this project