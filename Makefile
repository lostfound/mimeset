ifeq ("${PREFIX}", "")
PREFIX=/usr/local
endif

all:

install: all
	install -D mimeset.py $(PREFIX)/lib/mimeset/mimeset.py
	mkdir -m 0755 -p $(PREFIX)/bin
	ln -sf $(PREFIX)/lib/mimeset/mimeset.py $(PREFIX)/bin/mimeset

uninstall:
	rm -rf  $(PREFIX)/lib/mimeset $(PREFIX)/bin/mimeset
