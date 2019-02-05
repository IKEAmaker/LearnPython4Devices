import board
import tinker_kit
import time

mx, UD, LR, push, bf = tinker_kit.setup_hardware(board)

x = 3.0
y = 3.0

def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))

while True:
    up = (UD.value/65536) - 0.5
    left = (LR.value/65536) - 0.5
    x = clamp( (x + left), 0, 7)
    y = clamp( (y + up), 0, 7)
    time.sleep(0.05)
    mx.fill(0)
    mx[int(x),int(y)] = 1
    mx.show()