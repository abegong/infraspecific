import os

def build_dirs(base_path, filename):
	dir_list = filename.split('/')
	# print dir_list

	for i in range(len(dir_list)):
		temp_dir = base_path+'/'.join(dir_list[:i])
		# print temp_dir
		if not os.path.exists(temp_dir):
		    os.makedirs(temp_dir)