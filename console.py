#!/usr/bin/python3
""" contains entry point of command interpreter """
import cmd


class HBNBCommand(cmd.Cmd):
    """ defines class HBNBCommand """
    intro = 'Welcome to HBNB command. Type help or ? for options. \n'
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """ implements quit command """
        print("hasta la fuego")
        return True

    def do_EOF(self, arg):
        """ implements EOF """
        return True

if __name__ == '__main__':
    H_prompt = HBNBCommand()
    H_prompt.cmdloop()
