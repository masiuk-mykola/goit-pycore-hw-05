from colorama import Fore, init
from task_4.bot_config import bot_config
from task_4.bot_utils import utils

init(autoreset=True)


def main():
    print(f"{Fore.GREEN} Bot is starting...")
    print(f"{Fore.BLUE} Welcome to the Bot Assistant!")
    contacts = {}

    while True:
        user_input = input("Enter a command (or 'exit' to quit): ").strip().lower()
        command, *args = utils.parse_input(user_input)

        if command in bot_config.exit.command:
            print(f"{Fore.GREEN}{bot_config.exit.answer}")
            break

        elif command in bot_config.greeting.command:
            print(f"{Fore.GREEN}{bot_config.greeting.answer}")

        elif command == bot_config.add.command:
            utils.add(args, contacts)

        elif command == bot_config.change.command:
            utils.change(args, contacts)

        elif command == bot_config.phone.command:
            utils.phone(args, contacts)

        elif command == bot_config.all.command:
            utils.all(contacts)

        else:
            print(f"{Fore.RED} {bot_config.unknown_command.answer}")


if __name__ == "__main__":
    main()
