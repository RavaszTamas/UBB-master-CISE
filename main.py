import datetime
import os
from queries.lmql_queries import synthesize_data
import json
import uuid
import shutil

from rich import print
from dotenv import load_dotenv
load_dotenv()


RESULT_FILE = "./results/results.json"
SAMPLE_LIMIT = 2000

def cleanup_str(string:str)->str:
    return string.replace("\u201c","\"").replace("\u201d","\"").replace("bytes: \\xe2\\x80\\x9c","\"").replace("bytes:\\xe2\\\\x80\\\\x9c","\"").replace("bytes:\\xe2\\x80\\x9c","\"").replace("bytes:\\xe2\\x80\\x9d","\"").replace("bytes:\\xe2\\\\x80\\\\x9d","\"")

for i in range(1465,SAMPLE_LIMIT):
    try:
        print(f"Current item {i} from {SAMPLE_LIMIT}")
        if i % 10 == 0:
            shutil.copyfile(RESULT_FILE, f"./results/results-{i}.json")

        data = synthesize_data()

        # print(data.prompt)

        data = data.prompt.split('Implement CRUD functions for the schemas above in Python with FastAPI using a Redis database! Strictly include the program code! Add a get and get all endpoint as well to the put delete and update endpoints!')
        # print(data)
        prompt = data[0].split('case!')[1]
        result = data[1]

        # print(prompt)
        # print(result)
        json_object = None


        # Opening JSON file
        with open('./results/results.json', 'r') as openfile:
        
            # Reading from json file
            json_object = json.load(openfile)
            the_id = str(uuid.uuid4())
            json_object['prompts'][the_id] = cleanup_str(prompt)
            json_object['results'][the_id] = cleanup_str(result)
            json_object['ids'].append(the_id)


        with open("./results/results.json", "w") as outfile:
            json.dump(json_object, outfile)

    except Exception as ex:
        print("ERROR!!")
        print(ex)
        print("Trying again")

    #stuff = '''\nCreate five Pydantic schemas to construction use case!\n\n    class  User(BaseModel):\n    \tid:  int\n    \tusername:  str\n\n    class  Product(BaseModel):\n    \tid:  int\n    \tname:  str\n \tprice:  float\n\n    class  Order(BaseModel):\n    \tid:  int\n    \tuser_id:  int\n\n    class  OrderItem(BaseModel):\n    \tid:  int\n    \torder_id:  int\n    \tproduct_id:  int\nImplement CRUD functionsfor the schemas above in Python with FastAPI using a Redis database! Strictly include the program code!\n\n    @index_router.delete( "/users/{user_id}" )\n    \tasync  def  delete_user(user_id:  int):\n      \t\tuser = await  User.get(user_id)\n    \t\tif  user:\n    \t\t\tawait  user.delete()\n    \t\t\treturn  { "message":  "User deleted successfully" }\n    \t\telse:\n    \t\t\traise  HTTPException(status_code=404, detail= "User not found")\n    \n    @index_router.post( "/products" )\n    \tasync  def  create_product(product:  Product):\n    \t\tnew_product = await  Product.create(**product.dict())\n    \t\treturn  new_product\n    \n    @index_router.put( "/orders/{order_id}" )\n    \tasync  def  update_order(order_id:  int, order:  Order):\n    \t\texisting_order =    await  Order.get(order_id)\n    \t\tif  existing_order:\n    \t\t\tawait  existing_order.update(**order.dict()).apply()\n    \t\t\treturn  { "message":  "Order updated successfully" }\n    \t\telse:\n        \t\t\traise  HTTPException(status_code=404, detail= "Order not found")\n    \n    @index_router.get( "/orders/{order_id}/items" )\n    \tasync  def  get_order_items(order_id:  int):\n    \t\torder = await    Order.get(order_id)\n    \t\tif  order:\n    \t\t\torder_items = await  OrderItem.filter(order_id=order_id).all()\n    \t\t\treturn  order_items\n    \t\telse:\n    \t\t\traise  HTTPException(status_code=404,detail= "Order not found")\n    \n    @index_router.patch( "/users/{user_id}" )\n    \tasync  def  update_user(user_id:  int, username:  str):\n    \t\texisting_user = await  User.get(user_id)\n    \t\tif    existing_user:\n    \t\t\tawait  existing_user.update(username=username).apply()\n    \t\t\treturn  { "message":  "User updated successfully" }\n    \t\telse:\n    \t\t\traise  HTTPException(status_code=404, detail= "User not found")\n    '''
    #string = "\nCreate five Pydantic schemas to mining use case!\n\n    class Mining:\n        id: int\n        name: str\n\n    class Miner:\n        id: int\n        name: str\n        mining_id: int\n\n    class MiningCompany:\n    \tid: int\n    \tname: str\n"
    #string = "'\nCreate five Pydantic schemas to sport betting use case!\n\n    class Bet(BaseModel):\n    \tid:  int\n    \tamount:  float\n\n    class User(BaseModel):\n    \tid:  int\n    \tusername:  str\n    \temail:  str\n\n    class Match(BaseModel):\n    \tid:  int\n    \thome_team:  str\n'"
