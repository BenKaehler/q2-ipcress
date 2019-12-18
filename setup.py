# ----------------------------------------------------------------------------
# Copyright (c) 2019, Ben Kaehler
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


from setuptools import setup, find_packages

import versioneer


setup(
    name="q2-ipcress",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    author="Ben Kaehler",
    author_email="kaehler@gmail.com",
    description="QIIME 2 wrapper for ipcress,"
                "an in-silico PCR experiment simulation system",
    license="BSD-3-Clause",
    url="https://qiime2.org",
    entry_points={
        'qiime2.plugins': ['q2-ipcress=q2_ipcress.plugin_setup:plugin']
    },
    package_data={
        'q2_ipcress': ['citations.bib'],
        'q2_ipcress.tests': ['data/*']
    },
    zip_safe=False,
)
