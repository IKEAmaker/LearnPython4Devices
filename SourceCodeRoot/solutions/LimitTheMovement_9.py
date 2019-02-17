import board
import tinker_kit
import time

kit = tinker_kit.kit(board)

x = 3.0
y = 3.0

def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))

while True:
    up = kit.joystick.up
    right = kit.joystick.right
    x = clamp( (x + right), 0, 7.5)
    y = clamp( (y + up), 0, 7.5)
    time.sleep(0.05)
    kit.matrix.fill(0)
    kit.matrix[int(x),int(y)] = 1
    kit.matrix.show()