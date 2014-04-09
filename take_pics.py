import os
import time
import datetime

while 1:
	os.system('ffmpeg -y -f video4linux2 -i /dev/video0 ../pic.jpg')
	time.sleep(1)
