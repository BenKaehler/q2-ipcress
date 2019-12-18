# ----------------------------------------------------------------------------
# Copyright (c) 2019, Ben Kaehler
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import tempfile
from pathlib import Path

from q2_types.feature_data import DNAFASTAFormat
from q2_align._mafft import run_command


def ipcress(sequence: DNAFASTAFormat,
            primer_A: str,
            primer_B: str,
            min_product_len: int = 50,
            max_product_len: int = 1600,
            mismatch: int = 0,
            memory: int = 2048,
            seed: int = 12) -> DNAFASTAFormat:
    sequence_fp = str(sequence)

    temp_dir = tempfile.TemporaryDirectory(prefix='q2-ipcress-')
    input_fp = Path(temp_dir.name) / 'input.ipcress'
    with open(input_fp, 'w') as fp:
        fp.write(' '.join('q2', primer_A, primer_B,
                          str(min_product_len), str(max_product_len)))

    reads = DNAFASTAFormat()
    reads_fp = str(reads)

    cmd = ['ipcress', input_fp, sequence_fp, '--mismatch', str(mismatch),
           '--memory', str(memory), '--seed', str(seed), '--products']

    run_command(cmd, reads_fp)

    return reads
