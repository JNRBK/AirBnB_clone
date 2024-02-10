#!/usr/bin/python3
""" City Module """
from models.base_model import BaseModel


class City(BaseModel):
    """
    The City Class

    Attributes:
        name: string.
        state_id: string.
    """
    state_id = ""
    name = ""
