"""
install via pip
"""
from setuptools import setup, find_packages
setup(
    name='signalkgen',
    version='0.1.2',
    description='generate test json data based on signal k spec',
    author='Ed Sweeney',
    author_email='ed@onextent.com',
    url='https://github.com/navicore/signalkgen',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'signalkgen=signalkgen.__main__:main'
        ]
    }
)
