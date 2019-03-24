import busio
from adafruit_ht16k33 import matrix
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction, Pull
import bitmapfont
import board

class Joystick:
    def __init__(self, board):
        self.upDown = AnalogIn(board.A3)
        self.rightLeft = AnalogIn(board.A4)
        self.button = DigitalInOut(board.A0)
        self.button.direction = Direction.INPUT
        self.button.pull = Pull.UP
        
        up_sum = 0.0
        right_sum = 0.0

        for i in range (0, 1000, 1):
            up_sum += ((self.upDown.value / 65356)-0.5)
            right_sum += ((self.rightLeft.value / 65536)-0.5)

        self.up_cal = up_sum/1000
        self.right_cal = right_sum/1000

        self.up_dir = 1
        self.right_dir = 1
        
    
    def read_Up(self):
        return (((self.upDown.value/65536) - 0.5) - self.up_cal) * self.up_dir

    def read_Right(self):
            return (((self.rightLeft.value/65536) - 0.5) - self.right_cal) * self.right_dir
            
    def read_button(self):
        return not self.button.value

    up =  property(read_Up)
    
    right = property(read_Right)
    
    push = property(read_button)


i2c = busio.I2C(board.SCL, board.SDA)
matrix = matrix.Matrix8x8(i2c, auto_write=False)
matrix.fill(0)
matrix.show()
        
font = bitmapfont.BitmapFont(8, 8, matrix.pixel)
font.init()

joystick = Joystick(board)