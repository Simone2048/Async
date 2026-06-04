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
    canvas = display.Canvas(oled,5)
    playing_pong=False
    while True:
        up, down, left, right, action = read_btns()
        
        if action:
            canvas.text("Starting Pong",0,10)
            playing_pong=True
            
        if playing_pong:
            pong.run(canvas,read_btns())
            time.sleep_ms(2)
        else:
            canvas.text("Press Action To Play Pong",0,10)
            canvas.show()
            time.sleep_ms(50)
        """ 
        #Test Code(Remove When Shipped)
        array = canvas.import_bit_map('sprites/test_bitmap.json')
        canvas.clear()
        if action:
            canvas.text("Action Pressed!!! ", 0, 0)
            canvas.draw_bit_map(array,0,20)
        canvas.show()
        """


if __name__ == "__main__":
    main()
