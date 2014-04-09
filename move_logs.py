import os
import datetime
import glob
import shutil

import util

def move_logs(from_path, to_path):
	now = datetime.datetime.now()
	exempt_filepath = "hi"#now.strftime("/%Y/%m/%d")

	G = glob.glob(from_path+'*/*/*')

	for g in G:
		filepath = '/'+g.split(from_path)[1]
		if filepath != exempt_filepath:
			util.build_dirs(to_path, filepath)
			shutil.move(g, to_path+filepath)

#Mount disk:
os.cmd('sudo mount -o uid=pi,gid=pi /dev/sda1 /mnt/2TB_USB')

#Move logs
move_logs('/home/pi/videolog/', '/mnt/2TB_USB/pi/videolog/')
move_logs('/home/pi/audiolog/', '/mnt/2TB_USB/pi/audiolog/')

#Unmount disk
os.cmd('sudo unmount /mnt/2TB_USB')
