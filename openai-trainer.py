import ast
import json
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client = OpenAI()

def is_valid_python(code):
   try:
       ast.parse(code)
   except SyntaxError as e:
       return False
   return True


def reformat():
    formated = []
    with open('./results/results-final.json', 'r') as openfile:

        # Reading from json file
        json_object = json.load(openfile)
        count = 0
        for an_id in json_object["ids"]:
        
            prompt = json_object["prompts"][an_id].lstrip()
            completion = json_object["results"][an_id].lstrip()
            message = {'messages':[{"role":"system","content":"You are a programming aiding chatbot that generates FastAPI endpoints using Pydantic schemas for different use cases! You not only suggest code to be implemented but you are also doing the programming as well!"},{"role":"user","content":prompt},{"role":"assistant","content":completion}]}

            formated.append(message)
            if not is_valid_python(completion):
                count = count + 1
                #print("invalid")
        print(count)
    with open("./formated.jsonl", "w") as outfile:
        for entry in formated:
            json.dump(entry, outfile)
            outfile.write('\n')

def upload_file():
    client.files.create(
    file=open("formated.jsonl", "rb"),
    purpose="fine-tune"
    )

def fine_tune():
    client.fine_tuning.jobs.create(
    training_file="formated.jsonl", 
    model="gpt-3.5-turbo"
    )

reformat()
#upload_file()
#fine_tune()