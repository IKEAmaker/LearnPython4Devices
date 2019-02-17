import busio
from adafruit_ht16k33 import matrix
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction, Pull
import bitmapfont

class joystick:
    def __init__(self, board):
        self.upDown = AnalogIn(board.A3)
        self.rightLeft = AnalogIn(board.A4)
        self.button = DigitalInOut(board.A0)
        self.button.direction = Direction.INPUT
        self.button.pull = Pull.UP
        
        self.up_cal = 0
        self.up_dir = 1
        self.right_cal = 0
        self.right_dir = 1
        
    
    def read_Up(self):
        return (((self.upDown.value/65536) - 0.5) * self.up_dir) - self.up_cal

    def read_Right(self):
            return (((self.rightLeft.value/65536) - 0.5) * self.right_dir) - self.right_cal
            
    def read_button(self):
        return not self.button.value

    up =  property(read_Up)
    
    right = property(read_Right)
    
    push = property(read_button)

class kit:
        
    def __init__ (self, board):
        i2c = busio.I2C(board.SCL, board.SDA)
        self.matrix = matrix.Matrix8x8(i2c, auto_write=False)
        self.matrix.fill(0)
        self.matrix.show()
                
        self.font = bitmapfont.BitmapFont(8, 8, self.matrix.pixel)
        self.font.init()
        
        self.joystick = joystick(board)
        
        