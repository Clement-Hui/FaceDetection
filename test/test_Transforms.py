import unittest
from unittest import TestCase

from utils import WIDERFaceDataset
from utils.constants import *
from utils.transform import Rescale
from utils.utils import get_transform


class TestTransforms(TestCase):
    def test_rescale(self):
        dataset = WIDERFaceDataset(unittest_images_directory, unittest_label_directory, Rescale(512))
        print(dataset[0])
        self.assertTrue(dataset[0]['bbox'][0] == 449 / 2)
        self.assertTrue(dataset[0]['features'][0] == 0)

    def test_totensor(self):
        dataset = WIDERFaceDataset(train_images_directory, train_label_directory, get_transform())
        self.assertTrue(dataset[0]['images'].shape[0] == 512)
        self.assertTrue(dataset[0]['images'].shape[2] == 3)


if __name__ == '__main__':
    unittest.main()
