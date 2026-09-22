from decimal import Decimal

from pydantic import BaseModel


class InventoryItemResponse(BaseModel):
    product_id: int
    product_name: str
    sku: str
    quantity: int
    price: Decimal
    stock_value: Decimal

    class Config:
        from_attributes = True


class InventorySummaryResponse(BaseModel):
    total_products: int
    total_units: int
    total_stock_value: Decimal