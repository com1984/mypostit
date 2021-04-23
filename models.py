import json

def loadJSONDB():
    with open('stickynote_db.json') as f:
        return json.load(f)

def saveJSONDB(notes):
    with open('stickynote_db.json', 'w') as f:
        json.dump(notes, f)
