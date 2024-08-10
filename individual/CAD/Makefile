# vim: set ts=8 sts=0 sw=8 si fenc=utf-8 noet:
# vim: set fdm=marker fmr={{{,}}} fdl=0 foldcolumn=4:
# Authors:     BP
# Maintainers: BP
# Copyright:   2024, HRDAG, GPL v2 or later
# =========================================

buildstampdir := export/output/buildstamps

.PHONY: all clean import format export

all: export

clean: 
	for task in import format export; do \
		cd $$task && make clean && cd -; \
	done

export: format
	cd $@ && make
	-mkdir $(buildstampdir)
	cd $(buildstampdir) && touch $(shell date +%FT%T%Z).done

format: import
	cd $@ && make

import:
	cd $@ && make
