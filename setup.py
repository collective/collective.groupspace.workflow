# -*- coding: utf-8 -*-
"""
collective.groupspace.workflow
"""

from setuptools import setup, find_packages
import os

__version__  = '1.0'

__here__ = os.path.abspath(os.path.dirname(__file__))

README = open(os.path.join(__here__, 'README.txt')).read()
CHANGES = open(os.path.join(__here__, 'CHANGES.txt')).read()

setup(name='collective.groupspace.workflow',
    version=__version__,
    description="A placeful workflow policy enforcing a default workflow",
    long_description=README + '\n\n' +  CHANGES,
    classifiers=[
      "Development Status :: 4 - Beta",
      "Environment :: Web Environment",
      "Framework :: Plone",
      "Framework :: Zope2",
      "Intended Audience :: Developers",
      "License :: OSI Approved :: GNU General Public License (GPL)",
      "Operating System :: OS Independent",
      "Programming Language :: Python",
      "Topic :: Internet :: WWW/HTTP :: Dynamic Content",        
      "Topic :: Office/Business :: Groupware",
      "Topic :: Software Development :: Libraries :: Python Modules",
      ],
    keywords='',
    author='Maik Röder',
    author_email='roeder@berg.net',
    url='http://svn.plone.org/svn/collective/collective.groupspace.workflow',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective', 'collective.groupspace'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
    ],
    entry_points="""
    # -*- Entry points: -*-

    [distutils.setup_keywords]
    paster_plugins = setuptools.dist:assert_string_list

    [egg_info.writers]
    paster_plugins.txt = setuptools.command.egg_info:write_arg
    """,
    paster_plugins = ["ZopeSkel"],
    )
