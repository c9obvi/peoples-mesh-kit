.PHONY: pdf zip bom checksums
C ?= 6
R ?= 4

pdf:        ## build print/*.pdf
	./scripts/build_pdf.sh

zip:        ## zip the committed repo into dist/
	./scripts/make_zip.sh

bom:        ## shopping list, e.g. make bom C=10 R=5
	python3 scripts/bom_calc.py -c $(C) -r $(R)

checksums:  ## verify STL + firmware files
	cd stl && shasum -a 256 -c SHA256SUMS
	cd firmware/meshcore-v1.18.0 && shasum -a 256 -c SHA256SUMS
