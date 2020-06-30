#!/usr/bin/python3
""" contains entry point of command interpreter """
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import json
import shlex
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ defines class HBNBCommand """
    prompt = '(hbnb) '
    existing_classes = ["BaseModel", "User", "State",
                        "City", "Amenity", "Place",
                        "Review"]

    """ Basic Commands """
    def do_quit(self, arg):
        """ implements quit command """
        return True

    def help_quit(self):
        """ help command for quit """
        print("Quit command to exit HBNB\n")

    def do_EOF(self, arg):
        """ implements EOF """
        return True

    def help_EOF(self):
        """ help command for EOF option """
        print("EOF option to exit HBNB\n")

    def emptyline(self):
        """ do absolutley nothing """
        pass

    """ Modeling Options """
    def do_create(self, arg):
        """ creates instance of BaseModel """
        l = arg.split()
        if len(l) < 1:
            print("** class name missing **")
        elif arg not in self.existing_classes:
            print("** class doesn't exist **")
        else:
            new_base_model = eval("{}()".format(arg))
            new_base_model.save()
            print(new_base_model.id)

    def help_create(self):
        """ help command for create option """
        print("Create command will create an instance of specified class. \n"
              "Usage: create <class name>")

    def do_show(self, arg):
        """ prints string representation of instance """
        l = arg.split()
        if len(l) < 1:
            print("** class name missing **")
            return False

        elif l[0] not in self.existing_classes:
            print("** class doesn't exist **")
            return False

        elif len(l) < 2:
            print("** instance id missing **")
            return False

        objs = storage.all()
        for n in objs.keys():
            if n == "{}.{}".format(l[0], l[1]):
                print(objs[n])
                return False
        print("** no instance found **")

    def help_show(self):
        """ help command for show option """
        print("Show command prints string representation"
              "of a specified instance\n"
              "Usage: show <class name> <id>")

    def do_destroy(self, arg):
        """ deletes an instance based on class name and id """
        l = arg.split()
        if len(l) < 1:
            print("** class name missing **")
            return False

        elif l[0] not in self.existing_classes:
            print("** class doesn't exist **")
            return False

        elif len(l) < 2:
            print("** instance id missing **")
            return False

        del_objs = storage.all()
        for n in list(del_objs):
                del_objs.pop(n)
                storage.save()
                return False
        print("** no instance found **")

    def help_destroy(self):
        """ help command for destroy option """
        print("destroy command deletes an instance of a class\n"
              "Usage: destroy <class name> <id>")

    def do_all(self, arg):
        """ prints all string rep of all instances """
        l = arg.split()
        objs = storage.all()
        if l[0] not in self.existing_classes:
            print("** class doesn't exist **")
            return False
        else:
            for values in objs:
                print(str(objs[values]))

    def help_all(self):
        """ help command for all option """
        print("all commmand prints all string representations"
              "of all instances\n"
              "Usages: all; all <class name>")

    def do_update(self, args):
        """
        Usage: update <class name> <id> <attribute name> "<attribute value>"

        Updates an instance based on the class name and id by
        adding or updating attribute
        """
        line = shlex.split(args)
        if len(line) == 0:
            print("** class name missing **")
        else:
            try:
                eval(str(line[0]))
            except:
                print("** class doesn't exist **")
                return
            if len(line) == 1:
                print("** instance id missing **")
            else:
                _obj = storage.all()
                Id = str(line[0]) + "." + str(line[1])
                if Id not in _obj:
                    print("** no instance found **")
                else:
                    if len(line) == 2:
                        print("** attribute name missing **")
                    else:
                        if len(line) == 3:
                            print("** value missing **")
                        else:
                            setattr(_obj[Id], line[2], line[3])
                            storage.save()


if __name__ == '__main__':
    H_prompt = HBNBCommand()
    H_prompt.cmdloop()
