import kit
import time

while True:
    for i in range(20, -25, -1):
        kit.matrix.fill(0)
        kit.font.text('IKEA', i, 0, 1)
        kit.matrix.show()
        time.sleep(0.05)