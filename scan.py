from pdf2image import convert_from_path
import os
import sys
import time
import glob


outputDir = "output/"


def convert(file, outputDir):
    outputDir = outputDir + str(round(time.time())) + '/'
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    pages = convert_from_path(file, 500)
    counter = 1
    for page in pages:
        myfile = outputDir + 'output' + str(counter) + '.jpg'
        counter = counter + 1
        page.save(myfile, "JPEG")
        print(myfile)


args = sys.argv
for filename in glob.glob("*.pdf"):
    print(filename)
# if len(args) > 1:
#     file = args[1]
#     print(file)
    # convert(file, outputDir)
    convert(filename, outputDir)
