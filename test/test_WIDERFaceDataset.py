import unittest
from unittest import TestCase

from utils import WIDERFaceDataset


class TestWIDERFaceDataset(TestCase):

    def test_init_getitem_len(self):
        dataset = WIDERFaceDataset("K:\\WIDER_train\\train\\images\\", "K:\\wider_face_split\\train_bbox.txt", None)
        print(len(dataset))
        self.assertTrue(len(dataset) == 12880)
        dataset[0][0].show()


if __name__ == '__main__':
    unittest.main()
