from torchvision import transforms

from utils.constants import *
from utils.transform import *


def get_transform():
    transform = transforms.Compose([
        Rescale(input_img_size),
        ToTensor()

    ])
    return transform
