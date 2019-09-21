#Author: thulek@gmail.com
#correct an error phylip file

from os import listdir
from os.path import isfile, join
import os
import sys
import argparse

text = 'correct an error phylip file'
parser = argparse.ArgumentParser(description = text)  

parser.add_argument("-f", "--filex", help="The Phylip")
args = parser.parse_args()

filex = args.filex

filename = ""
path = ""
if "/" in filex:
	pathex = filex.split("/")
	filename = pathex[len(pathex)-1]
	path = filex.strip(filename)
else:
	filename = filex

def checkPar(filex):
	vfile = open(filex,"r")
	y = vfile.readline()
	if "=" in y:
		return True
	else:
		return False

i = 1
z = 1
xx = 1
if os.path.isfile(filex):
	infile = open(filex,'r')
	for line in infile:
		if i == 1:
			head_file = open(filex+"_head","w")
			head_file.write(line.strip()+"\n")
			head_file.close()
		else:
			if len(line.strip()) < 1:
				z+=1
			else:
				temp_file = open(filex+"_"+str(z),"a+")
				temp_file.write(line.strip()+"\n")
				temp_file.close()
		i+=1
	if z >= 3:
		t = 0
		while xx < (z-1):
			if(os.path.isfile(filex+"_"+str(xx+1)) and os.path.isfile(filex+"_1")):
				if(checkPar(filex+"_"+str(xx+1))):
					os.system("mv "+filex+"_"+str(xx+1)+" "+filex+"_"+str(z))
				else:
					os.system("python verticalJoin.py -f "+filex+"_1"+" -j "+filex+"_"+str(xx+1)+" -t 1")
			else:
				t+=1
			xx+=1	
		if t > 0:
			if(os.path.isfile(filex+"_"+str(z))):
				os.system("mv "+filex+"_"+str(z)+" "+filex+"_"+str(z-t))
			z = z - t
		if(checkPar(filex+"_"+str(z))): 
			os.system("mv "+filex+"_"+str(z)+" "+path+"PAR_"+filename)
		else:
			os.system("python verticalJoin.py -f "+filex+"_1"+" -j "+filex+"_"+str(z)+" -t 1")
		os.system("cat "+filex+"_head "+filex+"_1 > "+path+"output."+filename)
		os.system("rm "+filex+"_*")
	elif z==2:
		if(checkPar(filex+"_"+str(z))): 
			os.system("mv "+filex+"_"+str(z)+" "+path+"PAR_"+filename)
		else:
			os.system("python verticalJoin.py -f "+filex+"_1"+" -j "+filex+"_"+str(z)+" -t 1")
		os.system("cat "+filex+"_head "+filex+"_1 > "+path+"output."+filename)
		os.system("rm "+filex+"_*")
	else:
		#os.system("cat "+filex+"_head "+filex+"_1 > "+path+"output."+filename)
		print("Don't need correct.")
		os.system("rm "+filex+"_*")
else:
	print "File's not exists."