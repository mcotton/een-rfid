import serial

#configure to your device
PORT = '/dev/ttyUSB0'
SPEED = 9600

#remove extra chars from RFID string
def cleaner(dirty):
	return dirty.translate(None, '\x02\x03\r\n')	

ser = serial.Serial(PORT, SPEED)

print 'Starting...'
while ser.isOpen():
	print cleaner(ser.readline())

print ' ...Not able to open serial port ' + PORT

