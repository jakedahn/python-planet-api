import planet_api
from setuptools import setup, find_packages


def parse_requirements(requirements_filename='requirements.txt'):
    requirements = []
    with open(requirements_filename) as requirements_file:
        for requirement in requirements_file:
            requirements.append(requirement.rstrip('\n'))
    return requirements


setup(
    name='planet_api',
    version=planet_api.VERSION,
    url='https://github.com/jakedahn/python-planet-api',
    description='The unofficial python api client for the Planet Labs API.',
    author='Jake Dahn',
    author_email='jake@planet.com',
    install_requires=parse_requirements(),
    packages=find_packages(),
)
