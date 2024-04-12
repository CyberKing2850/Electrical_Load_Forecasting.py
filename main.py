from fastapi import FastAPI, BackgroundTasks
import asyncio
import extract_data_point as edp
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
load_dotenv()
import os

app = FastAPI()

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = "DataPoints"
COLLECTION_NAME = "CSVs"

# Connect to MongoDB
client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

async def cron_job():
    while True:
        # Replace this with the task you want to run periodically
        print("Running cron job...")
        csv_str = edp.extract_data_point()
        print(csv_str)
        item_doc={"csv_str":csv_str}
        result = await collection.insert_one(item_doc)
        print({"id": str(result.inserted_id), **item_doc})
        await asyncio.sleep(860)

@app.get("/start_cron/")
async def start_cron(background_tasks: BackgroundTasks):
    background_tasks.add_task(cron_job)
    return {"message": "Cron job started"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
