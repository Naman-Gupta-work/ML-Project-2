from setuptools import find_packages,setup

from typing import List


def get_requirements()->List[str]:
    # the functions returns list of requirements

    Libraries:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            
            lines=file.readlines()
            
            for line in lines:
                requirement=line.strip()

                if requirement and requirement!="-e .":        # confused why AND condition to prevent the blank lines
                    Libraries.append(requirement)
    except FileNotFoundError:
        print("requirements.txt is added")

    return Libraries

print(get_requirements()) # run setup.py if this prints then it is working


setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Naman Gupta",
    author_email="namangupta060504@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
    
)