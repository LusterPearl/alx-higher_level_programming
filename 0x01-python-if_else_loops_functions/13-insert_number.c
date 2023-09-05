#include "lists.h"

/**
 * insert_node - Inserts an interger into a sorted singly-linked list.
 * @head: A pointer to the head of the linked list.
 * @number: The integer to insert.
 *
 * Return: If memory allocation fails - NULL
 * Otherwise - a pointer to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	/* create a new node and allocate memory for it */
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	/* set the value of the new code to the given number */
	new->n = number;
	/* if the list is empty or the num is small insert at the beginning */
	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}
	/* tranverse the list to find the correct position */
	while (node && node->next && node->next->n < number)
		node = node->next;
	/* insert the new node into the list */
	new->next = node->next;
	node->next = new;

	return (new);
}
