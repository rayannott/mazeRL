import numpy as np
from matplotlib import pyplot as plt


class SimpleMaze:
    def __init__(self, image):
        self.image = image
        self.HEIGHT, self.WIDTH, _ = self.image.shape
        self.walls_mask = np.all(self.image == np.array(
            [[[1, 1, 1]]]), axis=2)
        self.blank_mask = np.all(self.image == np.array(
            [[[0, 0, 0]]]), axis=2)
        self.start = self.find_pixels(colour='red')
        self.exits = self.find_pixels(colour='green')
        self.make_field()

    def make_field(self):
        self.field = np.zeros(shape=(self.WIDTH, self.HEIGHT))
        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                self.field[x, y] = self.identify(pos=(x, y))
    rgb_values = {'red': [1, 0, 0],
                  'blue': [0, 0, 1],
                  'yellow': [1, 1, 0],
                  'green': [0, 1, 0]}

    def render(self, path=None):
        if path is None:
            plt.imshow(self.image)
        else:
            # path = path[1:-1]
            cmap = np.linspace([1,0,0], [0,1,0], len(path))
            self.image_solved = np.copy(self.image)
            for ind, point in enumerate(path):
                self.image_solved[point[0], point[1], :] = cmap[ind]
            plt.imshow(self.image_solved)

    def find_pixels(self, colour):
        coords = np.all(self.image == np.array(
            [[self.rgb_values[colour]]]), axis=2).nonzero()
        return set(zip(*coords))

    def identify(self, pos):
        x, y = pos
        if (x >= self.WIDTH or y >= self.HEIGHT or x < 0 or y < 0):
            return -1
        if self.blank_mask[x, y]:
            return 0
        elif self.walls_mask[x, y]:
            return 1
        elif pos in self.exits:
            return 3
        elif pos in self.start:
            return 2
        else:
            raise Exception('Unknown pixel identifier at', pos)
