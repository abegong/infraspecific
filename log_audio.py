import datetime
import os

import util

base_path = '/home/pi/audiolog/'

now = datetime.datetime.now()
filename = now.strftime("%Y/%m/%d/%H/aud-%Y%m%d-%H%M%S.wav")

util.build_dirs(base_path, filename)

cmd = "arecord -f S16_LE -d 10 "+base_path+filename
os.system(cmd)
