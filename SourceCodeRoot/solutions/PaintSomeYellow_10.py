import board
import tinker_kit
import time

mx, UD, LR, push, bf = tinker_kit.setup_hardware(board)

x = 3.0
y = 3.0
x_old = 3.0
y_old = 3.0
paint = False

def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))

while True:
    paint = paint or not push.value
    up = (UD.value/65536) - 0.5
    left = (LR.value/65536) - 0.5
    x = clamp( (x + left), 0, 7)
    y = clamp( (y + up), 0, 7)
    mx[int(x),int(y)] = 1
    if int(x) != int(x_old) or int(y) != int(y_old):
        if paint :
            mx[int(x_old), int(y_old)] = 1
            paint = False
        else:
            mx[int(x_old), int(y_old)] = 0
    mx.show()
    time.sleep(0.05)
    x_old = x
    y_old = y