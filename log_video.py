import datetime
import os
import util

base_path = '/home/pi/videolog/'

now = datetime.datetime.now()
filename = now.strftime("%Y/%m/%d/%H/vid-%Y%m%d-%H%M%S.mpg")

util.build_dirs(base_path, filename)

cmd = "/usr/local/bin/ffmpeg -y -t 10 -r 15 -s 320x240 -f video4linux2 -i /dev/video0 -r 30 "+base_path+filename
os.system(cmd)