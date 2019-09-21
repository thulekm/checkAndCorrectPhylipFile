#convert phylip to fasta
#Author: Thulek@gmail.com
 
from os import listdir
from os.path import isfile, join
import os
import sys
import platform
import subprocess
import time
import array as arr
#import runCommand

import argparse

text = "===================\nCheck Phylip File and write the sequence's status to a log file\n===================="

parser = argparse.ArgumentParser(description = text)  
#parser.parse_args()  

jobIds = arr.array('i')

parser.add_argument("-f", "--filex", help="The phylip file")

# read arguments from the command line
args = parser.parse_args()

filex = args.filex
#output = args.output

def countLines(files):
	if(os.path.isfile(files)):
		with open(files) as f:
			return len(f.readlines())
	else:
		return 0


if os.path.isfile(filex):
	infile = open(filex,"r")
	outfile = open(filex+".log","w")
	i = 1
	tax = 0
	sites = 0
	for line in infile:
		if i > 1:
			if len(line.strip()) >= 1:
				if "\t" in line:
					tx = line.split("\t",1)
					outfile.write(""+tx[0].strip()+"\t")
					outfile.write(str(len(tx[1].strip()))+"\t")
					if(len(tx[1].strip()) == sites):
						outfile.write("Ok\n")
					else:
						outfile.write("Nok\n")
				elif " " in line:
					tx = line.split(" ",1)
					outfile.write(""+tx[0].strip()+"\t")
					outfile.write(str(len(tx[1].strip()))+"\t")
					if(len(tx[1].strip()) == sites):
						outfile.write("Ok\n")
					else:
						outfile.write("Nok\n")
		else:
			tx = line.split(" ",1)
			#tax = int(tx[0].strip())
			sites = int(tx[1].strip())
		i = i + 1
	outfile.close()
	infile.close()
	if(countLines(filex+".log")>0):
		print "Finish check file."
	else:
		print "Create log file error."
else:
	print "Input file's not exists."
	