
import glob
import json
import re

jsonFiles = [f for f in glob.glob("*.json")]

for jsonFile in jsonFiles:
    with open(jsonFile, 'r+') as f:
        data = json.load(f)
        
        data['image'] = re.sub("UPDATE", "CID", data['image'])

        del data['dna']
        del data['edition']
        del data['date']
        del data['compiler']
        
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        
        f.truncate()     # remove remaining part

