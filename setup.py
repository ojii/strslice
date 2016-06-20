from setuptools import setup, find_packages

CLASSIFIERS = [
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2.7',
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Text Processing',
]


setup(
    version='1.0',
    name='strslice',
    description='Python 3 style emoji-safe string slicing for Python 2.',
    url='https://github.com/ojii/strslice',
    author='Jonas Obrist',
    author_email='ojiidotch@gmail.com',
    license='MIT',
    classifiers=CLASSIFIERS,
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
