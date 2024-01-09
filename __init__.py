import os
import torch

print('torch version----------------------', torch.__version__)
import subprocess
import sys


def install_package(package_name):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])


package_list = ["imageio", "cupy", "imageio_ffmpeg", 'cv2']  # Replace with your list of packages
install_name = ['imageio', '', 'imageio[ffmpeg]', 'opencv-python-headless']

for package,name in zip(package_list,install_name):
    try:
        __import__(package)
    except ImportError:
        if package == "cupy":
            cuda_version = int(round(float(torch.version.cuda)*10))
            if cuda_version <= 102:
                name = "cupy-cuda102"
            elif cuda_version <= 110:
                name = "cupy-cuda110"
            elif cuda_version <= 111:
                name = "cupy-cuda111"
            elif cuda_version <= 118:
                name = "cupy-cuda11x"
            else:
                name = "cupy-cuda12x" 
        install_package(name)

from .masknumcap import MaskListcaptoBatch
from .myopenpose import MyOpenPoseNode
from .filldarkmask import FillDarkMask
from .interpolatekeyframe import InterpolateKeyFrame
from .smoothVideo import SmoothVideo
from .rebatchimage import reBatchImage

NODE_CLASS_MAPPINGS = {
    "MaskListcaptoBatch": MaskListcaptoBatch,
    "MyOpenPoseNode": MyOpenPoseNode,
    "FillDarkMask": FillDarkMask,
    "InterpolateKeyFrame": InterpolateKeyFrame,
    "SmoothVideo": SmoothVideo,
    "reBatchImage": reBatchImage,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "MaskListcaptoBatch": "Mask List cap toBatch",
    "MyOpenPoseNode": "My OpenPose Node",
    "FillDarkMask": "Fill Dark Mask",
    "InterpolateKeyFrame": "Interpolate KeyFrame",
    "SmoothVideo": "Smooth Video",
    "reBatchImage": "reBatch Image",
}
