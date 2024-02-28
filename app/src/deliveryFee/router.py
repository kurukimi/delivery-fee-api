import logging
from fastapi import APIRouter, HTTPException

from src.deliveryFee.services.deliveryFeeService import calculateDeliveryFee
from src.deliveryFee.models.deliveryInfo import DeliveryInfo

deliveryFeeRouter = APIRouter()

logging.basicConfig(level=logging.INFO)


@deliveryFeeRouter.post("/delivery_fee")
async def deliveryFee(deliveryInfo: DeliveryInfo):
    try:
        delivery_fee = calculateDeliveryFee(
                                            deliveryInfo.cart_value,
                                            deliveryInfo.delivery_distance,
                                            deliveryInfo.number_of_items,
                                            deliveryInfo.time
        )
        return {"delivery_fee": delivery_fee}
    except ValueError as ve:
        logging.error(f"ValueError occurred: {ve}")
        raise HTTPException(status_code=400, detail="Invalid input data")
    except Exception as e:
        logging.error(e)
