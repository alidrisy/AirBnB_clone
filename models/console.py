#!/usr/bin/python3
"""Define HBNBCommand class"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Class for he command interpreter"""
    prompt = "(hbnb)"

    def do_EOF(self, line):
        """EOF command to exit the program
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
