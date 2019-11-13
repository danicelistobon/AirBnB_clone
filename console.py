#!/usr/bin/python3
"""Module of the command interpreter
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class contains the entry point of the command interpreter
    """
    prompt = '(hbnb) '

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
