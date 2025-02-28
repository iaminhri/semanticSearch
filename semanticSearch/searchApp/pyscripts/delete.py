import os

def deleteAudioFiles(targetDirectory):
    files = os.listdir(targetDirectory)

    audioFiles = [file for file in files if file.endswith('.wav')]

    for audio in audioFiles:
        audioPath = os.path.join(targetDirectory, audio)
        os.remove(audioPath)
