"""Module providing delivery fee api."""

from fastapi import FastAPI
from src.deliveryFee.router import deliveryFeeRouter

app = FastAPI()

app.include_router(deliveryFeeRouter)
