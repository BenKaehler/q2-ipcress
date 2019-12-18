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
from q2_alignment._mafft import run_command


def ipcress(sequence: DNAFASTAFormat,
            primer_a: str,
            primer_b: str,
            min_product_len: int = 50,
            max_product_len: int = 1600,
            mismatch: int = 0,
            memory: int = 2048,
            seed: int = 12) -> DNAFASTAFormat:
    sequence_fp = str(sequence)

    temp_dir = tempfile.TemporaryDirectory(prefix='q2-ipcress-')
    input_fp = str(Path(temp_dir.name) / 'input.ipcress')
    with open(input_fp, 'w') as fp:
        fp.write(' '.join(['q2', primer_a, primer_b,
                           str(min_product_len), str(max_product_len)]))

    output_fp = str(Path(temp_dir.name) / 'output.ipcress')

    cmd = ['ipcress', '--input', input_fp, '--sequence', sequence_fp,
           '--mismatch', str(mismatch), '--memory', str(memory),
           '--seed', str(seed), '--pretty', 'False', '--products', 'True']

    run_command(cmd, output_fp)

    reads = DNAFASTAFormat()
    reads_fp = str(reads)

    with open(output_fp) as ofp:
        with open(reads_fp, 'w') as rfp:
            for line in ofp:
                if 'ipcress' in line:
                    continue
                if line.startswith('>'):
                    line = '>'+line.split()[2].split(':')[0]+'\n'
                rfp.write(line)

    return reads
