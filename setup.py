# -*- coding: utf-8 -*-
#
# This file were created by Python Boilerplate. Use boilerplate to start simple
# usable and best-practices compliant Python projects.
#
# Learn more about it at: http://github.com/fabiommendes/python-boilerplate/
#

import os
import codecs
from setuptools import setup, find_packages

# Save version and author to __meta__.py
version = open('VERSION').read().strip()
dirname = os.path.dirname(__file__)
path = os.path.join(dirname, 'src', u'success_backup_check', '__meta__.py')
meta = '''# Automatically created. Please do not edit.
__version__ = '%s'
__author__ = u'Steffen.Exler@gmail.com'
''' % version
with open(path, 'w') as F:
    F.write(meta)

setup(
    # Basic info
    name=u'success-backup-check',
    version=version,
    author='Steffen.Exler@gmail.com',
    author_email='Steffen Exler',
    url='https://github.com/linuxluigi/success-backup-check',
    description='A short description for your project.',
    long_description=codecs.open('README.md', 'rb', 'utf8').read(),

    # Classifiers (see https://pypi.python.org/pypi?%3Aaction=list_classifiers)
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
    ],

    entry_points={
        "console_scripts": ['success_backup_check = success_backup_check.__main__:main']
    },

    # Packages and dependencies
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        "sendgrid>=6.0.5, <7",
        "python-telegram-bot>=11.1.0, <12",
        "requests>=2.22.0, <3",
    ],
    extras_require={
        'dev': [
            'python-boilerplate[dev]',
        ],
    },

    # extra files
    data_files=[('/lib/systemd/system/', ['scripts/backup.service'])],

    # Other configurations
    zip_safe=False,
    platforms='any',
)
