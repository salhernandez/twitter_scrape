import os

currentDirectory = os.getcwd()+"/"
dataOutput = currentDirectory+"data/"
source = currentDirectory+"data/users/"

#if not os.path.exists(souce):
#        os.makedirs(source) 

out = open(dataOutput+"users.txt", "w")
arr = []
for subdir, dirs, files in os.walk(source):
    for file in files:
        test = os.path.join(subdir, file)
        arr.append(test)
for i in arr:
	with open(i, "r") as f:
		for line in f:
			#removes the '\n' from the read
			line =  line[:-1]
			print line
			out.write(line+"\n")
out.close()
