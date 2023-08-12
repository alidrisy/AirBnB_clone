#!/usr/bin/python3
"""Define HBNBCommand class"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.city import City
import shlex
import ast


class HBNBCommand(cmd.Cmd):
    """Class for he command interpreter

    Args:
        prompt (str): the console prompt
        __model_dict (dict): dictionry of models
    """

    prompt = "(hbnb)"
    __model_dict = {'BaseModel': BaseModel, 'User': User, 'Review': Review}
    d = {'Place': Place, 'State': State, 'Amenity': Amenity, 'City': City}
    __model_dict.update(d)

    def onecmd(self, line):
        """Run command in style <class name>.command"""
        method_dict = {'all': self.do_all, 'count': self.do_count}
        d = {"show": self.do_show, 'destroy': self.do_destroy}
        method_dict.update(d)
        if line:
            if '.' in line and '(' in line and ')' in line:
                cls = line.split('.')
                cnd = cls[1].split('(')
                args = cnd[1].split(')')
                line = cnd[0] + ' ' + cls[0] + ' ' + args[0]
        r = super(HBNBCommand, self).onecmd(line)
        return r

    def do_count(self, value):
        """Retrieve the number of instances of a class"""
        dct = storage.all()
        x = 0
        for val in dct.values():
            if val.__class__.__name__ == value:
                x += 1
        print(x)

    def do_EOF(self, line):
        """EOF command to exit the program
        """
        return True

    def do_quit(self, line):
        """Exit the program
        """
        return True

    def help_create(self):
        """Print the documention of the command show"""
        print('Creates a new instance and prints the id.\n\
Usage: create <class name>\n')

    def do_create(self, line):
        """Creates a new instance and prints the id.
        """
        if not line:
            print("** class name missing **")
        else:
            modl = None
            if line in self.__model_dict.keys():
                modl = self.__model_dict[line]()
                print(modl.id)
                modl.save()
            else:
                print("** class doesn't exist **")

    def help_show(self):
        """Print the documention of the command show"""
        print('Prints the string representation of an instance based\
 on the class name and id.\n\
Usage: show <class name> <id>\n')

    def do_show(self, line):
        """Prints the string representation of an instance based\
on the class name and id.
        """
        if line:
            ret = cmd.Cmd.parseline(self, line)
            if ret[0] not in self.__model_dict.keys():
                print("** class doesn't exist **")
                return
            if ret[1] != '':
                dict1 = storage.all()
                key = ret[0]+'.'+ret[1]
                if key in dict1.keys() and dict1[key].id == ret[1]:
                    print(dict1[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class name missing **")

    def help_destroy(self):
        """Print the documention of the command destroy"""
        print('Deletes an instance based on the class name and id\n\
Usage: destroy <class name> <id>\n')

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        """
        if line:
            ret = ret = cmd.Cmd.parseline(self, line)
            if ret[0] not in self.__model_dict.keys():
                print("** class doesn't exist **")
                return
            if ret[1] != '':
                dict1 = storage.all()
                key = ret[0]+'.'+ret[1]
                if key in dict1.keys() and dict1[key].id == ret[1]:
                    dict1.pop(key)
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class name missing **")

    def help_all(self):
        """Print the documention of the command all"""

        print('Prints all string representation of all instances based\
 or not on the class name.\n\
Usage: all <class name> or all\n')

    def do_all(self, line):
        """Prints all string representation of all instances based\
 or not on the class name.
        """
        dict1 = storage.all()
        mod_list = []
        if line:
            if line in self.__model_dict.keys():
                for val in dict1.values():
                    if val.__class__.__name__ == line:
                        mod_list.append(str(val))
                print(mod_list)
            else:
                print("** class doesn't exist **")
        else:
            for val in dict1.values():
                mod_list.append(str(val))
            print(mod_list)

    def help_update(self):
        """Print the documention of the command update"""
        print('Updates an instance based on the class name and id by\
 adding or updating attribute.\n\
Usage: update <class name> <id> <attribute name> "<attribute value>"\n')

    def do_update(self, line):
        """Updates an instance based on the class name and id by\
adding or updating attribute.
        """
        if line:
            a = ""
            for argv in line.split(','):
                a = a + argv
            my_list = shlex.split(a)
            if my_list[0] not in self.__model_dict.keys():
                print("** class doesn't exist **")
                return

            if len(my_list) > 1:
                dict1 = storage.all()
                key = my_list[0]+'.'+my_list[1]
                if key in dict1.keys() and dict1[key].id == my_list[1]:
                    if len(my_list) < 3:
                        print("** attribute name missing **")
                        return
                    if len(my_list) < 4:
                        print("** value missing **")
                        return
                    setattr(dict1[key], my_list[2], my_list[3])
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class name missing **")

    def emptyline(self):
        """dosen’t execute anything when empty line"""
        pass



if __name__ == '__main__':
    HBNBCommand().cmdloop()
