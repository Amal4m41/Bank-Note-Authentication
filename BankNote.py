from pydantic import BaseModel
#This class describes Bank notes independent features
class BankNote(BaseModel):
    variance:float
    skewness:float 
    curtosis:float
    entropy:float