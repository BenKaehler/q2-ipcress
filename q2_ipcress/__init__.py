# ----------------------------------------------------------------------------
# Copyright (c) 2019, Ben Kaehler
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from ._ipcress import ipcress

from ._version import get_versions


__version__ = get_versions()['version']
del get_versions

__all__ = ['ipcress']
