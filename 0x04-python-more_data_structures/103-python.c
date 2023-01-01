#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

void print_python_list(PyObject *p)
{
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t i;
    PyObject *item;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *buf;

    if (!PyBytes_Check(p))
    {
        printf("[ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    buf = PyBytes_AsString(p);

    printf("[*] Python bytes info\n");
    printf("[*] Size = %ld\n", size);
    printf("[*] Trying string: %s\n", buf);
    printf("[*] First %ld bytes:", size < 10 ? size : 10);

    for (i = 0; i < size && i < 10; i++)
        printf(" %02hhx", buf[i]);
    printf("\n");
}
