from fastapi import APIRouter, HTTPException, Query

from .storage import get_customers_storage, get_orders_storage, get_products_storage
from .schema import CustomerCreateSchema, CustomerUpdateSchema, Customer, Order, Product

router = APIRouter()


CUSTOMERS_STORAGE = get_customers_storage()
ORDER_STORAGE = get_orders_storage()
PRODUCT_STORAGE = get_products_storage()


@router.get("/customers")
async def get_customers() -> list[Customer]:
    return list(get_customers_storage().values())


@router.get("/customers/{customer_id}")
async def get_customer(customer_id: int) -> Customer:
    try:
        return CUSTOMERS_STORAGE[customer_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Customer with ID={customer_id} does not exist."
        )


@router.patch("/customers/{customer_id}")
async def update_customer(
    customer_id: int, updated_customer: CustomerUpdateSchema
) -> Customer:
   pass


@router.delete("/customers/{customer_id}")
async def delete_customer(customer_id: int) -> None:
    try:
        del CUSTOMERS_STORAGE[customer_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Customer with ID={customer_id} does not exist."
        )


@router.post("/customers/")
async def create_customer(customer: CustomerCreateSchema) -> Customer:
    index = len(CUSTOMERS_STORAGE)
    CUSTOMERS_STORAGE[index] = Customer(id=index, **customer.dict())
    return CUSTOMERS_STORAGE[index]

@router.get("/orders")
async def get_orders() -> list[Order]:
    return list(get_orders_storage().values())

@router.get("/orders/{order_id}")
async def get_order(order_id: int) -> Order:
    return ORDER_STORAGE[order_id]

@router.get("/products")
async def get_products() -> list[Product]:
    return list(get_products_storage().values())

@router.get("products/{product_id}")
async def get_product(product_id: int) -> Product:
    return PRODUCT_STORAGE[product_id]