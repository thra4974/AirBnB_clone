#!/usr/bin/python3
""" contains entry point of command interpreter """
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """ defines class HBNBCommand """
    intro = 'Welcome to HBNB command. Type help or ? for options. \n'
    prompt = '(hbnb) '
    existing_classes = ["BaseModel"]

    def do_quit(self, arg):
        """ implements quit command """
        print("hasta la fuego")
        return True

    def do_EOF(self, arg):
        """ implements EOF """
        return True

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

    def do_show(self, arg):
        """ prints string representation of instance """
        l = arg.split()
        if len(l) < 1:
            print("** class name missing **")

        elif l[0] not in self.existing_classes:
            print("** class doesn't exist **")

        elif len(l) < 2:
            print("** instance id missing **")

        objs = storage.all()
        for n in objs.keys():
            if n == "{}.{}".format(l[0], l[1]):
                print(objs[n])
                return False
        print("** no instance found **")

    def do_destroy(self, arg):
        """ deletes an instance based on class name and id """
        l = arg.split()
        if len(l) < 1:
            print("** class name missing **")

        elif l[0] not in self.existing_classes:
            print("** class doesn't exist **")

        elif len(l) < 2:
            print("** instance id missing **")

        del_objs = storage.all()
        for n in list(del_objs):
                del_objs.pop(n)
                return False
        print("** no instance found **")

if __name__ == '__main__':
    H_prompt = HBNBCommand()
    H_prompt.cmdloop()
