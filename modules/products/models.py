from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Numeric
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from core.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)

    name = Column(String(255), nullable=False)

    sku = Column(String(100), unique=True, nullable=False)

    description = Column(String)

    price = Column(Numeric(10, 2), nullable=False)

    quantity = Column(Integer, default=0)

    created_at = Column(DateTime, server_default=func.now())

    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    