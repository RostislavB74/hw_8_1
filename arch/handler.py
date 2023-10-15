import difflib

def command_handler(user_input, command_dict):
    if user_input in command_dict:
        return command_dict[user_input][0]
    possible_command = difflib.get_close_matches(
        user_input.split()[0], command_dict, cutoff=0.55)
    if possible_command:
        return f'Wrong command. Maybe you mean: {", ".join(possible_command)}'
    else:
        return 'Wrong command.'
