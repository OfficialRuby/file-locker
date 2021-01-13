#!/usr/bin/python3
import os, pyminizip, sys
from tools.util import Tool
curentDir = os.getcwd()
inputFolder = os.path.join(curentDir, "Files/")
folder = os.listdir(inputFolder)
folder.sort()
more_files = folder
more_files.sort()

more = Tool.multiple(more_files)
# print(more)

try:
    
    for files in range (len(more)):
        fileName = more[files] #Output name of duplicate files
        realFileName = folder[0] #Real file to be reproduced, it is the input file
        realFileDir = inputFolder+realFileName
        if  os.path.isfile(realFileDir):
            # print(yike)
            fileFolder = fileName[:-4]
            # print(fileFolder)
            outputFolder = os.path.join(curentDir, "Encrypted/")
            outputFile = os.path.join(outputFolder, fileFolder+"/"+fileFolder+".zip")
            outputFilePath = os.path.join(outputFolder, fileFolder+"/")
            try:
                os.makedirs(outputFilePath)
            except FileExistsError:
                print("A folder with the name %s already exists and will not be Overitten" %fileFolder)
                continue

            inputFile = inputFolder+realFileName
            passwordFile= outputFilePath+fileFolder+".txt"
            password = Tool.generatePassword()    
            pyminizip.compress(inputFile, None, outputFile, password, 1)
            with open (passwordFile, 'w') as p:
                    p.write(password)
        else:
            print("The FOLDER directory does not contain any file\n")
            sys.exit()
except KeyboardInterrupt:
    print("\n Ctrl C dectected \nProgram terminated!")
