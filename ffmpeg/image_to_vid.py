import os

framerate = str(1)
imageSuffix = 'Slide'
imageRunningSeq = '%1d'
imageFormat = ".jpg"
outputVideoFile = "outputVid.mp4"

currentWorkingDirectory = os.getcwd()
imageDirectory = currentWorkingDirectory + "\\images\\Hi\\"

command = 'ffmpeg -framerate ' + framerate 
command += " -i " + imageDirectory + imageSuffix + imageRunningSeq + imageFormat
command += " " + outputVideoFile

print("This is the command:")
print(command)

print("Starting:")

os.system(command)