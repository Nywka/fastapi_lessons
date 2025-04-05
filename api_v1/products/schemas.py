from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    name: str
    description: str
    price: int


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class product_update(ProductCreate):
    pass


class product_update_partial(ProductCreate):
    name: str | None = None
    description: str | None = None
    price: int | None = None
