AC_PREREQ(2.52)

dnl the pylasem version number
m4_define(pylasem_major_version, 0)
m4_define(pylasem_minor_version, 1)
m4_define(pylasem_micro_version, 0)
m4_define(pylasem_version, pylasem_major_version.pylasem_minor_version.pylasem_micro_version)

dnl versions of packages we require ...
m4_define(pygobject_required_version, 2.10.1)
m4_define(pycairo_required_version, 1.4.0)
m4_define(lasem_required_version, 0.3.0)

AC_INIT(pylasem, pylasem_version)

AC_DEFINE(PYLASEM_MAJOR_VERSION, pylasem_major_version, [PyLasem major version])
AC_DEFINE(PYLASEM_MINOR_VERSION, pylasem_minor_version, [PyLasem minor version])
AC_DEFINE(PYLASEM_MICRO_VERSION, pylasem_micro_version, [PyLasem macro version])

AC_CONFIG_SRCDIR([./lasemmodule.c])
AM_CONFIG_HEADER(config.h)

AM_INIT_AUTOMAKE(AC_PACKAGE_NAME, AC_PACKAGE_VERSION)

AC_DISABLE_STATIC
AC_PROG_LIBTOOL
PKG_PROG_PKG_CONFIG

AM_PATH_PYTHON(2.6)

AM_CHECK_PYTHON_HEADERS(,[AC_MSG_ERROR(could not find Python headers)])

PYGOBJECT_INCLUDEDIR=`$PKG_CONFIG --variable=pygtkincludedir pygobject-2.0`
AC_SUBST(PYGOBJECT_INCLUDEDIR)

PYGOBJECT_DATADIR=`$PKG_CONFIG --variable=datadir pygobject-2.0`
AC_SUBST(PYGOBJECT_DATADIR)

dnl get rid of the -export-dynamic stuff from the configure flags ...
export_dynamic=`(./libtool --config; echo eval echo \\$export_dynamic_flag_spec) | sh`

dnl requirements
PKG_CHECK_MODULES(PYLASEM, [ dnl
                         pygobject-2.0 >= pygobject_required_version,
                         lasem-0.4 >= lasem_required_version,
                         pycairo >= pycairo_required_version
                         ])
if test -n "$export_dynamic"; then
	PYLASEM_LIBS=`echo $PYLASEM_LIBS | sed -e "s/$export_dynamic//"`
fi
PYGOBJECT_DATADIR=`pkg-config --variable=datadir pyobject-2.0`

AC_SUBST(PYLASEM_CFLAGS)
AC_SUBST(PYLASEM_LIBS)

AC_SUBST(PYGOBJECT_DATADIR)

dnl codegen
AC_MSG_CHECKING(for pygobject codegen)
CODEGENDIR=`pkg-config --variable=codegendir pygobject-2.0`
if test -f $CODEGENDIR/codegen.py; then
	CODEGEN=$CODEGENDIR/codegen.py
	AC_MSG_RESULT(yes)
else
	AC_MSG_RESULT(no)
	AC_MSG_ERROR([Error: codegen not found (should be shipped with pygobject!)])
fi
AC_SUBST(CODEGEN)

dnl output
AC_CONFIG_FILES(
  Makefile
  pylasem.pc
)

GTK_DOC_CHECK(1.4)

AC_OUTPUT
