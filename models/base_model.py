#!/usr/bin/python3
"""Module BaseModel
"""


from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel class
    """

    def __init__(self, *args, **kwargs):
        """Constructor of the BaseModel class
            Args:
                *args: pointer to an argument list
                **kwargs: double pointer to a dictionary: key/value
        """
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if "__" not in key:
                    if key == "created_at" or key == "updated_at":
                        date = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, key, date)
                    else:
                        setattr(self, key, date)

    def __str__(self):
        """Returns [<clase name>] (<self.id>) <self.__dict__>
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """Updates updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__
        """
        dict_new = self.__dict__.copy()
        dict_new.update({"__class__": self.__class__.__name__})
        dict_new.update({"created_at": datetime.isoformat(self.created_at)})
        dict_new.update({"updated_at": datetime.isoformat(self.updated_at)})
        return dict_new
