#!/usr/bin/python3
""" Review Module """
from models.base_model import BaseModel


class Review(BaseModel):
    """
    The Review Class

    Attributes:
        place_id = string
        user_id = string
        text = string
    """
    place_id = ""
    user_id = ""
    text = ""
