"""
   Copyright 2013 nilmtk authors

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from setuptools import setup, find_packages, Extension
from os.path import join
import os
import sys
import warnings

"""
Following Segment of this file was taken from the pandas project(https://github.com/pydata/pandas)
"""
# Version Check

MAJOR = 0
MINOR = 2
MICRO = 0
ISRELEASED = False
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)
QUALIFIER = ''

FULLVERSION = VERSION
if not ISRELEASED:
    FULLVERSION += '.dev'
    try:
        import subprocess
        try:
            pipe = subprocess.Popen(["git", "rev-parse", "--short", "HEAD"],
                                    stdout=subprocess.PIPE).stdout
        except OSError:
            # msysgit compatibility
            pipe = subprocess.Popen(
                ["git.cmd", "rev-parse", "--short", "HEAD"],
                stdout=subprocess.PIPE).stdout
        rev = pipe.read().strip()
        # makes distutils blow up on Python 2.7
        if sys.version_info[0] >= 3:
            rev = rev.decode('ascii')

        FULLVERSION += "-%s" % rev
    except:
        warnings.warn("WARNING: Couldn't get git revision")
else:
    FULLVERSION += QUALIFIER


def write_version_py(filename=None):
    cnt = """\
version = '%s'
short_version = '%s'
"""
    if not filename:
        filename = os.path.join(
            os.path.dirname(__file__), 'nilmtk', 'version.py')

    a = open(filename, 'w')
    try:
        a.write(cnt % (FULLVERSION, VERSION))
    finally:
        a.close()
write_version_py()
# End of Version Check


deps = {
    "bottleneck>=0.6.0",
    "hmmlearn",
    "ipython",
    "matplotlib",
    "networkx",
    "nilm_metadata",
    "numexpr>=2.2.2",
    "numpy>=1.8.0",
    "pandas==0.17.1",
    "scikit-learn>=0.14",
    "scipy",
    "six",
    "tables",
}

dev_deps = {
    "sh",
    "nose",
    "coveralls",
    "coverage",
    "psycopg2",
    "pbs",
}


setup(
    name='nilmtk',
    version=FULLVERSION,
    packages=find_packages(),
    install_requires=list(deps),
    extras_require={
        'dev': list(dev_deps),
    },
    description='Estimate the energy consumed by individual appliances from '
                'whole-house power meter readings',
    author='nilmtk authors',
    author_email='',
    url='https://github.com/nilmtk/nilmtk',
    download_url="https://github.com/nilmtk/nilmtk/tarball/master#egg=nilmtk-dev",
    long_description=open('README.md').read(),
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache 2.0',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],
    keywords='smartmeters power electricity energy analytics redd '
             'disaggregation nilm nialm'
)
