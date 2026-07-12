#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints basic info about a Python bytes object
 * @p: A pointer to the PyObject bytes object
 */
void print_python_bytes(PyObject *p)
{
long unsigned int size, i, limit;
char *trying_str;

printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

size = ((PyVarObject *)(p))->ob_size;
trying_str = ((PyBytesObject *)(p))->ob_sval;

printf("  size: %lu\n", size);
printf("  trying string: %s\n", trying_str);

limit = (size + 1 < 10) ? size + 1 : 10;
printf("  first %lu bytes:", limit);
for (i = 0; i < limit; i++)
printf(" %02x", (unsigned char)trying_str[i]);
printf("\n");
}

/**
 * print_python_list - Prints basic info about a Python list object
 * @p: A pointer to the PyObject list object
 */
void print_python_list(PyObject *p)
{
long unsigned int size, allocated, i;
PyListObject *list = (PyListObject *)p;
PyObject *item;

printf("[*] Python list info\n");
if (!PyList_Check(p))
{
printf("  [ERROR] Invalid List Object\n");
return;
}

size = ((PyVarObject *)(p))->ob_size;
allocated = list->allocated;

printf("[*] Size of the Python List = %lu\n", size);
printf("[*] Allocated = %lu\n", allocated);

for (i = 0; i < size; i++)
{
item = list->ob_item[i];
printf("Element %lu: %s\n", i, item->ob_type->tp_name);
if (PyBytes_Check(item))
print_python_bytes(item);
}
}
