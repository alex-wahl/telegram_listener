"""This module is used to parse arguments from command line
and to pass them into telegram client and telegram bot
in the main.py"""
import getopt
import sys
import emoji


def error_exit(message):
    """It is used to notify a user
    about misbehaviour """
    sys.exit(f'{emoji.emojize(":bell:")}'
             f'{message}\n'
             f'{emoji.emojize(":light_bulb:")}'
             f'Please check the parameters and type them again')


def parse_setup_options_from_cmd():
    """
    Parsing setup parameters from command line when you starting up application
    You can pass this parameters to command line
    -i to pass the client_api_id,
    -s to pass the client_api_hash,
    -b to pass the bot_token,
    -l to pass the listening_group,
    -t to pass the target_group,
    -h to get the help,
    --help to get the help,
    --client_api_id to pass the client_api_id,
    --client_api_hash to pass client_api_hash
    --bot_token to pass bot_token
    --listening_group to pass listening_group
    --target_group to pass target_group

    :param: None
    :return: options_dict
    """
    command_line_args = sys.argv[1:]

    param_list = [
        {'setup_option': '-i', 'setup_arg_name': 'client_api_id', 'required': True, 'int_type': True},
        {'setup_option': '-s', 'setup_arg_name': 'client_api_hash', 'required': True, 'int_type': False},
        {'setup_option': '-b', 'setup_arg_name': 'bot_token', 'required': True, 'int_type': False},
        {'setup_option': '-l', 'setup_arg_name': 'listening_group', 'required': True, 'int_type': True},
        {'setup_option': '-g', 'setup_arg_name': 'target_group', 'required': False, 'int_type': False},
        {'setup_option': '-t', 'setup_arg_name': 'target_group_id', 'required': False, 'int_type': True},
        {'setup_option': '-r', 'setup_arg_name': 'replace', 'required': False, 'int_type': False},
        {'setup_option': '-x', 'setup_arg_name': 'text', 'required': False, 'int_type': False},
    ]

    unix_options = "i:vs:vb:vl:vt:vh:r:v:x:v:g:v"
    gnu_options = [
        "help",
        "client_api_id=",
        "client_api_hash=",
        "bot_token=",
        "listening_group=",
        "target_group_id=",
        "target_group=",
        "replace=",
        "text="
    ]

    options_dict = {}

    try:
        setup_options, setup_args = getopt.getopt(command_line_args, unix_options, gnu_options)
        setup_params = [*setup_options, *setup_args]

        for param in param_list:
            param_name = param['setup_arg_name']
            # Iterating through all params,
            # provided from command line and if it's exists,
            # adding it to options_dict
            for item in setup_params:
                if item[0] == param['setup_option'] or item[0] == f"--{param_name}":
                    options_dict[param_name] = int(item[1]) if param['int_type'] else item[1]
                    continue
                if item[0] == '--help' or item[0] == '--h':
                    sys.exit('Please read the readme file')
            if param['required'] and param_name not in options_dict:
                raise ValueError(f'Missing setup option {param_name}')

    except getopt.GetoptError as parsing_error:
        error_exit(parsing_error)
    except ValueError as parsing_error:
        error_exit(parsing_error)

    return options_dict


if __name__ == "__main__":
    print(parse_setup_options_from_cmd())
