#! /usr/bin/python

import glob
import os

fileTypes = ["./*.ofx", "./*.QFX", "./*.sldasm", "./*.sldprt", "./*.step", "./*.stp", "./*.igs", "./*.iges", "./*.zip", "./*.dxf"]


def makeBool(char):
	char = char.lower()
	if char == "y" or char == "yes":
		return True
	return False

if makeBool(input("Are you sure you want to clean this folder? ")):
    print("Cleaning up files...")
    
    cleanList = glob.glob(fileTypes[0])
    
    for type in fileTypes:
        cleanList += glob.glob(type)    

    for file in cleanList:
        os.remove(file)
        print(file + "\tdeleted")

anyKey = input("Press any key to close...")
if anyKey:
    exit(0)