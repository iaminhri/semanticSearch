import os
from pydub import AudioSegment
import glob

def checkForFiles(directory):
    video_extensions = ('.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.mpeg')

    for file in os.listdir(directory):
        if file.lower().endswith(video_extensions):
            return True
    return False

def getAudiosByDirectory(videoDir, extensionList):
    os.chdir(videoDir)

    for extension in extensionList:
        for video in glob.glob(extension):
            audioFileName = os.path.splitext(os.path.basename(video))[0] + '.wav'
            AudioSegment.from_file(video).export("../audio/"+audioFileName, format="wav")

def getAudiosByIndex(videoDir, extensionList, startIndex):
    os.chdir(videoDir)

    videoFiles = [file for file in os.listdir(videoDir) if file.startswith('video') and file.endswith('.mp4') and int(file[5:-4]) >= startIndex]
    print(videoFiles)

    videoFiles.sort()
    print(videoFiles)

    print("Audio Directory: ", os.getcwd())

    for video in videoFiles:
        audioFileName = os.path.splitext(os.path.basename(video))[0] + '.wav'
        print("audio filename: ", os.path.splitext(os.path.basename(video))[0] + '.wav')
        AudioSegment.from_file(video).export("/vol/web/media/audio/"+audioFileName, format="wav")
        # AudioSegment.from_file(video).export("../audio/"+audioFileName, format="wav")

def deleteVideos(videoDir):
    fileNames = os.listdir(videoDir)  
    for file in fileNames:
        file_path = os.path.join(videoDir, file)  

        if os.path.isfile(file_path):  
            os.remove(file_path)  
            print(f"Deleted file: {file_path}")
        else:
            print(f"Skipped non-file: {file_path}")

