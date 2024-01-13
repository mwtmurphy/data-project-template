# src/{{ cookiecutter.repo_name }}/main.py

'''
Non-technical description for outputs and/or outcomes of code.
'''

import click
import {{cookiecutter.package_name}} as src # replace with appropriate alias


@click.command()
@click.version_option(version=src.__version__)
@click.option("--example", default=1, help="example command line option.")
def main(example: int):
    '''Technical description for outputs and/or outcomes of main 
    function.
    
    Args:
        example: example input of type int.

    Returns:
        response: example return of type int.
    '''

    execution_type = "default" if example == 1 else "custom"
    response = f"main execute in mode: {execution_type}"

    return response
