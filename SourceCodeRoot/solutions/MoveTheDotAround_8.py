import board
import tinker_kit
import time

kit = tinker_kit.kit(board)

x = 3.0
y = 3.0

while True:
    up = kit.joystick.up
    right = kit.joystick.right
    x = (x + right)%8
    y = (y + up)%8
    time.sleep(0.05)
    kit.matrix.fill(0)
    kit.matrix[int(x),int(y)] = 1
    kit.matrix.show()