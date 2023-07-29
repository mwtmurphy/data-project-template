import cookiecutter.main as cc_main
import os
import pathlib
import shutil
import tempfile
import typing
import unittest

CC_TEMPLATE = pathlib.Path(__file__).resolve().parents[1]
ARGS = {
    "project_title": "Test Project",
    "repo_name": "test-repo",
    "project_description": "Unit Tests",
    "project_author": "Mitchell Murphy",
    "python_symlink": "python",
    "pip_symlink": "pip"
}

class Error(Exception):
    pass

class CookieCutterError(Error):
    pass

class TestDirtaScience(unittest.TestCase):
    def test_folder_creation(self):
        '''validates expected folders/files are created'''
        try:
            created_dir = pathlib.Path(TEMP_DIR) / ARGS["repo_name"]
            self.assertTrue(created_dir.is_dir())
        except:
            raise CookieCutterError("template directory was not created with 'repo_name'")

        created_walk = list(os.walk(str(created_dir)))
        created_walk = list(map(lambda el: list(el), created_walk))
        created_walk.sort(key=lambda el: el[0])

        template_dir = CC_TEMPLATE / "{{cookiecutter.repo_name}}"        
        template_walk = list(os.walk(str(template_dir)))
        template_walk = list(map(map_dir_names, template_walk))
        template_walk.sort(key=lambda el: el[0])
    
        for ix in range(len(created_walk)):
            created_walk[ix][1].sort()
            template_walk[ix][1].sort()
            self.assertEqual(created_walk[ix][1], template_walk[ix][1])
            
            created_walk[ix][2].sort()
            template_walk[ix][2].sort()
            self.assertEqual(created_walk[ix][2], template_walk[ix][2])

    def test_user_input(self):
        '''validates user input variables are passed on to expected files'''
        try:
            created_dir = pathlib.Path(TEMP_DIR) / ARGS["repo_name"]
            self.assertTrue(created_dir.is_dir())
        except:
            raise CookieCutterError("template directory was not created with 'repo_name'")
        
        readme_path = created_dir / "README.md"
        
        with open(readme_path, "r") as input_file:
            data = input_file.read().split("\n")
            self.assertEqual(ARGS["project_title"], data[0].replace("# ", ""))
            self.assertEqual(ARGS["project_description"], data[2].replace(".", ""))
            self.assertEqual(ARGS["project_author"], data[88].replace("*", "").strip())


def map_dir_names(dir_branch: typing.Tuple[str, list, list]) -> typing.List[list]:
    '''Returns branch with template keys replaced by test template 
    values'''
    dir_branch = list(dir_branch)

    if "{{cookiecutter.repo_name}}" in dir_branch[0]:
        dir_branch[0] = dir_branch[0].replace("{{cookiecutter.repo_name}}", ARGS["repo_name"])

    pkg_name = ARGS["repo_name"].lower().replace("-", "_")

    if "{{cookiecutter.pkg_name}}" in dir_branch[0]:
        dir_branch[0] = dir_branch[0].replace("{{cookiecutter.pkg_name}}", pkg_name)

    if "{{cookiecutter.pkg_name}}" in dir_branch[1]:
        for ix in range(len(dir_branch[1])):
            if "{{cookiecutter.pkg_name}}" in dir_branch[1][ix]:
                dir_branch[1][ix] = dir_branch[1][ix].replace("{{cookiecutter.pkg_name}}", pkg_name)

    return dir_branch

if __name__=="__main__":
    TEMP_DIR = tempfile.mkdtemp()
    cc_main.cookiecutter(str(CC_TEMPLATE), output_dir=TEMP_DIR, no_input=True, extra_context=ARGS)

    unittest.main()
    
    shutil.rmtree(TEMP_DIR)
