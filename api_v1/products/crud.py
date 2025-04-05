from sqlalchemy import Select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Product

from .schemas import ProductCreate, product_update, product_update_partial


async def get_products(session: AsyncSession) -> list[Product]:
    start = Select(Product).order_by(Product.id)
    result: Result = await session.execute(start)
    products = result.scalars().all()
    return list(products)


async def get_product(
    session: AsyncSession,
    product_Id: int,
) -> Product | None:
    return await session.get(Product, product_Id)


async def create_product(
    session: AsyncSession,
    product_in: ProductCreate,
) -> Product:
    product = Product(**product_in.model_dump())
    session.add(product)
    await session.commit()
    # await session.refresh()
    return product


async def update_product(
    session: AsyncSession,
    product: Product,
    product_update: product_update | product_update_partial,
    partial: bool = False,
) -> Product:
    for name, value in product_update.model_dump(exclude_unset=partial).items():
        setattr(product, name, value)
    await session.commit()
    return product


async def delete_product(
    session: AsyncSession,
    product: Product,
):
    await session.delete(product)
    await session.commit()
