import datetime
import os

cmd = "arecord -f S16_LE -d 10 /home/pi/audiolog/aud-"+datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+".wav"
os.system(cmd)
