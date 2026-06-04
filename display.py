import time
import json

class Canvas:
    def __init__(self, display, spriteSize):
        self.d = display
        self.spriteSize = spriteSize

    def clear(self):
        self.d.fill(0)

    def show(self):
        self.d.show()

    def rect(self, x, y, w, h, fill=False):
        if fill:
            self.d.fill_rect(x, y, w, h, 1)
        else:
            self.d.rect(x, y, w, h, 1)

    def text(self, s, x, y, c=1):
        self.d.text(s, x, y, c)

    def hline(self, x, y, w):
        self.d.hline(x, y, w, 1)

    def vline(self, x, y, h):
        self.d.vline(x, y, h, 1)

    def pixel(self, x, y, t):
        self.d.pixel(x, y, t)
    def import_bit_map(self,file):
        with open(file, 'r') as file:
            loaded_array = json.load(file)
        print(loaded_array)
        return loaded_array
    def draw_bit_map(self,array,StartX,StartY):
        for x in range(self.spriteSize):
            for y in range(self.spriteSize):
                self.pixel(StartX+x,StartY+y,array[x][y])
