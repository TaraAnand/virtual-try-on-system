import os 
import random

def create_directory(newdir):
 	# Create a new directory 
	path = os.getcwd()
	print("The current working directory is %s" %path)

	path = path + "/" + newdir 
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
		
		newfile = open(filename)
		newfile.close()

		if newdir == "rmvlComp": 
			remove_texture_and_face(newfile, oldfile)
		elif newdir == "compressed": 
			reduce_vertices(newfile, oldfile)

def remove_texture_and_face(newfilename, oldfilename): 
	oldfile = open(oldfilename)
	newfile = open(newfilename)

	lines = oldfile.readlines()
	for line in lines: 
		if line[0] == "v": 
			if line[1] == "t": 
				#skip line
			newfile.write(line)

	newfile.close()
	oldfile.close()

def reduce_vertices(newfilename, oldfilename):
	oldfile = open(oldfilename)
	newfile = open(newfilename)

	lines = oldfile.readlines() 
	for line in lines: 
		#Check line includes vertices
		if line[0] != "v" or line[1] ! = " ": 
			break

		lineVars = line.split()

		x = lineVars[1]
		y = lineVars[2]
		z = lineVars[3]

		weights = calculate_vals(x, y, z)

		w1 = weights[0]
		w2 = weights[1]
		w3 = weights[2]

		encodedData = w1 * x + w2 * y + w3 * z 

		newfile.write(encodedData)

	newfile.close()
	oldfile.close()


def calculate_vals(x, y, z): 
	f = 3
	m = max(x, y, z) = (max(x, y, z) / 2)
	w1 = random.uniform(0,1)
	w2 = (w1 + m) + f 
	w3 = (m * w1 + m * w2) * f

	return (w1, w2, w3)


create_directory("/rmvlComp")
os.chdir(os.getcwd() + "/rmvlComp")
create_directory("/compressed") 