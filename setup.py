from setuptools import setup, find_packages


setup(
    version='1.0+6.2.0',
    name='strslice',
    install_requires=[
        'jinja2',
        'requests',
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'strslice-generate = strslice.generator:cli',
        ]
    },
    test_suite='strslice.tests',
)
