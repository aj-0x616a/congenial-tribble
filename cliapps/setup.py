from setuptools import (
    setup,
    find_packages
)

from sample_cli import (
    __author__,
    __version__,
    __license__    
)

setup(
    name = 'sample_cli',
    version = __version__,
    author = __author__,
    author_email = '',    
    license = __license__,
    description='Sample cli based application',
    packages = find_packages(),
    entry_points = {
        'console_scripts': [
            'sample_cli = sample_cli.__main__:main'
        ]
    },
)

