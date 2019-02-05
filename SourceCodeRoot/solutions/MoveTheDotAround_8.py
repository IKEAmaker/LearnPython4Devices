import board
import tinker_kit
import time

mx, UD, LR, push, bf = tinker_kit.setup_hardware(board)

x = 3.0
y = 3.0

while True:
    up = (UD.value/65536) - 0.5
    left = (LR.value/65536) - 0.5
    x = (x + left)%8
    y = (y + up)%8
    time.sleep(0.05)
    mx.fill(0)
    mx[int(x),int(y)] = 1
    mx.show()