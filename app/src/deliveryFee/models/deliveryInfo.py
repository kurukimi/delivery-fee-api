from pydantic import BaseModel


class DeliveryInfo(BaseModel):
    cart_value: int
    delivery_distance: int
    number_of_items: int
    time: str = '2024-01-15T13:00:00Z'
