import board
import tinker_kit
import time

kit = tinker_kit.kit(board)

while True:
    for i in range(15, -30, -1):
        kit.matrix.fill(0)
        kit.font.text('IKEA', i, 0, 1)
        kit.matrix.show()
        time.sleep(0.05)