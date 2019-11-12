#!/usr/bin/python3
"""Module to create an unique FileStorage instance for your aplication
"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
