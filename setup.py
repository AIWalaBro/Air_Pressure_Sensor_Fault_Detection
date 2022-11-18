from setuptools import find_packages,setup
from typing import List

def get_requirement()->List[str]:
    '''
        This function contains the list of string
    '''
    requirements_list:List[str] = []
    return requirements_list

setup(

    name = 'Sensor',
    version = '0.0.1',
    author = 'AIWalaBro',
    author_email = 'aiwalabro@gmail.com',
    packages = find_packages(),
    install_requires = get_requirement() #["pymongo==4.2.0"]
)