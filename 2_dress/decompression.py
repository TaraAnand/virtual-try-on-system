import os 
import random
from huffman import HuffmanCoding

def directory_iterator(): 
	cwd = os.getcwd()
	path = cwd + "/rmvlComp"
	os.chdir(path)

	files = [name for name in os.listdir('.') if os.path.isfile(name) and name.endswith("_decompressed.obj")]

	tfFilename = path  + "/textureFace_decompressed.obj"

	tfFile = open(tfFilename)
	tfLines = tfFile.readlines()
	

	for idx in range(len(files)): 
	

		filename = files[idx] 

		huffFile = open(filename)

		huffLines = huffFile.readlines()
		


		newfilename = filename.replace("_decompressed.obj", "_FullDecompressed.obj")
		#filepath = newfilename
		newfile = open(newfilename, "w")
		

		for line in tfLines: 
			if line[0] == "v":
				newfile.write(line)

		for line in huffLines: 
			newfile.write(line)

		for line in tfLines: 
			if line[0] == "f": 
				newfile.write(line)

		newfile.close()
		huffFile.close()

		#filepath = path + "/" + newfilename
		#print(filepath)
		#ogfile = (path + "/../" +filename).replace(".bin", ".obj")
		#print(ogfile

		#texture_face_addition(filepath, tf)


#def texture_face_addition(): 

directory_iterator()