# https://fastapi.tiangolo.com/
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class AssessmentRequest(BaseModel):
    # Each of these attributes can be passed in the request body
    requester_name: Optional[str] = None
    text: str
    

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/assess_text")
def assess_text(request: AssessmentRequest):
    return {"passed_text": request.text, "morphed_text":request.text.upper()}