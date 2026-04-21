from pydantic import BaseModel, Field, field_validator, ValidationError

class Person(BaseModel):
    name :str   = Field(default="Muster")
    alter :int  = Field(default=20,ge=18,le=50)

    model_config = {"validate_assignment": True}