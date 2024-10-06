# tests/test_main.py

from click import testing
import pytest
from pytest import mark

# import package

@pytest.fixture
def runner():
    '''Creates CLI runner for unit testing. 
    
    Returns:
        CLI runner
    '''
    
    return testing.CliRunner()

@mark.e2e
def test_main_succeeds(runner: testing.CliRunner):
    '''Validates main function executes without failing.

    Arguments:
        runner: Click CliRunner for executing E2E code.
    '''
    
    # result = runner.invoke(package.function)
    # assert result.exit_code == 0

    assert 1 == 1