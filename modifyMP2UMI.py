#! /usr/bin/env python
# 
import sys
from sys import argv
from os.path import exists

file, in_file = argv
print "/nScript to create new import file with modified UMI commands \n"
print "Usage: e.g. ./modifyMP2UMI.py <mp2exportfile> "
print "or: python modifyMP2UMI.py <mp2exportfile> \n"


print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input("[Press Enter] \n")

out_file = open("importUMIs.txt", 'w')
infile = open(in_file, 'r')

string1 = "\nFILE VERSION:11.00.01:MP2\n\n"
out_file.write(string1)

fFound = False

for line in infile:
	strLine = line.replace('\n', '')
	if(strLine=="UMI"):
		fFound = True
		
	if(strLine==";;" and fFound == True):
		fFound = False
		out_file.write("\t,MCPNAME=\"Default Mobile Client Profile\"\n\t,NEWMCPNAME=\"\"\n\t,OVERWRITEMOBTIMERS=false\n")	
		out_file.write(line)
		
	if(fFound == True):
#		print strLine
		out_file.write(line)

print "### DONE ###\n"

out_file.close()
infile.close()
