#!/usr/bin/python3
""" User Module """
from models.base_model import BaseModel


class User(BaseModel):
    """
    The User Class

    Attributes:
        email = string
        password = string
        first_name = string
        last_name = string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
