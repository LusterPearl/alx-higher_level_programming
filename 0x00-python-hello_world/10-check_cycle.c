#include "lists.h"

/**
 * check_cycle - checks for the presence of a cycle in a linked list
 * @list: linked list to examine
 *
 * Return: 1 if a cycle exists, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	/* initialize a slow pointer */
	listint_t *fast = list;
	/* Initialize a fast pointer */

	if (!list)
		return (0);
	/* if the list is empty, there is no cycle */

	while (slow && fast && fast->next)
		/* use slow and fast pointers to traverse */
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
