import unittest
from unittest import TestCase

from utils import WIDERFaceDataset
from utils.constants import *


class TestWIDERFaceDataset(TestCase):

    def test_init_getitem_len(self):
        dataset = WIDERFaceDataset(unittest_images_directory, unittest_label_directory, None)
        print(len(dataset))
        self.assertTrue(len(dataset) == 5)
        self.assertTrue(dataset[0]['image'].shape[2] == 3)
        self.assertTrue(dataset[0]['image'].shape[1] == 1024)



if __name__ == '__main__':
    unittest.main()
