import datetime
import os

cmd = "/usr/local/bin/ffmpeg -y -t 10 -r 15 -s 320x240 -f video4linux2 -i /dev/video0 -r 30 /home/pi/videolog/vid-"+datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+".mpg"
os.system(cmd)