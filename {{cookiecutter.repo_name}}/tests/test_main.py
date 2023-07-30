# tests/test_main.py

from click import testing
import pytest
from pytest import mark

from {{ cookiecutter.repo_name }} import main

@pytest.fixture
def runner():
    '''Creates CLI runner for unit testing. 
    
    Returns:
        CLI runner
    '''
    
    return testing.CliRunner()

@mark.e2e
def test_main_succeeds(runner: testing.CliRunner, is_caching: bool):
    '''Validates main function executes without failing.

    Arguments:
        runner: Click CliRunner for executing E2E code.
    '''
    
    result = runner.invoke(main.main)
    assert result.exit_code == 0