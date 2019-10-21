## This will contain utility functions.
import commands as cmd
import exceptions as erx



def tokenize(cmd):
    tokens = command.split()
    return tokens

def validateCommand(tokens):
    
    if type(tokens) == str:
        x = tokens
    elif type(tokens) == list:
        x = tokens[0]

    if x not in command_list.keys:
        raise CommandNotFoundException(x)
    
