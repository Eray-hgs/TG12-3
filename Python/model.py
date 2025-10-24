from pydantic import BaseModel, Field, field_validator, ValidationError

class Spieler(BaseModel):
    name        : str = Field(default = "Name Vergessen")
    jahrgang    : int = Field(default =2000, gt=1980,le=2007)
    staerke     : int = Field(default =5, gt=0,lt=11)
    torschuss   : int = Field(default =5, gt=0,lt=11)
    motivation  : int = Field(default =5, gt=0,lt=11)

    model_config = {"validate_assignment": True}

s = Spieler(name="Lukas",jahrgang=2006,staerke=10,torschuss=10,motivation=1)
print(s)
print(s.model_dump())