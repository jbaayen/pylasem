# require automake-1.7
AUTOMAKE_OPTIONS=1.7

INCLUDES = $(PYTHON_INCLUDES)

EXTRA_DIST = lasem.defs lasem.override

# pylasem module
pyexec_LTLIBRARIES = lasemmodule.la
lasemmodule_la_LDFLAGS = -module -avoid-version -no-undefined -export-symbols-regex initlasem
lasemmodule_la_CFLAGS = $(PYLASEM_CFLAGS)
lasemmodule_la_LIBADD = $(PYLASEM_LIBS) $(PYTHON_LDFLAGS)
lasemmodule_la_SOURCES = lasemmodule.c
nodist_lasemmodule_la_SOURCES = lasem.c
lasem.c: lasem.defs lasem.override
CLEANFILES = lasem.c

.defs.c:
	(cd $(srcdir)\
	&& $(PYTHON) $(CODEGEN) \
		--override $*.override \
		--prefix py$* $*.defs) > gen-$*.c \
	    && cp gen-$*.c $*.c \
	    && rm -f gen-$*.c

pkgconfigdir = $(libdir)/pkgconfig
pkgconfig_DATA = pylasem.pc
EXTRA_DIST += pylasem.pc
