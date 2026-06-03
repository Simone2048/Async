import time


class Canvas:
    def __init__(self, display):
        self.d = display

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

    def pixel(self, x, y):
        self.d.pixel(x, y, 1)
