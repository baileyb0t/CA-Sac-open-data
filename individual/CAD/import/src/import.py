#!/usr/bin/env python3
# vim: set ts=4 sts=0 sw=4 si fenc=utf-8 et:
# vim: set fdm=marker fmr={{{,}}} fdl=0 foldcolumn=4:
# Authors:     BP
# Maintainers: BP
# Copyright:   2024, HRDAG, GPL v2 or later
# =========================================

# ---- dependencies {{{
from os.path import isfile, isdir
from pathlib import Path
from sys import stdout
import argparse
import logging
import hashlib
import re
import pandas as pd
#}}}

# --- support methods --- {{{
def getargs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--indir", default=None)
    parser.add_argument("--output", default=None)
    args = parser.parse_args()
    assert Path(args.indir).exists()
    assert Path(f"{args.indir}/Sacramento_Call_for_Service_Data_2019_-7220233881378889146.csv").exists()
    return args


def getlogger(sname, file_name=None):
    logger = logging.getLogger(sname)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s " +
                                  "- %(message)s", datefmt='%Y-%m-%d %H:%M:%S')
    stream_handler = logging.StreamHandler(stdout)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    if file_name:
        file_handler = logging.FileHandler(file_name)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger


def getfiles(dirname, fext='csv'):
    """Basic collection of files from direction."""
    assert isdir(dirname)
    return [path for path in Path(dirname).rglob(f'*.{fext}')]


def hashid(fname):
    """Create a `fileid` from the contents of each file."""
    if pd.isna(fname): return None
    with open(fname, 'rb') as f:
        digest = hashlib.file_digest(f, "sha1")
    return digest.hexdigest()[:8]


def get_reftable(files):
    """
    Each file and filepath contains some metadata we want to include in the ref table.
    """
    reference = [{
        'fileid': hashid(file),
        'filepath': file,
        'filename': file.name,
        'fileyear': re.findall("Data_([0-9]{4})_", file.name)[0]
    } for file in files]
    return pd.DataFrame(reference)
# }}}

# --- main --- {{{
if __name__ == '__main__':
    args = getargs()
    logger = getlogger(__name__, "output/import.log")

    logger.info(f"reading {args.indir} directory for data files")
    files = getfiles(args.indir)
    logger.info("building reference table of data files")
    ref = get_reftable(files)
    ref.filepath = ref.filepath.astype(str)
    logger.info("writing reference table")
    ref.to_parquet(args.output)

    logger.info('done')
# }}}

# done.

