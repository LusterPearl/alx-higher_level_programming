#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

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
