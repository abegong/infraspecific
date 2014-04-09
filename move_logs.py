import os
import datetime
import glob
import shutil

import util

def move_logs(from_path, to_path):
	now = datetime.datetime.now()
	exempt_filepath = now.strftime("%Y/%m/%d")

	G = glob.glob(from_path+'*/*/*/*/*')

	for g in G:
		filepath = g.split(from_path)[1]

		if '/'.join(filepath.split('/')[:3]) != exempt_filepath:
			util.build_dirs(to_path, filepath)

			shutil.move(g, to_path+filepath)

#Mount disk:
os.system('sudo mount -o uid=pi,gid=pi /dev/sda1 /mnt/2TB_USB')

#Move logs
move_logs('/home/pi/videolog/', '/mnt/2TB_USB/pi/videolog/')
move_logs('/home/pi/audiolog/', '/mnt/2TB_USB/pi/audiolog/')
# move_logs('/Users/abe/Desktop/temp/', '/Users/abe/Desktop/temp2/')

#Unmount disk
os.system('sudo umount /mnt/2TB_USB')
