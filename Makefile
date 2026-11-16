.PHONY: pdf zip bom checksums offline refresh
C ?= 6
R ?= 4

pdf:        ## build print/*.pdf
	./scripts/build_pdf.sh

zip:        ## zip the committed repo into dist/
	./scripts/make_zip.sh

bom:        ## shopping list, e.g. make bom C=10 R=5
	python3 scripts/bom_calc.py -c $(C) -r $(R)

checksums:  ## verify STL + firmware files
	cd stl && shasum -a 256 -c --quiet SHA256SUMS
	for d in $$(find firmware -name SHA256SUMS -exec dirname {} \;); do (cd $$d && shasum -a 256 -c --quiet SHA256SUMS) || exit 1; done
	@echo all checksums OK

offline:    ## run the offline flasher on http://localhost:8080
	python3 offline-flasher/serve.py

refresh:    ## online: update flasher mirror, firmware, docs, apps
	python3 scripts/update_offline_flasher.py --apps
