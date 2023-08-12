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
        method_dict = {'all': self.do_all, 'count': self.count, "show": self.do_show, 'destroy': self.do_destroy, 'update': self.do_update}
        if line:
            l = line.replace("(", ".")
            l = l.replace(")", ".")
            l = l.replace(", ", ".")
            new = l.split(".")
            if len(new) > 1:
                if new[1] in method_dict.keys():
                    if new[2] != '':
                        if new[3] != '':
                            method_dict[new[1]](new[0]+' '+ str(new[2])+' '+str(new[3])+' '+str(new[4]))
                            return
                        else:
                            method_dict[new[1]](new[0]+' '+ new[2])
                            return
                    else:
                        method_dict[new[1]](new[0])
                        return
        r = super(HBNBCommand, self).onecmd(line)
        return r

    def count(self, value):
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
            my_list = pars(line)
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
                    try:
                        x = getattr(dict1[key], my_list[2])
                        x = type(x)
                        my_list[3] = x(my_list[3])
                        setattr(dict1[key], my_list[2], my_list[3])
                    except ValueError:
                        print(f"{my_list[2]} only accepte {str(x)[7:-1]}\
 value")
                    dict1[key].save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class name missing **")

    def emptyline(self):
        """Do empty line + ENTER dosen’t execute anything"""
        pass


def pars(line):
    """Convert a string into list

    Args:
        x (str): variable to collect char
        c (str): var to handle double quote
        i (str): var to count th loop run
        my_list (list): list to handel the values
    """

    x = ""
    c = ''
    i = 0
    my_list = []
    for ret in line:
        i += 1
        if ret == '"' and c == '':
            c = ret
            continue
        elif c == '"' and ret != '"':
            x += ret
            continue
        elif c == '"' and ret == '"':
            my_list.append(x)
            c = ''
            x = ''
            continue
        if ret == ' ':
            my_list.append(x)
            x = ""
        else:
            x += ret
            if i == len(line):
                my_list.append(x)
    return my_list


if __name__ == '__main__':
    HBNBCommand().cmdloop()
