#include "lists.h"

/**
 * insert_node - that's inserts new node
 * 
 * @head: points to the main head in struct
 * @number: data of integer type
 * 
 * Return: newnode
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode = (listint_t *) malloc(sizeof(listint_t));
	listint_t *last;

	if (newnode == NULL)
		return (NULL);

	newnode->n = number;
	newnode->next = NULL;

		if (!*head)
		{
			*head = newnode;
			return (newnode);
		}
		else
		{
			last = *head;

			while (last->next != 0)
			{
				last = last->next;
			}
			last->next = newnode;

			return (newnode);
		}


}
