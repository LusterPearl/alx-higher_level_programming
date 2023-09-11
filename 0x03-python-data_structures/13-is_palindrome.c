#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * add_nodeint - Tnserts a new node at the beginning
 * @head: A pointer to the head of the list
 * @n: The integer value to be added to the list
 *
 * Return: A ponter to the newly created node
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new_node;

	/* allocated memory for a new node */
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	/*set the value of the new node */
	new_node->n = n;
	new_node->next = *head;
	*head = new_node;

	/*return a pointer to the newly created node */
	return (new_node);
}

/**
 * is_palindrome - checking if the singly linked list is palindrome
 * @head: A pointer to the linked list.
 *
 * Return: 0 if the list is not palindrome
 * if the list a is palindrome -1.
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
	{
		/* a list with a single element */
		return (1);
	}

	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *tmp;
	/* use the slow and fast pointer approach to find the middle */
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;

		/* reverse the first half of the list */
		tmp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = tmp;
	}

	/* if the list has an odd number skips */
	if (fast != NULL)
	{
		slow = slow->next;
	}

	/* compare the first half with the second half */
	while (prev != NULL && slow != NULL)
	{
		if (prev->n != slow->n)
		{
			return (0);
		}
		prev = prev->next;
		slow = slow->next;
	}
	return (1);
}
