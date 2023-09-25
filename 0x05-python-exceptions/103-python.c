#include <python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
* print_python_list - python lists.
* @p: pointer to list objects
*/
void print_python_list(PyObject *p)
{
	PyObject *element = PyList_GetIten(p, i);
	const char *type = Py_TYPE(element)->tp_name;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "[*] Python list info\n [ERROR] Invalid List Object\n");
	return;
	}

		Py_ssize size = PyList_Size(p);
		Py_ssize_t allocated = ((PyListObject *)p)->allocated;

		printf("[*] Python list info\n[*] Size of the Python List = %ld\n[*] Allocated = %ld\n", size. allocated);

		for (Py_ssize_t i = 0; i < size; i++)
		{
			printf("Element %ld: %s\n", i, type);

			if (PyBytes_Check(element))
		{
			print_python_bytes(element);
		}
			else if (PyFloat_Check(element))
		{
			print_python_float(element);
		{
	}
}

/**
* print_python_bytes - python lists
* @p: pointer to the python
*/
void print_python_bytes(PyObject *p)
{
	Py_ssize size = PyBytes_Size(p);
	const char *str = PyBytes_AsString(p);

	if (!PyBytes_Check(p))
	{
	fprintf(stderr, "[.] bytes object info\n [ERROR] Invalid Byes Object\n");
	return;
	}

	printf("[.] bytes object info\n size: %ld\n", size);
	printf(" trying string: %s\n", str);

	printf(" first %d bytes:", size < 10 ? size : 10);
	for (Py_ssize_t i = 0; i < (size < 10 ? size : 10); i++)
	{
		printf(" %02x" str[i] & 0xFF);
	}
	printf("\n");
}

/**
* print_python_float - python lists
* @p: pointer to the pythonlist
*/
void print_python_float(PyObject *p)
{
	double value = PyFloat_AsDouble(p);

	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "[.] float object info\n [ERROR] Invalid Float Object\n");
	return;
	}
	printf("[.] float object info\n value: %f\n", value);
}
