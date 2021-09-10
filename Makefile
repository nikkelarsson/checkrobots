.PHONY: checkrobots

MAN_PAGES=$(shell pwd)/docs/checkrobots.1

checkrobots:
	@echo "TO INSTALL: make install"
	@echo "TO UNINSTALL: make uninstall"
	@echo "TO REINSTALL: make reinstall"

install:
	echo "Installing checkrobots ..."
	# Install the checkrobots Python -package.
	pip install .
	echo "Installing man -pages ..."
	# Install man -pages. Create "man1" if it doesn't exist.
	sudo mkdir -p /usr/local/man/man1
	sudo cp $(MAN_PAGES) /usr/local/man/man1
	sudo mandb
	echo "All successfully installed!"

reinstall:
	echo "Re-installing checkrobots ..."
	# Install the checkrobots Python -package.
	pip install .
	echo "Re-installing man -pages ..."
	# Install man -pages. Create "man1" if it doesn't exist.
	sudo mkdir -p /usr/local/man/man1
	sudo cp $(MAN_PAGES) /usr/local/man/man1
	sudo mandb
	echo "All successfully re-installed!"

uninstall:
	echo "Uninstalling checkrobots ..."
	pip uninstall checkrobots
	echo "Uninstalling man -pages ..."
	sudo rm /usr/local/man/man1/checkrobots.1
	echo "All successfully uninstalled!"
