import os


def check_directory(dirName):
	if os.path.isdir(dirName):
		return True
	else:
		return False

def create_directory(dirName):
	if os.path.exists(dirName):
		return -1
	else:
		os.makedirs(dirName)

def create_file(dirName, fileName, contents):
	if os.path.isdir(dirName):
		file_path = os.path.join(dirName, fileName)
		if not os.path.exists(file_path):
			fileout = open(file_path, "w")
			fileout.write(contents)
			fileout.close()
		else:
			return -1
	else:
		return -1

def list_directory(dirName, list):
	if os.path.isdir(dirName):
		files = os.listdir(dirName)
		print("The files in that directory are: ")
		for file in files:
			list.append(file)
	else:
		return -1

def check_file(dirName, fileName):
	if os.path.isdir(dirName):
		file_path = os.path.join(dirName, fileName)
		if os.path.isfile(file_path):
			return True
		else:
			return False
	else:
		return False


def delete_file(dirName, fileName):
	if os.path.isdir(dirName):
		file_name = input("Enter the name of the file: ")
		file_path = os.path.join(dirName, fileName)
		if os.path.isfile(file_path):
			os.remove(file_path)
		else:
			return -1
	else:
		return -1

def delete_directory(dirName):
	if os.path.isdir(dirName):
		files = os.listdir(dirName)
		for file in files:
			os.remove(os.path.join(dirName, file))
		os.rmdir(dirName)
	else:
		return -1
