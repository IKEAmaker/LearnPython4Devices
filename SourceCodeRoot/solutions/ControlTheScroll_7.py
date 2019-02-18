import board
import tinker_kit
import time

kit = tinker_kit.kit(board)

relative_position = 0.0
absolute_position = 0
speed = 0.0

while True:
    time.sleep(0.02)
    speed = kit.joystick.right
    relative_position = (relative_position + speed) % 45
    absolute_position = int(relative_position) - 25
    kit.matrix.fill(0)
    kit.font.text('IKEA', absolute_position, 0, 1)
    kit.matrix.show()
