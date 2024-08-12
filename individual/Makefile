# vim: set ts=8 sts=0 sw=8 si fenc=utf-8 noet:
# vim: set fdm=marker fmr={{{,}}} fdl=0 foldcolumn=4:
# Authors:     BP
# Maintainers: BP
# Copyright:   2024, HRDAG, GPL v2 or later
# =========================================

buildstampdir := export/output/buildstamps

.PHONY: all clean CAD RMS

all: CAD RMS

clean: 
	for task in CAD RMS; do \
		cd $$task && make clean && cd -; \
	done

CAD:
	cd $@ && make

RMS:
	cd $@ && make
