from pydantic import BaseModel, ConfigDict

class StudentRequest(BaseModel):
    full_name: str
    class_name: str
    email: str
    phone_number: str

class StudentResponse(BaseModel):
    id: int
    full_name: str
    class_name: str
    email: str
    phone_number: str

    model_config = ConfigDict(from_attributes=True)

