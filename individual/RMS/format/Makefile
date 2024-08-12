# vim: set ts=8 sts=0 sw=8 si fenc=utf-8 noet:
# vim: set fdm=marker fmr={{{,}}} fdl=0 foldcolumn=4:
# Authors:     BP
# Maintainers: BP
# Copyright:   2024, HRDAG, GPL v2 or later
# =========================================

input := ../import/output/reference.parquet
hand := hand/rules.yml
output := output/rms.parquet

PHONY = clean all

all: $(output)

clean:
	rm -rf output/*

$(output): \
	src/format.py \
	$(input) \
	$(hand)
	-mkdir output
	python3 $< \
		--input=$(input) \
		--hand=$(hand) \
		--output=$@

# done.
