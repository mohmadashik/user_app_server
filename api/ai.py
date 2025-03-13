from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from transformers import pipeline

# Initialize Router
router = APIRouter()

# Define Request Model
class AIRequest(BaseModel):
    prompt: str

# Load the model pipeline once (example: FLAN-T5)
generator = pipeline("text2text-generation", model="google/flan-t5-large")


def prepare_prompt(user_prompt: str) -> str:
    # Add a generic instruction, you can customize this
    return f"Answer the following question: {user_prompt}"

@router.post("/generate/")
async def generate_text(request: AIRequest):
    try:
        prepared_prompt = prepare_prompt(request.prompt)
        outputs = generator(prepared_prompt, max_length=200)
        return {"response": outputs[0]["generated_text"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))











# from fastapi import APIRouter, HTTPException
# from pydantic import BaseModel
# import requests

# from common import constants  # Assuming your constants file has the HF token

# # Initialize Router
# router = APIRouter()

# # Define Request Model
# class AIRequest(BaseModel):
#     prompt: str

# # Hugging Face settings
# HF_API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-small"
# HF_API_TOKEN = constants.HF_API_TOKEN  # Add this token to your constants.py

# headers = {
#     "Authorization": f"Bearer {HF_API_TOKEN}",
#     "Content-Type": "application/json"
# }

# @router.post("/generate/")
# async def generate_text(request: AIRequest):
#     try:
#         payload = {
#             "inputs": request.prompt,
#             "parameters": {
#                 "temperature": 0.7,
#                 "max_length": 200
#             }
#         }

#         response = requests.post(HF_API_URL, headers=headers, json=payload)

#         # Check for HTTP errors
#         if response.status_code != 200:
#             raise HTTPException(status_code=response.status_code, detail=response.json())

#         # Parse the response
#         result = response.json()

#         if isinstance(result, dict) and "error" in result:
#             raise HTTPException(status_code=500, detail=result["error"])

#         generated_text = result[0]["generated_text"]

#         return {"response": generated_text}

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))





# from fastapi import APIRouter, HTTPException
# from pydantic import BaseModel
# import openai

# from common import constants

# # Initialize Router
# router = APIRouter()

# # Define Request Model
# class AIRequest(BaseModel):
#     prompt: str

# client = openai.Client(api_key=constants.OPENAI_API_KEY)

# @router.post("/generate/")
# async def generate_text(request: AIRequest):
#     try:
#         response = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {'role':"user","content":request.prompt}
#             ]
#         )
#         return {"response": response.choices[0]["message"]["content"]}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
