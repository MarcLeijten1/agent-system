from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, constr
from dotenv import load_dotenv
import os
import logging
from datetime import datetime
import uvicorn

app = FastAPI()

from fastapi import FastAPI, Request, HTTPException

app = FastAPI()

@app.post("/run")
async def run_task(request: Request):
    token = request.headers.get("x-api-key")
    if token != os.getenv("LOCAL_API_TOKEN"):
        raise HTTPException(status_code=403, detail="Invalid API token")
    data = await request.json()
    task = data.get("task")

    result = run_agent(task)
    return {"result": result}

# Load environment variables
load_dotenv()

# API security token from .env
API_KEY = os.getenv("LOCAL_API_TOKEN")

# Set up logging
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "agent_requests.log")
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(message)s",
)

# Placeholder agent logic
def run_agent(task: str) -> str:
    return f"Agent received task: {task}"

# Handle POST request
@app.post("/run")
async def run_task(request: Request):
    headers = request.headers
    if headers.get("x-api-key") != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

    data = await request.json()
    task = data.get("task")

    if not task:
        raise HTTPException(status_code=400, detail="Missing task")

    result = run_agent(task)
    logging.info(f"TASK: {task} | RESULT: {result}")
    return {"result": result}

if __name__ == "__main__":
    uvicorn.run("local_agent_api:app", host="127.0.0.1", port=8000, reload=True)
