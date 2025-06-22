from box import Box
from colorama import Fore, init
from task_4.bot_config import bot_config

init(autoreset=True)


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print(f"{Fore.RED} Error: {bot_config.phone.answer.fail(args[0][0])}.")
        except ValueError:
            print(f"{Fore.RED} Error: Enter the argument for the command")
        except IndexError:
            print(f"{Fore.RED} Error: Enter user name.")
        except TypeError:
            print(f"{Fore.RED} Error: Invalid command or missing data.")

    return inner


def check_args_length(
    args,
    expected_length=2,
):
    if len(args) < expected_length:
        raise ValueError("Insufficient arguments")
    return True


@input_error
def add_contact(args, contacts):
    check_args_length(args)
    name, phone = args[0], args[1]
    contacts[name] = phone
    print(f"{Fore.GREEN} {bot_config.add.answer} {name}: {phone}")


@input_error
def change_contact(args, contacts):
    check_args_length(args)
    name, phone = args[0], args[1]
    if name in contacts:
        contacts[name] = phone
        print(f"{Fore.GREEN} {bot_config.change.answer.success}")
    else:
        print(f"{Fore.RED} {bot_config.change.answer.fail}")


@input_error
def show_phone(args, contacts):
    check_args_length(args, 1)
    name = args[0]
    print(f"{Fore.GREEN} {bot_config.phone.answer.success(name, contacts[name])}")


@input_error
def show_all(contacts):
    if not contacts:
        print(f"{Fore.YELLOW} No contacts found.")
    for name, phone in contacts.items():
        print(f"{Fore.GREEN} {name}: {phone}")


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


utils = Box(
    {
        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
        "all": show_all,
        "parse_input": parse_input,
    }
)
