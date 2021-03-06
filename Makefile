.PHONY: checkrobots install install-editable uninstall
PROG = checkrobots
PYTHON = python3.8
MAN_PAGES = $(shell pwd)/docs/man/checkrobots.1
MAN_PAGES_MD = $(shell pwd)/docs/man/checkrobots.1.md

checkrobots:
	@echo "TO INSTALL: make install"
	@echo "TO UNINSTALL: make uninstall"
	@echo "TO REINSTALL: make reinstall"

install:
	@echo "Installing $(PROG) ..."
	$(PYTHON) -m pip install -qq .
	@echo "Installing man -pages ..."
	sudo mkdir -p /usr/local/man/man1
	pandoc $(MAN_PAGES_MD) -s -t man -o $(MAN_PAGES)
	sudo cp $(MAN_PAGES) /usr/local/man/man1
	@echo "All successfully installed!"

install-editable:
	@echo "Installing $(PROG) as editable ..."
	$(PYTHON) -m pip install -qq -e .
	@echo "Installing man -pages ..."
	sudo mkdir -p /usr/local/man/man1
	pandoc $(MAN_PAGES_MD) -s -t man -o $(MAN_PAGES)
	sudo cp $(MAN_PAGES) /usr/local/man/man1
	@echo "All successfully installed!"

uninstall:
	@echo "Uninstalling $(PROG) ..."
	$(PYTHON) -m pip uninstall -qq --yes $(PROG)
	@echo "Uninstalling man -pages ..."
	sudo rm /usr/local/man/man1/checkrobots.1
	@echo "All successfully uninstalled!"
