import os 

def create_directory():
 	# Create a new directory 
	path = os.getcwd()
	print("The current working directory is %s" %path)

	path = path + "/compressed"
	print("The new directory that will be created is %s" %path)

	try: 
		os.mkdir(path)
	except OSError: 
		print("Creation of the directory %s failed" %path)
	else: 
		print("Successfully created the directory %s " %path)

	#Create new .obj files
	files = [name for name in os.listdir('.') if os.path.isfile(name)]
	
	for idx in range(len(files)): 
		oldname = files[idx]				#uncompressed filename
		filename = path + "/" + oldname		#compressed filename
		oldfile = open(oldname)
		newfile = open(filename)
		remove_texture_and_face(newfile, oldfile)

def remove_texture_and_face(newfile, oldfile): 
	lines = oldfile.readlines()
	for line in lines: 
		if line[0] == "v": 
			if line[1] == "t": 
				#skip line
			newfile.write(line)

create_directory() 

