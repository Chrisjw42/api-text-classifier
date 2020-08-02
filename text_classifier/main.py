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
    """Simple root returner for debugging

    :return: hello world dict
    :rtype: dict
    """
    return {"Hello": "World"}

@app.post("/assess_text")
def assess_text(request: AssessmentRequest):
    """Main assessment function, takes text and does the magic.

    :param request: main reqeust object, declaring this explicity gives editor support.
    :type request: AssessmentRequest
    :return: result of assessment
    :rtype: dict
    """

    return {"passed_text": request.text, "morphed_text":request.text.upper()}