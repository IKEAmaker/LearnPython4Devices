import board
import busio
import digitalio
from analogio import AnalogIn


class Joystick:
    def __init__(self, board):
        if type == 'i2c':
            self.button = digitalio.DigitalInOut(board.A0)
            self.upDown = AnalogIn(board.A3)
            self.rightLeft = AnalogIn(board.A4)
        elif type == 'spi':
            self.button = digitalio.DigitalInOut(board.A3)
            self.upDown = AnalogIn(board.A4)
            self.rightLeft = AnalogIn(board.A5)
            
        self.up_dir = 1
        self.right_dir = 1
        self.button.direction = digitalio.Direction.INPUT
        self.button.pull = digitalio.Pull.UP
        
        up_sum = 0.0
        right_sum = 0.0

        for i in range (0, 1000, 1):
            up_sum += ((self.upDown.value / 65356)-0.5)
            right_sum += ((self.rightLeft.value / 65536)-0.5)

        self.up_cal = up_sum/1000
        self.right_cal = right_sum/1000        
    
    def read_Up(self):
        return (((self.upDown.value/65536) - 0.5) - self.up_cal) * self.up_dir

    def read_Right(self):
            return (((self.rightLeft.value/65536) - 0.5) - self.right_cal) * self.right_dir
            
    def read_button(self):
        return not self.button.value

    up =  property(read_Up)
    
    right = property(read_Right)
    
    push = property(read_button)

class Matrix:
    def __init__(self, type):
        self.type = type
        _matrix.fill(0)
        _matrix.show()

    def fill(self, color):
        _matrix.fill(color)
        
    def show(self):
        _matrix.show()

    def pixel(self, x, y, color):
        _matrix.pixel(x, y, color)
        
    def __setitem__ (self, coords, color):
        self.pixel(coords[0], coords[1], color)
        
    def text(self, str, x, y, color):
        if self.type == 'i2c':
            font.text(str, x, y, color)
        elif self.type =='spi':
            _matrix.text(str, x, y, color)

try:
    i2c = busio.I2C(board.SCL, board.SDA)
    from adafruit_ht16k33.matrix import Matrix8x8
    import bitmapfont
    _matrix = Matrix8x8(i2c, auto_write=False)
    font = bitmapfont.BitmapFont(8, 8, _matrix.pixel)
    font.init()
    type = 'i2c'
except:
    from adafruit_max7219.matrices import Matrix8x8
    cs = digitalio.DigitalInOut(board.D2)
    spi = busio.SPI(board.SCK, MOSI=board.MOSI, )
    _matrix = Matrix8x8(spi, cs)
    _matrix.brightness(9)
    type = 'spi'

matrix = Matrix(type)
joystick = Joystick(board)