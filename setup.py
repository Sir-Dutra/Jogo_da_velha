from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="jogo_da_velha",
    version="0.0.1",
    author="Matheus Dutra",
    author_email="brandmatheus96@hotmail.com",
    description="projeto simpes de jogo da velha",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sir-Dutra/Jogo_da_velha"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)