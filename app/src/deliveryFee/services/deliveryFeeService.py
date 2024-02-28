from datetime import datetime
from src.deliveryFee.constants.constants import *
from math import ceil


def calculateDeliveryFee(cartValue: int,
                         distance: int,
                         numberOfItems: int,
                         time: str
                         ):
    if cartValue >= FREE_DELIVERY_MIN_CART_VALUE:
        return 0
    totalBeforeRushMult = cartValueFee(cartValue) + \
        deliveryDistanceFee(distance) + \
        itemFee(numberOfItems) + bulkItemFee(numberOfItems)
    total = rushTimeFee(totalBeforeRushMult, time)
    return min(MAX_DELIVERY_FEE, total)


def cartValueFee(cartValue: int):
    if cartValue >= NO_SURCHARGE_MIN_CART_VALUE:
        return 0
    return NO_SURCHARGE_MIN_CART_VALUE - cartValue


def deliveryDistanceFee(distance: int):
    if distance <= BASE_DELIVERY_DISTANCE:
        return BASE_DELIVERY_FEE
    additionalDistanceFee = ceil(
        (distance - BASE_DELIVERY_DISTANCE) / ADDITONAL_DISTANCE
        ) * ADDITIONAL_DISTANCE_SURCHARGE
    return BASE_DELIVERY_FEE + additionalDistanceFee


def itemFee(numItems: int):
    if numItems <= BASE_ITEM_LIMIT:
        return 0
    additionalItemFee = (numItems - BASE_ITEM_LIMIT) \
        * ADDITIONAL_ITEM_SURCHARGE
    return additionalItemFee


def bulkItemFee(numItems: int):
    if numItems <= BULK_ITEM_LIMIT:
        return 0
    return BULK_ITEM_SURCHARGE


def rushTimeFee(fee: int, date: str):
    dateTime = datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
    dayOfWeek = dateTime.isoweekday()
    hour = dateTime.hour
    if dayOfWeek == RUSH_DAY_OF_WEEK and \
            RUSH_HOUR_START <= hour <= RUSH_HOUR_END:
        return fee * RUSH_TIME_MULTIPLIER
    return fee
