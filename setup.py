#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


name = 't4_geom_convert'
author = u'Davide Mancusi, Martin Maurey'
author_email = u'davide.mancusi@cea.fr'
pkg_copyright = u'2019, ' + author

test_deps = ['pytest', 'pytest-cov', 'pytest-xdist', 'pytest-timeout',
             'hypothesis']
dev_deps = test_deps  + ['flake8', 'pylint', 'sphinx', 'sphinx_rtd_theme']

with open('README.md') as readme:
    long_description = readme.read()

setup(name=name,
      author=author,
      author_email=author_email,
      url=r'https://github.com/arekfu/t4_geom_convert/',
      description='A tool to convert MCNP geometries into the TRIPOLI-4® '
      'format',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=find_packages(exclude=['doc', 't4_geom_convert.UnitTests',
                                      't4_geom_convert.UnitTests.*',
                                      'Oracle']),
      python_requires='>=3.5, <4',
      setup_requires=['pytest-runner', 'setuptools-scm'],
      classifiers=[
          "Programming Language :: Python :: 3",
          "Development Status :: 3 - Alpha",
          "Environment :: Console",
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
          "Operating System :: POSIX :: Linux",
          "Topic :: Scientific/Engineering :: Physics",
          ],
      install_requires=['TatSu==4.3.0', 'numpy'],
      tests_require=test_deps,
      extras_require={'dev': dev_deps},
      command_options={
          'build_sphinx': {
              'source_dir': ('setup.py', 'doc/src'),
              'build_dir': ('setup.py', 'doc/build'),
              }
          },
      include_package_data=True,
      use_scm_version=True,
      entry_points={
          'console_scripts': [
              't4_geom_convert = t4_geom_convert.main:main'
              ]
          }
      )
