#! /usr/bin/env python

import csv     # imports the csv module
import sys      # imports the sys module
import os
import shutil

# yes ok a primitive menu
if len(sys.argv) < 4 : 
	sys.exit("** Usage: ./formatCSV <infile> <p|np> (option to print modified lines or not) <ovw|n> (option to overwrite existing file, else create new one named \"name_2\" **")
	
name = sys.argv[1]
p=False
ovw=False

if sys.argv[2]=="p":
	p=True

if sys.argv[3]=="ovw":
        ovw=True

f = open(name, 'rb') # opens the csv file
w = open(name+'_2', 'wb')
writer = csv.writer(w)
i = 0
try:
	reader = csv.reader(f)  # creates the reader object
	for row in reader:   # iterates the rows of the file in orders

		if not row: continue

        	i+=1
		#print i
		row[0]=i

		if p==True:
 			print row    # prints each row

		writer.writerow(row)
finally:
	f.close()      # closingi
	w.close()

if ovw==True:
	shutil.copyfile(name+'_2',name)
	os.remove(name+'_2')	

