from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str) -> List[str]:
    '''
    this function will retirn the list of reqirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)


setup(
    name='ml_project',
    version='0.0.1',
    author='Aravind',
    author_email='aravind1843@gmail.com',
    packages=find_packages(),
    install_requieres = get_requirements('requirements.txt')

)