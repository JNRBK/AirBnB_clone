#!/usr/bin/python3
""" Console Module """
import cmd
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    The HBNBCommand Class

    Attributes:
        prompt = prompt.
        classes_list = list of classes.
    """
    prompt = '(hbnb) '
    classes = [
            "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"
        ]

    def do_quit(self, args):
        """ Quit command to exit the program. """
        return True
    do_EOF = do_quit

    def emptyline(self):
        """ Checks if emptyline passed on, just do nothing, keep going. """
        pass

    def do_create(self, args):
        """ Creates a new instance, saves into JSON file & print id."""
        if len(args) < 1:
            print("** class name missing **")
        elif args not in HBNBCommand().classes:
            print("** class doesn't exist **")
        else:
            new = eval(f'{args}()')
            new.save()
            print(new.id)

    def do_show(self, args):
        """ Prints the string representation of an instance. """
        argv = []
        argv = args.split()
        if not argv:
            print("** class name missing **")

        elif argv[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")

        elif len(argv) < 2 and argv[0] in HBNBCommand.classes:
            print("** instance id missing **")

        elif len(argv) == 2 and argv[0] in HBNBCommand.classes:
            class_name, id_to_look4 = map(str, args.split(" "))
            with open('file.json') as file:
                json_to_dict = json.load(file)
                checking_id = False
                for value in json_to_dict.values():
                    if id_to_look4 == value['id']:
                        class_name = value['__class__']
                        instance = globals()[class_name](**value)
                        checking_id = True
                        print(instance)
                if not checking_id:
                    print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes an instance & save the change into the JSON file. """
        argv = []
        argv = args.split()
        if not argv:
            print("** class name missing **")

        elif argv[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")

        elif len(argv) < 2 and argv[0] in HBNBCommand.classes:
            print("** instance id missing **")

        elif len(argv) == 2 and argv[0] in HBNBCommand.classes:
            class_name, id2look4 = map(str, args.split(" "))
            key = "{}.{}".format(class_name, id2look4)

            objects_saved = storage.all()

            if key in objects_saved:
                del objects_saved[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """ Prints all string representation of all instances. """
        objects_saved = storage.all()
        save_list = []
        if not args:
            for value in objects_saved.values():
                save_list.append(value.__str__())
            print(save_list)
        elif args in HBNBCommand.classes:
            for key, value in objects_saved.items():
                if key.split('.')[0] == args:
                    save_list.append(value.__str__())
            print(save_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """
            Updates an instance by adding/updating attribute
            based on the class name & id
            then save the change into the JSON file.
        """
        argv = args.split()

        if not args:
            print("** class name missing **")
        elif argv[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(argv) < 2:
            print("** instance id missing **")
        else:
            objects_saved = storage.all()
            key_to_find = argv[0] + "." + argv[1]

            if key_to_find not in objects_saved:
                print("** no instance found **")
            elif len(argv) < 3:
                print("** attribute name missing **")
            elif len(argv) < 4:
                print("** value missing **")
            else:
                instance = objects_saved[key_to_find]
                setattr(instance, argv[2], argv[3].strip('"'))
                instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
