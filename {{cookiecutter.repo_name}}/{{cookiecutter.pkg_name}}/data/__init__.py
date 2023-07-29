'''data import and parsing submodule'''

#module imports
import dotenv
import os
import typing

from {{ cookiecutter.pkg_name }} import errors

#functions
def get_env_vars(*args: str) -> typing.Union[typing.Tuple[str, ...], str]:
    '''Returns list of environment variable values respective for each
    key provided, or a string if only a single variable is requested'''
    try:
        if len(args) > 1:
            env_vars = tuple(map(lambda key: os.environ[key], args)) 
        else:
            env_vars = os.environ[args[0]]

    except KeyError:
        raise KeyError("Environment variable not found. Ensure all variables are loaded.")
    except TypeError:
        raise TypeError("Invalid argument provided. Key expected as type 'str'.")
    
    return env_vars

def load_env_vars() -> bool:
    '''Returns true if function executes successfully, else false'''
    env_loaded = dotenv.load_dotenv(dotenv.find_dotenv())
    return env_loaded

