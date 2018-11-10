import os 
import random

def create_directory(newdir):
 	# Create a new directory 
	path = os.getcwd()
	print("The current working directory is %s" %path)

	newpath = path + "/" + newdir 
	print("The new directory that will be created is %s" %newpath)

	try: 
		os.mkdir(newpath)
	except OSError: 
		print("Creation of the directory %s failed" %newpath)
	else: 
		print("Successfully created the directory %s " %newpath)

	#Create new .obj files
	files = [name for name in os.listdir('.') if os.path.isfile(name) and name.endswith(".obj")]
	
	for idx in range(len(files)): 
		oldname = files[idx]						#uncompressed filename
		newfilename = newpath + "/" + oldname		#compressed file path
		oldfilename = path + "/" + oldname
		
		newfile = open(newfilename, "w")
		newfile.close()

		if newdir == "rmvlComp": 
			remove_texture_and_face(newfilename, oldfilename)
		elif newdir == "compressed": 
			reduce_vertices(newfilename, oldfilename)

def remove_texture_and_face(newfilename, oldfilename): 
	oldfile = open(oldfilename)
	print("Opening old %s" %oldfilename)
	newfile = open(newfilename, "w")
	print("Opening new %s" %newfilename)

	lines = oldfile.readlines()
	print("Lines")
	print(lines)

	for line in lines: 
		print(line)
		if line[0] == "v": 
			print("Line starts with v \n")
			if line[1] == " ": 
				print("Line is vertext line \n")
				newfile.write(line)

	newfile.close()
	oldfile.close()

def reduce_vertices(newfilename, oldfilename):
	oldfile = open(oldfilename)
	#print("Opening %s" %oldfilename)
	newfile = open(newfilename, "w")
	#print("Opening %s" %newfilename)

	lines = oldfile.readlines() 
	for line in lines: 
		#print(line)
		#Check line includes vertices
		if line[0] != "v" or line[1] != " ": 
			break

		lineVars = line.split()

		x = float(lineVars[1])
		y = float(lineVars[2])
		z = float(lineVars[3])

		weights = calculate_vals(x, y, z)

		w1 = weights[0]
		w2 = weights[1]
		w3 = weights[2]

		encodedData = str(w1 * x + w2 * y + w3 * z)

		newfile.write(encodedData)

	newfile.close()
	oldfile.close()


def calculate_vals(x, y, z): 
	f = 3
	m = max(x, y, z) + (max(x, y, z) / 2)
	w1 = random.uniform(0,1)
	w2 = (w1 + m) + f 
	w3 = (m * w1 + m * w2) * f

	return (w1, w2, w3)

#reduce_vertices()
create_directory("rmvlComp")
os.chdir(os.getcwd() + "/rmvlComp")
create_directory("compressed") 