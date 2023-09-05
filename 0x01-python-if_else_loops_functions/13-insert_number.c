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
	/* initialize a pointer to the current node */
	listint_t *current = *head;
	/* declare a pointer for the new node */
	listint_t *new node;

	/* allocate memory for the new node and check for allocation success */
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	/* initialize the new node with the provided number */
	new_node->n = number;

	/* handle list is empty or the new node should be the new head */
	if (current == NULL || current->n >= number)
	{
		new_node->next = current;
		*head = new_node;
		return (new_node);
	}

	/* Traverse the list to find the current posistion to insert the new node */
	while (current && current->next && current->next->n < number)
		current = current->next;

	/*Insert the new node at the appropriate position */
	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
