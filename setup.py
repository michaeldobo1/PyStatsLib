
from setuptools import find_packages, setup

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name = 'pystatslib',
    packages = find_packages(include = ['pystatslib']),
    version = '0.1.0',
    description = 'Python Statistics and Probability library',
    author = ['Michael Dobo', 'Michael Gannon', 'Maia Bolko', 'Nicole Messina'],
    license = 'MIT',
    install_requires = ['numpy', 'scipy', 'pandas', 'matplotlib.pyplot', 'time', 'sympy', 'sys', 'math', 'mpl_toolkits.mplot3d'],
    setup_requires = ['pytest-runner'],
    tests_require = ['pytest==4.4.1'],
    test_suite = 'tests',
)












