import board
import tinker_kit
import time

mx, UD, LR, push, bf = tinker_kit.setup_hardware(board)

relative_position = 0.0
absolute_position = 0
left = 0.0

while True:
    left = (LR.value/65536) - 0.5
    relative_position = (relative_position + left) % 50
    absolute_position = int(relative_position) - 25
    mx.fill(0)
    bf.text('IKEA', absolute_position, 0, 1)
    mx.show()
    time.sleep(0.02)