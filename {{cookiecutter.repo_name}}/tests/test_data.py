'''test script for {{ cookiecutter.pkg_name }}.data'''

#external imports
import os
import unittest
from unittest.mock import patch

#interal imports
from {{ cookiecutter.pkg_name }} import data

#unit tests
class TestGetEnvVars(unittest.TestCase):
    def test_bad_arg(self):
        '''Validate argument error raise when incorrect variable type
        provided as argument to get_env_vars'''
        self.assertRaises(TypeError, data.get_env_vars, None)
        self.assertRaises(TypeError, data.get_env_vars, 1)

    def test_bad_env_vars(self):
        self.assertRaises(KeyError, data.get_env_vars, "DUMMY VAR")

    def test_expected_outcome(self):
        with patch.dict('os.environ', {'KEY1': 'value_1'}):
            self.assertEqual(data.get_env_vars("KEY1"), "value_1")

        with patch.dict('os.environ', {'KEY1': 'value_1', "KEY2": "value_2"}):
            self.assertEqual(data.get_env_vars("KEY1", "KEY2"), ("value_1", "value_2"))

class TemplateTestCase(unittest.TestCase):
    '''template test case for unit testing'''

    def test_template_func(self):
        '''asserts dummy function creates expected output'''
        mantissa = 5
        base = 10
        power = 4

        gen_output = mantissa * base ** power
        exp_output = 50000

        self.assertEqual(gen_output, exp_output)


if __name__=="__main__":
    unittest.main()