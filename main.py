from machine import Pin, SoftI2C
import time
from libraries.ssd1306 import SSD1306
import display
from games import snake, tetris, pong

I2C_SDA_PIN = 16
I2C_SCL_PIN = 17
OLED_WIDTH = 128
OLED_HEIGHT = 64
OLED_ADDR = 0x3C

BTN_UP = 18
BTN_DOWN = 19
BTN_LEFT = 21
BTN_RIGHT = 22
BTN_ACTION = 23

i2c = SoftI2C(sda=Pin(I2C_SDA_PIN), scl=Pin(I2C_SCL_PIN))
oled = SSD1306(OLED_WIDTH, OLED_HEIGHT, i2c, OLED_ADDR)

btn_up = Pin(BTN_UP, Pin.IN, Pin.PULL_DOWN)
btn_down = Pin(BTN_DOWN, Pin.IN, Pin.PULL_DOWN)
btn_left = Pin(BTN_LEFT, Pin.IN, Pin.PULL_DOWN)
btn_right = Pin(BTN_RIGHT, Pin.IN, Pin.PULL_DOWN)
btn_action = Pin(BTN_ACTION, Pin.IN, Pin.PULL_DOWN)


def read_btns():
    return (
        btn_up.value() == 1,
        btn_down.value() == 1,
        btn_left.value() == 1,
        btn_right.value() == 1,
        btn_action.value() == 1,
    )

def main():
    canvas = display.Canvas(oled)
    while True:
        up, down, left, right, action = read_btns()
        canvas.clear()
        if action:
            canvas.text("Action Pressed!!!" ,0,0)
        canvas.show()
        time.sleep_ms(50)


if __name__ == "__main__":
    main()
