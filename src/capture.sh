#!/bin/bash

gphoto2 --auto-detect
gphoto2 --set-config-value /main/capturesettings/shutterspeed=1/4000
gphoto2 --capture-image-and-download --filename ../imgs/"$1".%C