
all:
	@(cd sipgen; $(MAKE))
	@(cd siplib; $(MAKE))

install:
	@(cd sipgen; $(MAKE) install)
	@(cd siplib; $(MAKE) install)
	@test -d $(DESTDIR)/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages || mkdir -p $(DESTDIR)/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages
	cp -f sipconfig.py $(DESTDIR)/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/sipconfig.py
	cp -f /Users/jeremyberkov/Documents/python/tutorial/sip-4.16.2/sipdistutils.py $(DESTDIR)/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/sipdistutils.py

clean:
	@(cd sipgen; $(MAKE) clean)
	@(cd siplib; $(MAKE) clean)
