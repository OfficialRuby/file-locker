import os, pyminizip 
from tools.util import Tool
curentDir = os.getcwd()
inputFolder = os.path.join(curentDir, "Files/")
folder = os.listdir(inputFolder)
folder.sort()
try:
    for files in range (len(folder)):
        fileName = folder[files]
        fileFolder = fileName[:-4]
        outputFolder = os.path.join(curentDir, "Encrypted/")

        # outputFolder = os.path.join(outputFolder,f"{fileFolder}/")
        outputFile = os.path.join(outputFolder, fileFolder+"/"+fileFolder+".zip")
        outputFilePath = os.path.join(outputFolder, fileFolder+"/")
        try:
            os.makedirs(outputFilePath)
        except FileExistsError:
            print("A folder with the name %s already exists and will not be Overitten" %fileFolder)
            continue
        # os.makedirs(outputFilePath)

        inputFile = inputFolder+fileName
        # print(inputFile)
        # print(fileFolder)
        # print(fileName)
        # print(outputFolder)
        # print(outputFilePath)
        passwordFile= outputFilePath+fileFolder+".txt"
        # print(passwordFile)
        password = Tool.generatePassword()


        pyminizip.compress(inputFile, None, outputFile, password, 1)
        with open (passwordFile, 'w') as p:
                p.write(password)
except KeyboardInterrupt:
    print("\n Ctrl C dectected \nProgram terminated!")