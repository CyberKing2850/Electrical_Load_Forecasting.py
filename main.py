from fastapi import FastAPI, BackgroundTasks
import asyncio
import extract_data_point as edp
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
load_dotenv()
import os
import time

app = FastAPI()

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = "DataPoints"
COLLECTION_NAME = "CSVs"

# Connect to MongoDB
client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

@app.get("/cron_collect/")
async def cron_job():
    print("Running cron job...")
    csv_str = edp.extract_data_point()
    print(csv_str)
    item_doc={"csv_str":csv_str,"timestamp":time.time()}
    result = await collection.insert_one(item_doc)
    print({"id": str(result.inserted_id), **item_doc})
    return "success"
    


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
