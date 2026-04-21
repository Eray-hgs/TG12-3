from pydantic import BaseModel, Field, field_validator, ValidationError

class Auto(BaseModel):
    marke:str = Field(default="unbekannt",min_lenght=2,max_lenght=20)
    baujahr:int =Field(default=2000,ge=1950, le=2025)
    ps:int  =Field(default=50,ge=20,le=300)

    model_config = {"validate_assignment": True}