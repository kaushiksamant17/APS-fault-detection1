import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

#path of the csv file
DATA_FILE_PATH= "/config/workspace/aps_failure_training_set1.csv"

#database and collection name
DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"

if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"rows and columns: {df.shape}")

#convert dataframe to json so that we can dump these records in mongo db
    df.reset_index(drop = True , inplace = True)

#convert the dataframe to json file and store in json_record
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

#call the mongo client database and store in mongodb database
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)



