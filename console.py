#!/usr/bin/python3
"""Module of the command interpreter
"""


import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class contains the entry point of the command interpreter
    """
    prompt = '(hbnb) '
    classes = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place',
               'Review']

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """EOF command to exit the program
        """
        return True

    def emptyline(self):
        """Does not execute anything when entering an empty line
        """
        pass

    def do_create(self, args):
        """Creates a new instance
        """
        arg = args.split()

        if len(arg) == 0:
            print("** class name missing **")
            return
        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            obj = eval(arg[0])()
            obj.save()
            print(obj.id)

    def do_show(self, args):
        """Prints the string representation of an instance
        """
        arg = args.split()

        if len(arg) == 0:
            print("** class name missing **")
            return
        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            print("** instance id missing **")
            return
        else:
            obj_id = str(arg[0] + "." + str(arg[1]))
            objs = models.storage.all()
            if obj_id not in objs.keys():
                print("** no instance found **")
                return
            else:
                print(objs[obj_id])

    def do_destroy(self, args):
        """Deletes an instance
        """
        arg = args.split()

        if len(arg) == 0:
            print("** class name missing **")
            return
        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            print("** instance id missing **")
            return
        else:
            obj_id = str(arg[0] + "." + str(arg[1]))
            objs = models.storage.all()
            if obj_id not in objs.keys():
                print("** no instance found **")
                return
            else:
                del(objs[obj_id])
                models.storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances
        """
        arg = args.split()
        objs = models.storage.all()
        printer = []

        if len(arg) == 0:
            for value in objs.values():
                printer.append(str(value))
        elif arg[0] in self.classes:
            for key, value in objs.items():
                if arg[0] in key:
                    printer.append(str(value))
        else:
            print("** class doesn't exist **")
            return
        print(printer)

    def do_update(self, args):
        """Updates an instance by adding or updating attribute
        """
        arg = args.split()

        if len(arg) == 0:
            print("** class name missing **")
            return
        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            print("** instance id missing **")
            return
        elif len(arg) == 2:
            print("** attribute name missing **")
            return
        elif len(arg) == 3:
            print("** value missing **")
            return
        else:
            obj_id = str(arg[0] + "." + str(arg[1]))
            objs = models.storage.all()
            if obj_id not in objs.keys():
                print("** no instance found **")
                return
            else:
                obj = objs.get(obj_id)
                setattr(obj, arg[2], arg[3][1:-1])
                models.storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
