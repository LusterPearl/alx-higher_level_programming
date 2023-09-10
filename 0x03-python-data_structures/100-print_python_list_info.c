#include <python.h>
/**
* print_python_list_info = prints out the smallest info about python
* @p: A pointer to a PuObject representing a list
*/
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyObject *obj;

/* Get the size of the python list */
	size = Py_Size(p);
/* Get the allocated size of slots in the list */
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	/* iterated through the list and print information */
	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

	/* Get a pointer to the i-th element */
	obj = PyList_GetItem(p, i);
	printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
