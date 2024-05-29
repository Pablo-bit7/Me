#!/usr/bin/python3
"""Module for HBNBCommand class."""

import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project."""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        """
        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)
        class_name = args[0]
        cls = strong.__classes.get(class_name)
        if cls is None:
            print("**class doesn't exist **")
            return
        instance = cls()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an
        instance based on the class name and id.
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        try:
            cls = globals()[args[0]]
        except KeyError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
        else:
            print(instance)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        try:
            cls = globals()[args[0]]
        except KeyError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all
        instances based or not on the class name.
        """
        args = shlex.split(arg)
        if args:
            class_name = args[0]
            cls = storage.__classes.get(class_name)
            if cls is None:
                try:
                    cls = globals()[arg]
                except KeyError:
                    print("** class doesn't exist **")
                    return
            instances = [
                    str(obj) for obj in storage.all().values()
                    if isinstance(obj, cls)
                    ]
        else:
            instances = [str(obj) for obj in storage.all().values()]
        print(instances)

    def do_update(self, arg):
        """
        Updates an instance based on the class
        name and id by adding or updating attribute.
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        try:
            cls = globals()[args[0]]
        except KeyError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        class_name, instance_id, attr_name, attr_value = args[0], args[1], args[2], args[3]
        key = "{}.{}".format(args[0], args[1])
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
            return
        setattr(instance, attr_name, attr_value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
