from setuptools import setup

__version__ = '0.0.1'


with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
    name='python-archetype',
    description='python-archetype API',
    packages=['app'],
    version=__version__,
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only'
    ],
    setup_requires=[
        'pytest-runner',
        'flake8'
    ],
    tests_require=[
        'pytest>=4.1.1',
        'pytest-cov>=2.6.1',
        'http-server-mock==1.2',
        'atomicwrites==1.4.0'
    ],
    test_suite='tests',
    install_requires=requirements
)
