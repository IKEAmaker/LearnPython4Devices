import kit
import time

x = 3.0
y = 3.0
x_old = 3.0
y_old = 3.0
paint = False

def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))

while True:
    paint = paint or kit.joystick.push
    up = kit.joystick.up
    right = kit.joystick.right
    x = clamp( (x + right), 0, 7.5)
    y = clamp( (y + up), 0, 7.5)
    kit.matrix[int(x),int(y)] = 1
    if int(x) != int(x_old) or int(y) != int(y_old):
        if paint :
            kit.matrix[int(x_old), int(y_old)] = 1
            paint = False
        else:
            kit.matrix[int(x_old), int(y_old)] = 0
    kit.matrix.show()
    time.sleep(0.05)
    x_old = x
    y_old = y