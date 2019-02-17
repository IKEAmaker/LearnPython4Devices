import board
import tinker_kit
import time

kit = tinker_kit.kit(board)

relative_position = 0.0
absolute_position = 0
right = 0.0

while True:
    right = kit.joystick.right
    relative_position = (relative_position + right) % 50
    absolute_position = int(relative_position) - 25
    kit.matrix.fill(0)
    kit.font.text('IKEA', absolute_position, 1, 100)
    kit.matrix.show()
    time.sleep(0.02)