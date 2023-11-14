import redis
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
app = FastAPI()

# Connect to Redis database
r = redis.Redis(host='localhost', port=6379, db=0)

# Printer schema
class Printer(BaseModel):
    id: str
    name : str

# PrinterMaterial schema
class PrinterMaterial(BaseModel):
    name: str
    printer_id: str

# Create a new printer
@app.post("/printer/")
def create_printer(printer: Printer):
    r.set(printer.id, printer.name)
    return printer

# Get a specific printer
@app.get("/printer/{id}")
def get_printer(id: str):
    name = r.get(id)
    if name is None:
        raise HTTPException(status_code=404, detail="Printer not found")
    return {"id": id, "name": name}

# Get all printers
@app.get("/printer/all ")
def get_all_printers():
    printers = []
    for key in r.scan_iter():
        name = r.get(key)
        printers.append({"id": key, "name": name})
    return printers

# Update a printer
@app.put("/printer/{id}")
def update_printer(id: str, printer:  Printer):
    if r.exists(id):
        r.set(id, printer.name)
        return {"id": id, "name": printer.name}
    else:
        raise HTTPException(status_code=404, detail="Printer not found")

# Delete a printer
@app.delete("/printer/{id}")
def delete_printer(id:         str):
    if r.exists(id):
        r.delete(id)
        return {"message": "Printer successfully deleted"}
    else:
        raise HTTPException(status_code=404, detail="Printer not found")

# Create a new printer material
@app.post("/printer/material/")
def create_printer_material(material: PrinterMaterial):
    r.set(material.printer_id, material.name)
    return material

# Get a specific printer material
@app.get("/printer/material/{printer_id}")
def get_printer_material(printer_id: str):
    name = r.get(printer_id)
    if name is None:
        raise HTTPException(status_code=404 , detail="Printer material not found")
    return {"printer_id": printer_id, "name": name}

# Get all printer materials
@app.get("/printer/material/all")
def get_all_printer_materials():
    materials = []
    for key in r.scan_iter():
        name = r.get(key)
        materials.append ({"printer_id": key, "name": name})
    return materials

# Update a printer material
@app.put("/printer/material/{printer_id}")
def update_printer_material(printer_id: str, material: PrinterMaterial):
    if r.exists(printer_id):
        r.set(printer_id, material.name)
        return {"printer_id": printer_id, "name": material.name}
    else:
        raise HTTPException(status_code=404, detail="Printer material not found")

# Delete a printer material
@app.delete("/printer/material/{printer_id}")
def delete_printer_material(printer_id: str):
    if r.exists(printer_id):
        r.delete(printer_id)
        return {"message": "Printer material successfully deleted"}
    else:
        raise HTTPException(status_code=404, detail="Printer material not found")