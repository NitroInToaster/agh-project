from functools import lru_cache

from .schema import Customer, Order, Product

CustomerStorageType = dict[int, Customer]
OrdersStorageType = dict[int, Order]
ProductsStorageType = dict[int, Product]

CUSTOMERS: CustomerStorageType = {}
ORDERS: OrdersStorageType = {
    0: Order(
        customer_id=1,
        order_items=[1],
        order_id=1,
    ),
    1: Order(
        customer_id=2,
        order_items=[0,2,3],
        order_id=2,
    ),
}

PRODUCTS: ProductsStorageType = {
    0: Product(name="Item", price=1.0, description="Lorem Ipsum", id=0),
    1: Product(name="Item2", price=2.2, description="Lorem Ipsum", id=1),
    2: Product(name="Item3", price=3.3, description="Lorem Ipsum", id=2),
    3: Product(name="Item4", price=4.4, description="Lorem Ipsum", id=3),
}


@lru_cache(maxsize=1)
def get_customers_storage() -> CustomerStorageType:
    return CUSTOMERS

@lru_cache(maxsize=1)
def get_orders_storage() -> OrdersStorageType:
    return ORDERS

@lru_cache(maxsize=1)
def get_products_storage() -> ProductsStorageType:
    return PRODUCTS