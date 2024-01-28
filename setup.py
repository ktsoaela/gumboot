# setup.py
from setuptools import setup, find_packages

setup(
    name='gumboot',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'gumboot = gumboot.cli:main',
        ],
    },
    author='Khotso Tsoaela',
    author_email='khotso.s.tsoaela@gmail.com',
    description='Frontend Manager for Django',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ktsoaela/gumboot',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
