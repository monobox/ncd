#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='monobox-ncd',
    version='0.1.0',
    description='Monobox Network Configuration Daemon',
    long_description=readme,
    author='OXullo Intersecans',
    author_email='x@brainrapers.org',
    url='https://github.com/oxullo/monobox-ncd',
    packages=[
        'monobox-ncd',
    ],
    package_dir={'monobox-ncd': 'monobox_ncd'},
    include_package_data=True,
    install_requires=requirements,
    license='GPL',
    zip_safe=False,
    keywords='monobox-ncd',
    entry_points={
            'console_scripts': ['monobox-ncd = monobox_ncd.runner:run'],
    }
)
