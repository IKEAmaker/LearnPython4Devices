import board
import tinker_kit
import time

mx, UD, LR, push, bf = tinker_kit.setup_hardware(board)

while True:
    mx[0,0] = 0
    mx.show()
    time.sleep(0.5)
    mx[0,0] = 1
    mx.show()
    time.sleep(0.5)