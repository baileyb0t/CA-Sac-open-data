#!/usr/bin/env python3
# vim: set ts=4 sts=0 sw=4 si fenc=utf-8 et:
# vim: set fdm=marker fmr={{{,}}} fdl=0 foldcolumn=4:
# Authors:     BP
# Maintainers: BP
# Copyright:   2024, HRDAG, GPL v2 or later
# =========================================

# ---- dependencies {{{
from os.path import isfile, isdir
from pathlib import Path, PosixPath
from sys import stdout
import argparse
import logging
import yaml
import pandas as pd
#}}}

# --- support methods --- {{{
def getargs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=None)
    parser.add_argument("--hand", default=None)
    parser.add_argument("--output", default=None)
    args = parser.parse_args()
    assert Path(args.input).exists()
    assert Path(args.hand).exists()
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


# support methods
def readyaml(fname):
    with open(fname, 'r') as f:
        data = yaml.safe_load(f)
    return data


def fixpath(strpath):
    """
    We can't write the reference table when it contains PosixPath type data.
    So, those get converted to a string in the `import` task.
    Since we're downstream from that task, we also have to prefix the string to read correctly.
    """
    logger.info("formatting and testing file path")
    formatted = f"../import/{strpath}"
    path = PosixPath(formatted)
    assert Path(path).exists()
    return path


def cleanname(colname):
    """Standard column name formatting."""
    assert " " not in colname
    return colname.lower()


def readfile(row):
    """
    Each row in the reference table contains info about a data file we need to read in.
    We also have to format the column names in that data and
    filter out fields we only want to track in the reference table.
    Since these are Excel files and we only read the first sheet,
    we should also check that we're not missing other sheets.
    """
    logger.info(f"reading in dataset for {row.fileyears}")
    logger.info("verifying file contents are as expected")
    sheets = pd.ExcelFile(row.filepath).sheet_names
    if sheets == ['RMS_2020_2022']: sheets = ['RMS_2020_2021']
    assert sheets == [row.filename.replace(".xlsx", "")], f"\
    expected {[row.filename]} sheets but found {sheets}"
    logger.info("proceeding with read")
    df = pd.read_excel(row.filepath)
    df.rename(columns={col: cleanname(col) for col in df.columns}, inplace=True)
    keepcols = ('fileyears', 'fileid', 'filename',)
    for col in keepcols: df[col] = row[col]
    return df


def checkasserts(df, rules):
    """
    The hand file contains `rules` that document characteristics that
    were true of the data at the time the `import` and `clean` tasks were written.
    If these are no longer passing, we should check if there are changes in the new data
    or something has gone wrong in the processing steps.
    """
    logger.info("verifying data")
    for year in range(2004, 2025):
        assert df.fileyears.str.contains(str(year)).any()
    for col in rules['no_missing']:
        found = df[col].isna().sum()
        assert found == 0, \
            f"expected 100% completion rate for `{col}` but found {found} missing values."
    for col, rate in rules['completion_rate'].items():
        found = df[col].notna().sum() / df.shape[0]
        assert found >= rate, \
            f"expected >= {rate*100:.1f}% completion rate for `{col}` but found {found*100:.1f}%."
    for col, nunique in rules['nunique'].items():
        found = len(df[col].unique())
        assert found == nunique, \
            f"expected {nunique} nunique values for `{col}`"
    for col, rate in rules['unique_rate'].items():
        found = len(df[col].unique()) / df[col].notna().sum()
        assert found >= rate, \
            f"expected >= {rate*100:.1f}% unique rate for `{col}` but found {found*100:.1f}%."
    return 1


def readconcat(ref, rules):
    """
    The CAD datasets are organized by year (of call?), so we should be safe to use
    concatenation when combining them into one dataset.
    """
    logger.info("reading in data and formatting to table")
    dfs = [readfile(ref.iloc[i]) for i in range(ref.shape[0])]
    full = pd.concat(dfs)
    #checkasserts(df=full, rules=rules)
    return full
# }}}

# --- main --- {{{
if __name__ == '__main__':
    args = getargs()
    logger = getlogger(__name__, "output/format.log")

    logger.info("loading data")
    ref = pd.read_parquet(args.input)
    rules = readyaml(args.hand)

    ref.filepath = ref.filepath.apply(fixpath)
    data = readconcat(ref=ref, rules=rules)

    logger.info("writing formatted data")
    data.district = data.district.astype(str)
    data.zone = data.zone.astype(str)
    data.ibr_code = data.ibr_code.astype(str)
    data.to_parquet(args.output)

    logger.info('done')
# }}}

# done.

