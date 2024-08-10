# vim: set ts=8 sts=0 sw=8 si fenc=utf-8 noet:
# vim: set fdm=marker fmr={{{,}}} fdl=0 foldcolumn=4:
# Authors:     BP
# Maintainers: BP
# Copyright:   2024, HRDAG, GPL v2 or later
# =========================================

rms:= ../format/output/rms.parquet

PHONY := all clean

all: output/rms_asof_$(shell date +%F).done

clean:
	rm -rf output/*

output/rms_asof_$(shell date +%F).done: \
    $(rms)
	-mkdir output
	-cd output && ln -s ../$(rms) .
	touch $@

# done.

