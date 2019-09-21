#Author: thulek@gmail.com
#Extract a phylip to the partitioned phylip files (input raxml partition)

from os import listdir
from os.path import isfile, join
import os
import sys
import argparse
from datetime import datetime

text = 'The Vertical Join script for merge 2 same-line files vertically.'
parser = argparse.ArgumentParser(description = text)  

parser.add_argument("-f", "--filex", help="The file A")
parser.add_argument("-j", "--joint", help="the joined file")
parser.add_argument("-t", "--tx", help="the merge type: 1 -- merge into file A, 2-- merge into joined file")
args = parser.parse_args()

filex = args.filex

if args.joint:
	part = args.joint
else:
	part = "partition.txt"

if args.tx:
	tx = int(args.tx)
else:
	tx = 1

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d%m%Y%H%M%S%f")

output = filex+"_parf_o"+str(timestampStr)

def readLine(files,linen):
	fp = open(files,"r")
	for i, line in enumerate(fp):
		if i == (linen-1):
			return line.strip()
		elif i > (linen-1):
			break
	fp.close()

def countLines(files):
	if(os.path.isfile(files)):
		with open(files) as f:
			return len(f.readlines())
	else:
		return 0
		

#print("Line number: "+str(countLines(filex))+" - "+str(countLines(part))+"\n")
if countLines(filex) == countLines(part):
	rOut = open(output,"w")
	rline = open(filex,"r")	
	i = 1
	for l in rline:
		#print(str(readLine(part,i)))
		rOut.write(str(l).rstrip("\n")+str(readLine(part,i)).strip()+"\n")
		i=i+1
	rOut.close()
	if(tx==1):
		os.system("rm "+filex)
		os.system("mv "+output+" "+filex)
	else:
		os.system("rm "+part)
		os.system("mv "+output+" "+part)
else:
	print("Two files're not same lines.")		