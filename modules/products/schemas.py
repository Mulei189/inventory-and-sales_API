from typing import Optional

from pydantic import BaseModel, Field

class CreateProductSchema(BaseModel):
    name: str
    sku: str
    description: str | None = None
    price: float
    quantity: int = 0
    category_id: int
    low_stock_threshold: int = Field(default=5, gt=0)

class UpdateProductSchema(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    quantity: int | None = None
    category_id: Optional[int] = None
    low_stock_threshold: int | None = Field(default=None, gt=0)

class ProductResponse(BaseModel):
    id: int
    name: str
    sku: str
    description: str | None = None
    price: float
    quantity: int
    low_stock_threshold: int

    class Config:
        from_attributes = True