#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - prints basic info about Python lists
 * @p: pointer to a PyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, size;

	printf("[*] Python list info\n");
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
		if (PyBytes_Check(PyList_GetItem(p, i)))
			print_python_bytes(PyList_GetItem(p, i));
	}
}

/**
 * print_python_bytes - prints basic info about Python bytes objects
 * @p: pointer to a PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, size;
	char *str;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		size = PyBytes_Size(p);
		printf("  size: %ld\n", size);
		str = PyBytes_AsString(p);
		printf("  trying string: %s\n", str);
		if (size > 10)
			size = 10;
		else
			size++;
		printf("  first %ld bytes:", size);
		for (i = 0; i < size; i++)
		{
			printf(" %02x", str[i] & 0xff);
		}
		putchar('\n');
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}
