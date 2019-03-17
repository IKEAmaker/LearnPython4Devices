import kit
import time

while True:
    kit.matrix[0,0] = kit.joystick.push
    kit.matrix.show()
    time.sleep(0.05)