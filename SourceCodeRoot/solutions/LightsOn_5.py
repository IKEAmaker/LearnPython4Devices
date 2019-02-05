import board
import tinker_kit
import time

mx, UD, LR, push, bf = tinker_kit.setup_hardware(board)

while True:
    mx[0,0] = not push.value
    mx.show()
    time.sleep(0.05)