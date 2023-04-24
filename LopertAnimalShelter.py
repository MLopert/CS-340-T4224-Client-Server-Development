from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:30993/AAC' % (username, password))
        # where xxxx is your unique port number
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.(Create)
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary    
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

# Create method to implement the R in CRUD. (Read)
    def read(self, search):
            if search is not None:
                if search:
                    searchResult = self.database.animals.find(search,{"_id":False})
                    return searchResult
            else:
                raise Exception("Nothing to search, because search parameter is empty")
                return False
# Create method to implement the U in CRUD (Update)
    def update(self, search, data):
            if search is not None:
                if search:
                    updateResult = self.database.animals.update_one(search, {'$set':data})
                    updateMatch = updateResult.modified_count #Modified count not currently being used
                    return updateResult.raw_result
            else:
                raise Exception("Nothing to update, because search parameter is empty")
                return False
# Create method to implement the D in CRUD (Delete)
    def delete(self, search):
            if search is not None:
                if search:
                    deleteResult = self.database.animals.delete_one(search)
                    deleteCount = deleteResult.deleted_count #Deleted count not currently being used
                    return deleteResult.raw_result
            else:
                raise Exception("Nothing to delete, because search parameter is empty")
                return False
