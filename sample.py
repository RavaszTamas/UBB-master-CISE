class Printer(BaseModel):
    id: str
    name: str

class PrinterMaterial(BaseModel):
    name: str
    printer_id: str