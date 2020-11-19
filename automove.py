from pdf2image import convert_from_path
import os
import sys
import time
import glob
import shutil
import random
import hashlib
from PIL import Image
from pyzbar.pyzbar import decode

# os.rename("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
# shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
# os.replace("path/to/current/file.foo", "path/to/new/destination/for/file.foo")

outputDir = "output/"
targetDir = "documents/"
destinationDir = "share/"


def convert(file, targetDir, outputDir):
    num1 = random.randint(10000, 99999)
    outputDir = outputDir + str(round(time.time())) + str(num1) + '/'
    originalFilename, originalFile_extension = os.path.splitext(file)

    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    # Convert PDF to Image
    # pages = convert_from_path(file, 500)
    pages = convert_from_path(file)
    counter = 1
    for page in pages:
        myfile = outputDir + 'output' + str(counter) + '.jpg'
        counter = counter + 1
        page.save(myfile, "JPEG")
        # Decode QR Code
        data = decode(Image.open(myfile))
        newDestinationFolder = destinationDir
        for i in data:
            # Get Code
            folderName = i.data.decode("utf-8")
            print(folderName)

            # Check Folder + Create Folder
            newDestinationFolder = destinationDir+folderName
            if not os.path.exists(newDestinationFolder):
                os.makedirs(newDestinationFolder)

            # Move File

            num2 = random.randint(10000, 99999)
            shutil.move(file, newDestinationFolder+"/" +
                        hashlib.md5(folderName.encode()).hexdigest() + "-"+str(num2)+originalFile_extension)

            print("----"+newDestinationFolder+"----")
            print(folderName)
            listFile = [f for f in glob.glob(
                newDestinationFolder + "/*.*")]

            print("====================")
            listFile.sort(key=os.path.getctime)
            num = 0
            for f in listFile:
                num += 1
                f_name, f_ext = os.path.splitext(f)
                renameFilename = folderName+"-"+str(num).zfill(4)
                print(num, f, newDestinationFolder+"/"+renameFilename+f_ext)
                os.rename(f, newDestinationFolder+"/"+renameFilename+f_ext)


# args = sys.argv
for filename in glob.glob(targetDir + "*.pdf"):
    print(filename)
# if len(args) > 1:
#     file = args[1]
#     print(file)
    # convert(file, outputDir)
    convert(filename, targetDir, outputDir)
    print(" ")
