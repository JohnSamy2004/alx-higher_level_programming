#include "lists.h"

/**
 * print_dlistint - that prints all the elements of a dlistint_t list.
 * 
 * @h: points to head
 * 
 * Return: the number of nodes
*/
size_t print_dlistint(const dlistint_t *h)
{
	dlistint_t *current;
	size_t nodes = 0;

	if (h)
	{
		current = h;
		while (current != NULL)
		{
			printf("%d\n", current->n);
			current = current->next;
			nodes++;
		}
		
	}

	return (nodes);
}
