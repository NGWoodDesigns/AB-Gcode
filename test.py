import sys
import os
import re
import shutil
import fileinput
from Tkinter import *
import tkFileDialog
from tkFileDialog import askopenfile

#Title definitions
X = ""
T = ""
C = ""
M = ""
K = ""
L = ""

#Waste. Changed to comment and left for reference.
#Key-hertz library
#Cy = 65
#Dy = 73
#Ey = 82
#Fy = 87
#Gy = 98
#Ay = 110
#By = 123
#C = 130
#D = 146
#E = 164
#F = 174
#G = 196
#A = 220
#B = 246 
#c = 261
#d = 293
#e = 329
#f = 349
#g = 392
#a = 440
#b = 493
#cz = 523
#dz = 587
#ez = 659
#fz = 698
#gz = 784
#az = 880
#bz = 987

#Library for char conversion
#rptps = Repeat post
#rptpr = Repeat previous
char = {",":"y" , "'":"z", "|:":"rptps", ":|":"rptpr", "|":""}

#Library for notes
notes = {"Cy":"65" + "\n", "Dy":"73" + "\n", "Ey":"82" + "\n", "Fy":"87" + "\n", "Gy ":"98" + "\n", "Ay":"110" + "\n", "By":"123" + "\n", "C":"130" + "\n", "D":"146" + "\n", "E":"164" + "\n", "F":"174" + "\n", "G":"196" + "\n", "A":"220" + "\n", "B":"246" + "\n", "c":"261" + "\n", "d":"293" + "\n", "e":"329" + "\n", "f":"349" + "\n", "g":"392" + "\n", "a":"440" + "\n", "b":"493" + "\n", "cz":"523" + "\n", "dz":"587" + "\n", "ez":"659" + "\n", "fz":"698" + "\n", "gz":"784" + "\n", "az":"880" + "\n", "bz":"987" + "\n"}

#Open and read file
file1 = askopenfile(mode='r')

#Get filename/path
name = file1.name
tmp = name + ".tmp"
print name

def conversion():
#Converts code in file and writes to a temp file
    #Opens file(r) and temp(w) file    
    with open(name) as infile, open(tmp, 'w') as outfile:
        for line in infile:
            #Remove headerlines
            if line.startswith(('X', 'T', 'C', 'M', 'K', 'L')):
                outfile.write(line)
            else:
                #Replace any problem characters
                for src, target in char.iteritems():
                    line = line.replace(src, target)
                    #Remove any whiteliness
                    line = line.replace(" ", "")
                    #Replace notes with their corresponding frequency
                    for src, target in notes.iteritems():
                        line = line.replace(src, "m300" + target)
                line = line.replace("m300", "m300 ")
        #Write to file
        outfile.write(line)
        
def readheader():
    #Open file
    with open(tmp, 'r'):
        line = 0
        while line <= 5:
            print tmp.line

    
def debug():
    #This will allow us to display the file in the program.
    file = open(tmp, 'r')
    print file.read()
    
    
conversion()
debug()
