import os

from PIL import Image
from torch.utils.data import Dataset


class WIDERFaceDataset(Dataset):
    def __init__(self,
                 data_dir,
                 label_dir,
                 transform):
        super(WIDERFaceDataset, self).__init__()
        self.transform = transform

        self.data_dir = data_dir
        self.label_dir = label_dir

        # 3d array of bbox
        self.labels = []
        # 1d array of image paths
        self.path = []
        # 1d array of #of bbox
        self.num_bbox = []
        # temp array to store 2d array of labels
        current_bbox_arr = None
        with open(label_dir, 'r') as f:
            for line in f:
                # remove "\n"
                stripped_line = line.replace("\n", '')
                # replaces / to \ and remove \n
                path_line = stripped_line.replace("/", "\\")
                # join data_dir and img relative path
                path = os.path.join(self.data_dir, path_line)
                # check if dataline is path
                file_exists = True
                try:
                    f = open(path, 'r')
                    f.close()

                except FileNotFoundError:
                    file_exists = False

                if file_exists:
                    self.path.append(path)

                # check if line is int
                elif stripped_line.isdigit():
                    self.num_bbox.append(int(line))
                    if current_bbox_arr is not None:
                        self.labels.append(current_bbox_arr)

                    current_bbox_arr = []
                else:

                    bbox = [x for x in line.split()]
                    current_bbox_arr.append(bbox)

        self.labels.append(current_bbox_arr)

    def __len__(self):
        return len(self.path)

    def __getitem__(self, idx):
        # load image from path
        img = Image.open(self.path[idx])
        # transform image
        if self.transform is not None:
            img = self.transform(img)

        # return tuple of image and label
        return (img, self.labels[idx])
