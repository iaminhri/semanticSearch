import whisper_timestamped as whisper
import os
import json 
import csv 
import logging
from videotoimages import extract_frame
import random 
from imagecaption import generateCaptions

logging.basicConfig(level=logging.INFO)

# filePath = "/vol/web/media/audio/" # container
filePath = "/Users/hridoyrahman/Desktop/COSC 4F90/SemanticVideoSearch/semanticSearch/media/audio/"

print("transcribe: ", os.getcwd())

fileNames = os.listdir(filePath)
for files in fileNames:
    print(files)

model_id = "tiny"

def loadMetaData(metaFilePath, startCount):
    metaDict = []

    with open(metaFilePath, 'r', encoding='utf-8') as csvFile:
        csvFile = csv.DictReader(csvFile)
        for idx, row in enumerate(csvFile):
            if idx >= (startCount-1):
                metaDict.append({
                    "video_id": 'video'+row['id'],
                    "name": row['name'],
                    "url": row['url'],
                    "source": row['source'],
                    "language": row['language'],
                    "filePath": row['file']
                })

    return metaDict

def transcribeTexts(model_id, startCount):
    logging.info("transcribeTexts function is being executed.")
    result = []

    fileNames = os.listdir(filePath)
    print(fileNames)

    # Filter and sort files sequentially (e.g., video1, video2, ...)
    sorted_files = sorted(
        [f for f in fileNames if f.startswith("video") and f.endswith((".wav")) and int(f[5:-4]) >= startCount],
        key=lambda x: int("".join(filter(str.isdigit, x)))  # Extract numeric part for sorting
    )
    
    model = whisper.load_model(model_id)

    for files in sorted_files:
        audioPath = filePath + "/" + files
        print(audioPath)

        audio = whisper.load_audio(audioPath)

        result.append(model.transcribe(audio, language="en"))
    
    # outputFileName = '/vol/web/media/data/model.json'
    outputFileName = "/Users/hridoyrahman/Desktop/COSC 4F90/SemanticVideoSearch/semanticSearch/media/data/model.json"
    with open(outputFileName, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    return result
    
def exportTranscript(result, meta, startCount):
    # Dictionary to store transcripts grouped by index
    transcripts_dict = {}
    videoPath = "/Users/hridoyrahman/Desktop/COSC 4F90/SemanticVideoSearch/semanticSearch/media/media/"

    for j in range(len(result)):
        resultIndex = result[j]
        transcripts = []  # List to hold all segments for current resultIndex

        metaData = {
            "video_id": f"{meta[j]['video_id']}",
            "video_title": f"{meta[j]['name']}",  
            "url": f"{meta[j]['url']}",
            "source": f"{meta[j]['source']}",
            "language": f"{meta[j]['language']}",
            "filePath": f"{meta[j]['filePath']}",
        }

        for i, segment in enumerate(resultIndex['segments']):
            start, end = segment['start'], segment['end']
            
            videoFileName = videoPath + f"{metaData['video_id']}.mp4"
            
            rand = random.random()
            if rand >= 0.8:
                extract_frame(videoFileName, start)
                imagePath = '/Users/hridoyrahman/Desktop/COSC 4F90/SemanticVideoSearch/semanticSearch/media/images/temp_frame.jpg'
                # image = Image.open(imagePath)
                frameCap = generateCaptions(imagePath)
                # caption = Caption()
                # frameCap = caption(image)
            else:
                frameCap = ""

            # Converting start and end times to hours, minutes, seconds
            start_h, start_m = divmod(int(start), 60)
            start_h, start_m = divmod(start_h, 60)

            end_h, end_m = divmod(int(end), 60)
            end_h, end_m = divmod(end_h, 60)

            # Timestamps formatted in HH:MM:SS
            start_timestamp = f"{start_h:02}:{start_m:02}:{int(start % 60):02}"
            end_timestamp = f"{end_h:02}:{end_m:02}:{int(end % 60):02}"

            # Append the transcript segment with timestamps to the list for current resultIndex
            transcripts.append({
                "id": f"{j}_{i}",  # Unique ID for each segment
                "video_id": f"{meta[j]['video_id']}",
                "start_timestamp": start_timestamp,
                "end_timestamp": end_timestamp,
                "text": segment['text'].strip(),
                "captions": frameCap,
            })

        # Store the transcripts in a dictionary under the key corresponding to the index
        transcripts_dict[j] = {
            "metaData": metaData,
            "transcripts": transcripts,
         }

    if startCount == 1:
        name = "transcript0.json"
    else:
        name = "transcript1.json"

    # outputFileName = f'/vol/web/media/transcripts/{name}'
    outputFileName = f'/Users/hridoyrahman/Desktop/COSC 4F90/SemanticVideoSearch/semanticSearch/media/transcripts/{name}'

    # Write the structured data to a JSON file
    with open(outputFileName, 'w', encoding='utf-8') as f:
        json.dump(transcripts_dict, f, indent=2, ensure_ascii=False)

def transcribe(startCount):
    try:
        # metaFilePath = "/vol/web/media/data/metaData.csv"
        metaFilePath = "/Users/hridoyrahman/Desktop/COSC 4F90/SemanticVideoSearch/semanticSearch/media/data/metaData.csv"

        metaData = loadMetaData(metaFilePath, startCount)
        result = transcribeTexts(model_id, startCount)
        exportTranscript(result, metaData, startCount)
    except Exception as e:
        logging.error(f"Error in transcribe: {e}")
        raise e
