from pydantic import BaseModel, ConfigDict

class CategoriesSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    name: str

class CreateCategory(BaseModel):
    name: str

class UpdCategory(BaseModel):
    name: str | None = None