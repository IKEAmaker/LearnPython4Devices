import busio
from adafruit_ht16k33 import matrix
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction, Pull
import bitmapfont

def setup_hardware(board):
    i2c = busio.I2C(board.SCL, board.SDA)
    led_matrix = matrix.Matrix8x8(i2c, auto_write=False)
    led_matrix.fill(0)
    led_matrix.show()
    
    upDown = AnalogIn(board.A3)
    leftRight = AnalogIn(board.A4)
    button = DigitalInOut(board.A0)
    button.direction = Direction.INPUT
    button.pull = Pull.UP
    
    font = bitmapfont.BitmapFont(8, 8, led_matrix.pixel)
    font.init()
    return led_matrix, upDown, leftRight, button, font