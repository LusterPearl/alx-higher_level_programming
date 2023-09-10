/*
 * File: 13-is_palindrome.c
 * Auth: Mbah Nkemdinma
 */

#include "lists.h"

int is_palindrome(listint_t **head);

/**
 * is_palindrome - checking if the singly linked list is palindrome
 * @head: A pointer the the linked list.
 *
 * Return: if the list is not palindrome
 * if the list is palindrome
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
	{
		/* an empty list or a list with a single element */
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

	/* if the list has ann odd number skips */
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

/**
 * main - main
 *
 * Return: 0
 */
int main(void)
{
	/*create a sample linked list */
	listint_t *head = NULL;
	listint_t *current;

	/* populated the linked list */
	int values[] = {1, 2, 3, 3, 2, 1};

	for (int i = 0; i < 6; i++)
	{
		listint_t *new_node = malloc(sizeof(listint_t));

		if (new_node == NULL)
		{
			perror("Failed to alllocate memory");
			return (-1);
		}
		new_node->n = values[i];
		new_node->next = head;
		head = new_node;
	}

	/* check if the linked list is a palindrome */
	int result = is_palindrome(&head);

	if (result)
	{
		printf("The linked list is a palindrome.\n");
	}
	else
	{
		printf("The linked list is not a palindrome.\n");
	}

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
	return (0);
}
