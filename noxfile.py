# noxfile.py

import nox


@nox.session(python=["3.9", "3.10", "3.11"])
def tests(session):
    session.run("poetry", "install", external=True)
    tmp_dir = session.create_tmp()
    session.run("cookiecutter", ".", "-o", tmp_dir, "--no-input")