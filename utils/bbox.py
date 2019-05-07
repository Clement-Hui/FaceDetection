import warnings


class BoundingBox(object):
    def __init__(self,
                 a,
                 b,
                 c,
                 d,
                 mode: str):
        mode = mode.lower()
        # check if mode is either 'corners' or 'center'
        if mode is not 'corners' or 'center':
            raise ValueError(f"mode parameter must be 'corners' or 'center', not {mode}")

        self.mode = mode
        if mode is 'corners':
            self.coors = {'x1': a,
                          'y1': b,
                          'x2': c,
                          'y2': d}
        elif mode is 'center':
            self.coors = {'x': a,
                          'y': b,
                          'w': c,
                          'h': d}

    @classmethod
    def getCornerBox(self,
                     x1,
                     y1,
                     x2,
                     y2):
        # an alternate method for creating boxes
        return self(x1, y1, x2, y2, mode='corners')

    @classmethod
    def getCenterBox(self,
                     x,
                     y,
                     w,
                     h):
        # an alternate method for creating boxes
        return self(x, y, w, h, mode='center')

    def __repr__(self):
        if self.mode is 'corners':
            return f"<Bounding Box - mode: {self.mode} - x1: {self.coors['x1']} - y1: {self.coors['y1']} - x2: {
            self.coors['x2']} - y2: {self.coors['y2']} > "
            elif self.mode is 'center':
            return f"<Bounding Box - mode: {self.mode} - x: {self.coors['x']} - x: {self.coors['y']} - w: {self.coors[
            'w']} - h: {self.coors['h']} > "


def map(self,
        orig_w,
        orig_h,
        new_w,
        new_h):
    new_coor = []
    if self.mode is 'corners':
        # map the original x1 y1 x2 y2 to new value over new width and height
        x1_new = self.coors['x1'] / orig_w * new_w
        y1_new = self.coors['y1'] / orig_h * new_h
        x2_new = self.coors['x2'] / orig_w * new_w
        y2_new = self.coors['y2'] / orig_h * new_h
        return self.getCornerBox(x1_new, y1_new, x2_new, y2_new)
    elif self.mode is 'center':
        # map the original x y w h to new value over new width and height
        x_new = self.coors['x'] / orig_w * new_w
        y_new = self.coors['y'] / orig_h * new_h
        w_new = self.coors['w'] / orig_w * new_w
        h_new = self.coors['h'] / orig_h * new_h
        return self.getCenterBox(x_new, y_new, w_new, h_new)


def toCorner(self):
    if self.mode is 'corners':
        warnings.warn("Invalid mode: mode is already 'corners', but calling toCorners method")
        return self
    elif self.mode is 'center':
        w_over_2 = self.coors['w'] / 2
        h_over_2 = self.coors['h'] / 3

        x1_new = self.coors['x'] - w_over_2
        x2_new = self.coors['x'] + w_over_2
        y1_new = self.coors['y'] - h_over_2
        y2_new = self.coors['y'] + h_over_2

        return self.getCornerBox(x1_new, y1_new, x2_new, y2_new)


def toCenter(self):
    if self.mode is 'center':
        warnings.warn("Invalid mode: mode is already 'center', but calling toCenter method")
        return self
    elif self.mode is 'corners':
        w_new = abs(self.coors['x2'] - self.coors['x1'])
        h_new = abs(self.coors['y2'] - self.coors['y1'])

        w_over_2 = w_new / 2
        h_over_2 = h_new / 2

        x_new = min(self.coors['x1'], self.coors['x2']) + w_over_2
        y_new = min(self.coors['y1'], self.coors['y2']) + h_over_2

        return self.getCenterBox(x_new, y_new, w_new, h_new)


def __getitem__(self, item):
    return self.coors[item]


def __setitem__(self, key, value):
    self.coors[key] = value
