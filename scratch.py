from movingsign import MovingSign
ms1 = MovingSign()
ms2 = MovingSign()
write = ms1.cmd_txt(b"MOTHER")
delete = ms2.clear()
import serial
ser = serial.Serial('/dev/ttyACM0', 9600)
