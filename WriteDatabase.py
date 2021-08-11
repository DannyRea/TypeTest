import pymongo
import random

client = pymongo.MongoClient("mongodb+srv://danielrea:LybxRhw6FgK76ex7@cluster0.8ajz4.mongodb.net/Project_0?retryWrites=true&w=majority")
db = client['TypeTest']
col = db['Users']



try:
    print("Connected to server!")
    
    
except Exception:
    print("Unable to connect to the server.")

def addStats(fname, lname, c, i, words,wpm):
    id = random.randrange(1,9999999)
    wordString= " ".join(x for x in words)
    statDoc = {
        "_id":id,
        "First Name":fname,
        "Last Name":lname,
        "Correct": c,
        "Incorrect":i,
        "Mispelled":wordString,
        "WPM":wpm
        }
    if db.collection.count_documents({ '_id': id }, limit = 1) == 0:
        col.insert_one(statDoc)
