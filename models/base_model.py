#!/usr/bin/python3
"""
"""


from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    """

    def __init__(self):
        """
        """
        self.id = uuid4()
        self.created_at = datetime.now()
        self.update_at = datetime.now()

    def __str__(self):
        """
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """
        """
        self.update_at = datetime.now()

    def to_dict(self):
        """
        """
        dict_new = self.__dict__.copy()
        dict_new.update({"__class__": self.__class__.__name__})
        dict_new.update({"update_at": datetime.isoformat(self.update_at)})
        dict_new.update({"created_at": datetime.isoformat(self.created_at)})
        return dict_new
