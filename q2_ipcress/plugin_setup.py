# ----------------------------------------------------------------------------
# Copyright (c) 2019, Ben Kaehler.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from qiime2.plugin import (
    Plugin, Int, Range, Citations, Str)
from q2_types.feature_data import FeatureData, Sequence

import q2_ipcress

citations = Citations.load('citations.bib', package='q2_ipcress')
plugin = Plugin(
    name='ipcress',
    version=q2_ipcress.__version__,
    website='https://github.com/BenKaehler/q2-ipcress',
    package='q2_ipcress',
    description=('This QIIME 2 plugin provides support for generating '
                 'synthetic PCR reads from a set of reference sequences.'),
    short_description='Wrapper for ipcress, an in-silico PCR program.'
)


plugin.methods.register_function(
    function=q2_ipcress.ipcress,
    inputs={'sequence': FeatureData[Sequence]},
    parameters={'primer_a': Str,
                'primer_b': Str,
                'min_product_len': Int % Range(0, None),
                'max_product_len': Int % Range(0, None),
                'mismatch': Int % Range(0, None),
                'memory': Int % Range(0, None),
                'seed': Int % Range(0, None)},
    outputs=[('reads', FeatureData[Sequence])],
    name='Run in-silico PCR on references',
    description='Extract sequencing-like reads from a reference database.',
    parameter_descriptions={
        'primer_a': 'Sequence for the first primer',
        'primer_b': 'Sequence for the second primer',
        'min_product_len': 'Minimum product length to report',
        'max_product_len': 'Maximum product length to report',
        'mismatch': 'The number of mismatches allowed per primer. Allowing '
                    'mismatches reduces the speed of the program as a large '
                    'primer neighbourhood must be constructed, and fewer '
                    'experiments can be fitted in memory prior to each scan '
                    'of the sequence databases.',
        'memory': 'The amount of memory the program should use in Mb. The '
                  'more memory made available ipcress, the faster it will '
                  'run, as more PCR experiments can be conducted in each scan '
                  'of the sequence databases. This does not include memory '
                  'used during the scan (for storing partial results and '
                  'sequences), so the actual amount of memory used will be '
                  'slightly higher.',
        'seed': 'The seed length for the wordneighbourhood for the FSM. If '
                'set to zero, the full primer is used. Shorter words reduce '
                'the size of the neighbourhood, but increase the time taken '
                'by ipcress to filter false positive matches.'
    }
)
