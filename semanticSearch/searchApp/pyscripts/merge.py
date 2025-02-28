import json

def mergeFiles(path1, path2):
    with open(path1, 'r', encoding='utf-8') as p1:
        data1 = json.load(p1)

    with open(path2, 'r', encoding='utf-8') as p2:
        data2 = json.load(p2)

    merged_dict = {str(i): value for i, value in enumerate(list(data1.values()) + list(data2.values()))}
    
    with open(path1, 'w', encoding='utf-8') as writable:
        json.dump(merged_dict, writable, indent=2)
