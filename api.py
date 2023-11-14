import io
import uuid
from dotenv import load_dotenv
import os

from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.responses import StreamingResponse
from queries.lmql_queries import generate_code, synthesize_data
from rich import print

load_dotenv()

MODEL=os.getenv("MODEL")




def execute_generation():
    file_data = None
    with open('./sample.py', 'r') as openfile:
        content = openfile.read().strip()
        result = generate_code(pydantic_schemas=content,used_model=f"openai/{MODEL}")
        # result = synthesize_data()
        print(result.prompt)
        file_data = result.prompt
    rand_id = str(uuid.uuid4())

    with open(f'./created_files/{rand_id}.py', 'w') as outfile:
        outfile.write(file_data)

async def handle_generation(file_data:str):
    result = await generate_code(pydantic_schemas=file_data,used_model=f"openai/{MODEL}")
    return result.prompt

app = FastAPI()


@app.post("/generate")
async def root(file: UploadFile):
    if file.content_type != "text/x-python":
        raise HTTPException(400, detail="Invalid document type")
    contents = await file.read()
    data = contents.decode()
    result = await handle_generation(file_data=data)
    result = result.split('Only use utf-8 characters!')[1].strip()
    result = result.replace('@app .','@app.')
    result = result.replace('$$','')
    result = result.replace(' (','(')
    result = result.replace('\n @','\n@')
    result = result.replace('\n  @','\n@')
    result = result.replace('\n   @','\n@')
    result = result.replace('\n    @','\n@')
    result = result.replace('\n     @','\n@')


    # Convert the string to bytes
    byte_data = result.encode("utf-8")

    # Create a StreamingResponse
    response = StreamingResponse(iter([byte_data]), media_type="text/x-python")

    # Set a filename for the response
    response.headers["Content-Disposition"] = 'attachment; filename="output.py"'

    return response
