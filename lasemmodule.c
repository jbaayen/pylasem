#include "Python.h"
#include <pygobject.h>
#include <pycairo.h>
Pycairo_CAPI_t *Pycairo_CAPI;

void lasem_register_classes (PyObject *d);
extern PyMethodDef lasem_functions[];

DL_EXPORT(void)
initlasem(void)
{
    PyObject *m, *d;

    init_pygobject ();

    Pycairo_IMPORT;

    m = Py_InitModule ("lasem", lasem_functions);
    d = PyModule_GetDict (m);



    lasem_register_classes (d);

    if (PyErr_Occurred ()) {
        Py_FatalError ("can't initialise module lasem");
    }
}
