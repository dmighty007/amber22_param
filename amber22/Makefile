#  Simple top-level Makefile to point users to those hidden below:

CONFIG_FILE=config.h
include $(CONFIG_FILE)

clean.test:
	-(cd AmberTools/test && $(MAKE) clean)
	-(cd test && $(MAKE) clean)

test.clean:  clean.test

test::
	@echo "There is no overall 'test' target."
	@echo "  Use 'test.serial', 'test.parallel, 'test.cuda.serial' or 'test.cuda.parallel'"

test.serial:
	-(cd AmberTools/test && $(MAKE) test)
	@(if [ -n "$(BUILDAMBER)" ] ; then \
		cd test && $(MAKE) test; \
		echo ""; \
		echo "Summary of AmberTools serial tests:"; \
		echo ""; cat ../logs/test_at_serial/at_summary; \
	fi ;\
	)

test.openmp:
	(cd AmberTools/test && $(MAKE) test.openmp)

test.parallel:
	-(cd AmberTools/test && $(MAKE) test.parallel)
	@(if [ -n "$(BUILDAMBER)" ] ; then \
		cd test && $(MAKE) test.parallel; \
		echo ""; \
		echo "Summary of AmberTools parallel tests:"; \
		echo ""; cat ../logs/test_at_parallel/at_summary; \
	fi ;\
	)

test.cuda.serial:
	-(cd AmberTools/test && $(MAKE) test.cuda.serial)
	-(cd test && $(MAKE) test.cuda.serial)

test.cuda.parallel:
	-(cd test && $(MAKE) test.cuda.parallel)

test.mic_offload:
	-(cd test && $(MAKE) test.mic_offload)

test.mic2:
	-(cd test && $(MAKE) test.parallel.pmemd.mic2)
