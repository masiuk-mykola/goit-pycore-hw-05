from box import Box

greeting_commands = ["hello", "hi", "hey"]
exit_bot_commands = ["exit", "close", "q"]

bot_config = Box(
    {
        "greeting": {
            "command": greeting_commands,
            "answer": "Hello! How can I help you?",
        },
        "exit": {"command": exit_bot_commands, "answer": "Goodbye! Have a great day!"},
        "unknown_command": {
            "answer": "Invalid command.",
        },
        "add": {
            "command": "add",
            "answer": "Contact added.",
        },
        "change": {
            "command": "change",
            "answer": {
                "success": "Contact updated.",
                "fail": "Contact not found.",
            },
        },
        "phone": {
            "command": "phone",
            "answer": {
                "success": lambda name, contact: f"{name}: {contact}",
                "fail": lambda name: f"{name} not found in contacts.",
            },
        },
        "all": {
            "command": "all",
        },
    }
)
