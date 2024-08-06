from setuptools import setup, find_packages

setup(
    name='franzl',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'franzl=franzl.franzl:main',
        ],
    },
    description='A must have CLI tool for Franzl lovers',
    author='Örn Segerstedt',
    author_email='orn.segerstedt@gmail.com',
    url='https://github.com/eeegl/franzl',
)
