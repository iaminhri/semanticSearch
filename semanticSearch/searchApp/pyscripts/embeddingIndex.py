import txtai
import json 

def loadTranscriptData(filePath):
    transcript_dict = {}

    with open(filePath, "r", encoding='utf-8') as f:
        transcript_dict = json.load(f)
    return transcript_dict

# def embeddingIndex(transcripts):
#     embedding_data = []
    
#     for key in transcripts:
#         transcript_entry = transcripts[key]['transcripts']

#         for segment in transcript_entry:
#             embedding_data.append((key, segment['text'], None)) # id, text, none
            
#     outputFile = "/Users/hridoyrahman/Desktop/COSC 4F90/SemanticVideoSearch/semanticSearch/media/embedding_data.json"
#     with open(outputFile, 'w', encoding='utf-8') as f:
#         json.dump(embedding_data, f, indent=2, ensure_ascii=False)

#     return embedding_data

# def embeddingIndex(transcripts):
#     transcriptData = []

#     for key in transcripts:
#         transcript_entry = transcripts[key]

#         for transcript in transcript_entry["transcripts"]:

#             transcriptData.append(
#                 (
#                     key,
#                     {
#                         "text": transcript["text"],
#                         "caption": transcript["captions"],
#                         "metadata": {
#                             "video_title": transcript_entry["metaData"]["video_title"], 
#                             "source": transcript_entry["metaData"]["source"]
#                         },
#                     }
#                     ,
#                     None
#                 )
#             )

#     outputFile = "/Users/hridoyrahman/Desktop/COSC 4F90/SemanticVideoSearch/semanticSearch/media/transcriptData.json"
#     with open(outputFile, 'w', encoding='utf-8') as f:
#         json.dump(transcriptData, f, indent=2, ensure_ascii=False)

#     return transcriptData

def embeddingIndex(transcripts):
    transcriptData = []

    for key in transcripts:
        transcript_entry = transcripts[key]

        for transcript in transcript_entry["transcripts"]:
            transcriptData.append(({"text": transcript["text"],
                                    "caption": transcript["captions"], 
                                    "metadata": key}
                )
            )

    # outputFile = "/Users/hridoyrahman/Desktop/COSC 4F90/SemanticVideoSearch/semanticSearch/media/transcriptData.json"
    outputFile = "/vol/web/media/transcriptData.json"
    with open(outputFile, 'w', encoding='utf-8') as f:
        json.dump(transcriptData, f, indent=2, ensure_ascii=False)

    return transcriptData

def indexEmbeddingsMain():
    # load transcripts data from file
    filePath = "/vol/web/media/transcripts/transcript0.json"
    # filePath = "/Users/hridoyrahman/Desktop/COSC 4F90/SemanticVideoSearch/semanticSearch/media/transcripts/transcript0.json"

    transcript_dict = loadTranscriptData(filePath=filePath)

    # loading necessary data to embeddingsData
    transcriptData = embeddingIndex(transcript_dict)

    # print(json.dumps(embeddingData, indent=2))

    # Indexing embeddings
    embeddings = txtai.embeddings.Embeddings({
            "method": "transformers", 
            "content": True,
            "hybrid": True,
            "indexes": {
                "text": {
                    "path": "sentence-transformers/all-MiniLm-L6-v2",
                    "columns": {
                        "text": "text"
                    }
                },
                "captions": {
                    "path": "sentence-transformers/all-MiniLm-L6-v2",
                    "columns": {
                        "text": "caption"
                    }
                }
            }
        }
    )

    embeddings.index(embeddingIndex(transcript_dict))

    embeddings.save("/vol/web/media/embeddings/")
    # embeddings.save("/Users/hridoyrahman/Desktop/COSC 4F90/SemanticVideoSearch/semanticSearch/media/embeddings/")