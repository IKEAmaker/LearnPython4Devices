import sys
import os
import win32api
import serial
from distutils.dir_util import copy_tree
from zipfile import ZipFile
from urllib.request import urlretrieve
from shutil import copy2
from time import sleep
from PyQt5 import QtWidgets

from setup_utilityUI import Ui_MainWindow

class MainWindow_EXEC():

    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)

        # pyuic5 converted QT Windows
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)

        self.ui.pushButton_refresh.clicked.connect(self.check_device)
        self.ui.pushButton_init_device.clicked.connect(self.init_device)
        self.ui.pushButton_reset_projects.clicked.connect(self.reset_projects)

        self.device_status = 'none'
        self.device_drive = ''

        self.firmware_url = 'https://github.com/IKEAmaker/LearnPython4Devices/raw/master/Firmware/adafruit-circuitpython-trinket_m0-3.1.2.uf2'
        self.firmware_temp_file = 'adafruit-circuitpython-trinket_m0-3.1.2.uf2'
        self.source_zip_url = 'https://github.com/IKEAmaker/LearnPython4Devices/archive/master.zip'
        self.source_zip_file = 'LearnPython4Devices-master.zip'
        self.source_base = '\\LearnPython4Devices-master\\SourceCodeRoot'

        self.file_list = [
            'LearnPython4Devices-master/SourceCodeRoot/tinker_kit.py',
            'LearnPython4Devices-master/SourceCodeRoot/boot.py',
            'LearnPython4Devices-master/SourceCodeRoot/font5x8.bin',
            'LearnPython4Devices-master/SourceCodeRoot/main.py',
            'LearnPython4Devices-master/SourceCodeRoot/lib/adafruit_dotstar.mpy',
            'LearnPython4Devices-master/SourceCodeRoot/lib/bitmapfont.py',
            'LearnPython4Devices-master/SourceCodeRoot/lib/font_to_bin.py',
            'LearnPython4Devices-master/SourceCodeRoot/lib/adafruit_bus_device/__init__.py',
            'LearnPython4Devices-master/SourceCodeRoot/lib/adafruit_bus_device/i2c_device.mpy',
            'LearnPython4Devices-master/SourceCodeRoot/lib/adafruit_bus_device/spi_device.mpy',
            'LearnPython4Devices-master/SourceCodeRoot/lib/adafruit_ht16k33/__init__.py',
            'LearnPython4Devices-master/SourceCodeRoot/lib/adafruit_ht16k33/ht16k33.mpy',
            'LearnPython4Devices-master/SourceCodeRoot/lib/adafruit_ht16k33/matrix.mpy',
            'LearnPython4Devices-master/SourceCodeRoot/projects/Blink_4.py',
            'LearnPython4Devices-master/SourceCodeRoot/projects/ControlTheScroll_7.py',
            'LearnPython4Devices-master/SourceCodeRoot/projects/LightsOn_5.py',
            'LearnPython4Devices-master/SourceCodeRoot/projects/LimitTheMovement_9.py',
            'LearnPython4Devices-master/SourceCodeRoot/projects/MoveTheDotAround_8.py',
            'LearnPython4Devices-master/SourceCodeRoot/projects/PaintSomeYellow_10.py',
            'LearnPython4Devices-master/SourceCodeRoot/projects/ScrollSomeText_6.py',
            'LearnPython4Devices-master/SourceCodeRoot/solutions/Blink_4.py',
            'LearnPython4Devices-master/SourceCodeRoot/solutions/ControlTheScroll_7.py',
            'LearnPython4Devices-master/SourceCodeRoot/solutions/LightsOn_5.py',
            'LearnPython4Devices-master/SourceCodeRoot/solutions/LimitTheMovement_9.py',
            'LearnPython4Devices-master/SourceCodeRoot/solutions/MoveTheDotAround_8.py',
            'LearnPython4Devices-master/SourceCodeRoot/solutions/PaintSomeYellow_10.py',
            'LearnPython4Devices-master/SourceCodeRoot/solutions/ScrollSomeText_6.py'
        ]


        self.check_device()

        MainWindow.show()
        sys.exit(app.exec_())

    def check_device(self):
        status_message = "No connected devices found"
        drives = win32api.GetLogicalDriveStrings()
        drives = drives.split('\000')[:-1]
        self.device_status = 'none'
        self.device_drive = ''

        for drive in drives:
            try:
                label = win32api.GetVolumeInformation(drive)[0]
                if label == "CIRCUITPY":
                    status_message = 'Found running device on '
                    self.device_status = 'run'
                    self.device_drive = drive
                elif label == "TRINKETBOOT":
                    status_message = 'Found a trinket in boot mode on '
                    self.device_drive = drive
                    self.device_status = 'boot'
            except:
                pass
        self.ui.statusbar.showMessage(status_message+self.device_drive)
        if self.device_status == 'none':
            self.ui.textEdit_status.setText('Connect a Tinker Kit device')
            self.ui.pushButton_init_device.setEnabled(False)
            self.ui.pushButton_reset_projects.setEnabled(False)
        elif self.device_status == 'run':
            self.ui.textEdit_status.setText('To flash the devices firmware double press the reset button')
            self.ui.pushButton_init_device.setEnabled(False)
            self.ui.pushButton_reset_projects.setEnabled(True)
        elif self.device_status == 'boot':
            self.ui.textEdit_status.setText('You can now flash the devices firmware')
            self.ui.pushButton_init_device.setEnabled(True)
            self.ui.pushButton_reset_projects.setEnabled(False)

    def init_device(self):
        self.ui.pushButton_init_device.setEnabled(False)
        if not os.path.isfile(self.firmware_temp_file):
            print('downloading ..')
            urlretrieve(self.firmware_url, self.firmware_temp_file)
            print('done')
        copy2(self.firmware_temp_file, self.device_drive)
        sleep(5)
        self.check_device()


    def reset_projects(self):
        ports = ['COM%s' % (i + 1) for i in range(256, 1, -1)]
        for port in ports:
            try:
                s = serial.Serial(port, 115200, timeout=1)
                s.write(b'\x03')
                s.write(b'print("hello")\r')
                response = s.read()
                s.close()
                break
            except (OSError, serial.SerialException):
                pass

        if not os.path.isfile(self.source_zip_file):
            print('downloading ..')
            urlretrieve(self.source_zip_url, self.source_zip_file)
            print('done')
        with ZipFile(self.source_zip_file, 'r') as zf:
            file_names = zf.namelist()
            for file in self.file_list:
                if file in file_names:
                    zf.extract(file, '.')
                else:
                    print(file)
        print('from: '+os.getcwd()+self.source_base+' to: '+self.device_drive)
        #copy_tree(os.getcwd()+self.source_base, self.device_drive)

        #s = serial.Serial(port, 115200)
        #s.write(b'\x04')
        #s.close()


if __name__ == "__main__":
    MainWindow_EXEC()
