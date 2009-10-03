all: lasem.so

lasem.c: lasem.defs lasem.override
	pygobject-codegen-2.0 -p lasem --register lasem-types.defs -o lasem.override  \
	lasem.defs > $@

CFLAGS = `pkg-config --cflags gdk-pixbuf-2.0 cairo pycairo pygobject-2.0 lasem` \
	-I/usr/include/python2.6/ -I.
LDFLAGS = `pkg-config --libs gdk-pixbuf-2.0 cairo pycairo pygobject-2.0 lasem`

lasem.so: lasem.o lasemmodule.o
	$(CC) $(LDFLAGS) -shared $^ -o $@
