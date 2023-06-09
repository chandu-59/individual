from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_req(a:str)->List[str]:
    requirements=[]
    with open(a) as file_obj:
        reuirements=file_obj.readlines()
        [i.replace("/n","") for i in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
    
setup(name='MLproject',
versio='0.0.1',
author='chandu',
packages=find_packages(),
install_requires=get_req('requirements.txt')
)