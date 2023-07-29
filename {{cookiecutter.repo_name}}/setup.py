import setuptools

setuptools.setup(
    name="{{ cookiecutter.pkg_name }}",
    version="0.1.0",
    description="",
    license="",

    author="{{ cookiecutter.project_author }}",
    author_email="",
    
    install_requires=[
        "python-dotenv"
    ],
    packages=setuptools.find_packages(),
    zip_safe=False
)
