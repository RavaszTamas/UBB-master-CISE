Implement CRUD functions for the Pydantic schemas below with FastAPI using a Redis database!
class Printer(BaseModel):
    id: str
    name: str

class PrinterMaterial(BaseModel):
    name: str
    printer_id: str
Strictly include the program code! Add a 'get' and 'get_all' endpoint as well besides the 'put', 'delete' and 'update' endpoints! The 'get_all' method should use accurate Redis calls! Be specific as you can be even in text formatting! Only use utf-8 characters!
 from fastapi import FastAPI, HTTPException
import redis
from pydantic import BaseModel

app = FastAPI()

# Connect to Redis database
r = redis.StrictRedis(host='localhost', port=6379, db=0, charset="utf-8", decode_responses=True)

class Printer(BaseModel):
     id: str
    name: str

class PrinterMaterial(BaseModel):
    name: str
    printer_id: str

@app.post("/printer")
async def create_printer(printer: Printer):
    r.set(printer.id, printer.json())
    return printer

@app.get("/printer/{id}")
async def  get_printer(id: str):
    printer = r.get(id)
    if printer:
        return printer
    else:
        raise HTTPException(status_code=404, detail="Printer not found")

@app.get("/printers")
async def get_all_printers():
    printers = []
    for key in r.scan_iter(" printer:*"):
        printer = r.get(key)
        printers.append(printer)
    return printers

@app.put("/printer/{id}")
async def update_printer(id: str, printer: Printer):
    if r.exists(id):
        r.set(id, printer.json())
        return printer
    else:
        raise HTTPException (status_code=404, detail="Printer not found")

@app.delete("/printer/{id}")
async def delete_printer(id: str):
    if r.exists(id):
        r.delete(id)
        return {"message": "Printer successfully deleted"}
    else:
        raise HTTPException(status_code=404, detail="Printer not found ")

@app.delete("/printer/{id}")
async def delete_printer(id: str):
    if r.exists(id):
        r.delete(id)
        return {"message": "Printer successfully deleted"}
    else:
        raise HTTPException(status_code=404, detail="Printer not found")$$
