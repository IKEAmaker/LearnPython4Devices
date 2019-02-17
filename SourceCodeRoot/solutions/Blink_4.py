import board
import tinker_kit
import time

kit = tinker_kit.kit(board)

while True:
    kit.matrix[0,0] = 0
    kit.matrix.show()
    time.sleep(0.5)
    kit.matrix[0,0] = 1
    kit.matrix.show()
    time.sleep(0.5)