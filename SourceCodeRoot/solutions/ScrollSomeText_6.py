import board
import tinker_kit
import time

mx, UD, LR, push, bf = tinker_kit.setup_hardware(board)

while True:
    for i in range(15, -30, -1):
        mx.fill(0)
        bf.text('IKEA', i, 1, 100)
        mx.show()
        time.sleep(0.05)