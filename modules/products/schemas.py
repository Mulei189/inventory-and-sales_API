from typing import Optional

from pydantic import BaseModel

class CreateProductSchema(BaseModel):
    name: str
    sku: str
    description: str | None = None
    price: float
    quantity: int = 0
    category_id: int

class UpdateProductSchema(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    quantity: int | None = None
    category_id: Optional[int] = None

class ProductResponse(BaseModel):
    id: int
    name: str
    sku: str
    description: str | None = None
    price: float
    quantity: int

    class Config:
        from_attributes = True