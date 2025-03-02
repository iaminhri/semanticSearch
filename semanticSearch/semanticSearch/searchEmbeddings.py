import txtai
import json

def loadTranscriptData(filePath):
    transcript_dict = {}

    with open(filePath, "r", encoding='utf-8') as f:
        transcript_dict = json.load(f)
        # print(json.dumps(transcript_dict, indent = 2, ensure_ascii = False))
    return transcript_dict

# Single Query
def searchInEmbeddingDB(query, embeddings):
    return embeddings.search(query, 3)

def timeToSeconds(timeStr):
    hours, minutes, seconds = map(int, timeStr.split(':'))
    return hours * 3600 + minutes * 60 + seconds

# Multiple Query
def searchInEmbeddingsDB_multiquery(query_list, embeddings):
    load_transripts = loadTranscriptData(filePath)
    formattedOutput = {}

    for query in query_list:
        # Find similar results in transcription index
        searchQuery = f"select id, text, caption, metadata, score from txtai where similar('{query}', 'text') and score >= 0.30"
        search_results = embeddings.search(searchQuery, 1)

        # Find similar results in caption data index
        capSearch2 = f"SELECT id, text, caption, metadata, score FROM txtai WHERE SIMILAR('{query}', 'captions') and score >= 0.30"
        capResult2 = embeddings.search(capSearch2, 1)

        # filtering caption results based on transcription data.
        uniqueCapResults = [cap for cap in capResult2 if not any(cap['text'] == sr['text'] for sr in search_results)]

        # Formatting to JSON output
        formattedOutput = exportOutput(search_results, load_transripts, formattedOutput, query)
        formattedOutput = exportOutput(uniqueCapResults, load_transripts, formattedOutput, query)
    
    # sys.stderr.write(len(query_list))
    # sys.stderr.write(query_list)

    for i in range(len(query_list) - 1):
        multiQuery = f"""select id, text, caption, metadata, score from txtai \
                                    where similar('{query_list[i]}', 'text') and  
                                    similar('{query_list[i+1]}', 'captions') and score >= 0.30"""
        multiQueryResults = embeddings.search(multiQuery, 1)

        uniqueMultiResults = [query for query in multiQueryResults if not any(query['text'] == sr['text'] for sr in search_results)]

        formattedOutput = exportOutput(multiQueryResults, load_transripts, formattedOutput, query_list[i], query_list[i+1])

    with open("Transcript.json", 'w', encoding='utf-8') as f:
        json.dump(formattedOutput, f, indent = 2, ensure_ascii = False)
    return formattedOutput

filePath = "/vol/web/media/transcripts/transcript0.json"
# filePath = "/Users/hridoyrahman/Desktop/COSC 4F90/SemanticVideoSearch/semanticSearch/media/transcripts/transcript0.json"

def exportOutput(search_results, load_transripts, formattedOutput, query1, query2 = ""):

    for result in search_results:
            # matched_id = str(result['id']).split("_")[0]
            matched_id = str(result['metadata'])

            matched_entry = load_transripts[matched_id]['transcripts']

            metaDataEntry = load_transripts[matched_id]['metaData']

            if matched_id not in formattedOutput:
                formattedOutput[matched_id] = {
                    "metaData": metaDataEntry,
                    "searchResult": []
                }
            
            for segment in matched_entry:
                if segment['text'] == result['text']:
                    formattedOutput[matched_id]["searchResult"].append({
                        'id': segment['id'],
                        "video_id": segment['video_id'],
                        'text': segment['text'],
                        'caption': segment['captions'],
                        'start_timestamp': timeToSeconds(segment['start_timestamp']),
                        'end_timestamp': timeToSeconds(segment['end_timestamp']),
                        'score': result['score'],
                        'searchKey': query1 if query2 == "" else query1 + "," + query2,
                    })
    return formattedOutput

def loadEmbeddings():
    embeddingsPath = "/vol/web/media/embeddings"
    # embeddingsPath = "/Users/hridoyrahman/Desktop/COSC 4F90/SemanticVideoSearch/semanticSearch/media/embeddings/"
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

    try:
        embeddings.load(embeddingsPath)
    except Exception as e:
        print("Embeddings file not found", e)
    
    return embeddings