## utils.py

def command_is_valid(message):
    """
    A function that checks if a command in a message is valid.
    A valid command starts with '!' and has at least one character following the '!'.
    """
    if message.startswith('!') and len(message.split(' ')[0]) > 1:
        return True
    return False