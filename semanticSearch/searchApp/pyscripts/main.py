import django
from django.conf import settings

from exportAudios import checkForFiles, getAudiosByIndex, deleteVideos
from transcribe import transcribe
from embeddingIndex import indexEmbeddingsMain
from merge import mergeFiles
import os

def updateStatus(counterDir, startCount, status):
    with open(counterDir, 'r') as file:
        line = file.read().strip()
        parts = line.split(',')

        if int(parts[0]) == startCount:
            with open(counterDir, 'w') as out:
                newStr = str(startCount) + "," + status
                out.write(newStr)

def main():
    data = "The videos has been embedded."
    extensionList = ('*.mp4', '*.flv')
    print("Current Working Dir: ", os.getcwd())
    error = "No Videos Found!!!"

    # For Docker Container setup
    videoPath = "/vol/web/media/media/" 
    dataD = '/vol/web/media/data/counter.txt'
    path1 = '/vol/web/media/transcripts/transcript0.json'
    path2 = '/vol/web/media/transcripts/transcript1.json'

    # videoPath = "/Users/hridoyrahman/Desktop/COSC 4F90/SemanticVideoSearch/semanticSearch/media/media/"
    # dataD = "/Users/hridoyrahman/Desktop/COSC 4F90/SemanticVideoSearch/semanticSearch/media/data/counter.txt"
    # path1 = "/Users/hridoyrahman/Desktop/COSC 4F90/SemanticVideoSearch/semanticSearch/media/transcripts/transcript0.json"
    # path2 = "/Users/hridoyrahman/Desktop/COSC 4F90/SemanticVideoSearch/semanticSearch/media/transcripts/transcript1.json"

    with open(dataD, 'r') as counter:
        line = counter.read().strip()
        parts = line.split(',')
        startCount = int(parts[0])
        status = parts[1]

    if checkForFiles(videoPath) and status == "False":
        # getAudiosByDirectory(videoPath, extensionList)
        # extract audios from the videos based on the starting number
        print("getting the audios...")
        getAudiosByIndex(videoPath, extensionList, startCount)

        print("transcribing...")
        # transcribe the audios
        transcribe(startCount)

        if startCount > 1:
            mergeFiles(path1, path2)

        # mergeAndDumpJson()

        print("indexing...")
        # Indexing the vector embeddings.
        indexEmbeddingsMain()

        print("updating status...")
        updateStatus(dataD, startCount, "True")

        # deleteVideos(videoPath)

        return data
    else:
        return error

main()