// https://www.acmicpc.net/problem/5397

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct	_node
{
	char			data;
	struct _node	*prev;
	struct _node	*next;
}	Node;

typedef struct
{
	Node	*head;
	Node	*tail;
	Node	*cur;
}	List;

static Node	*AllocNode(void)
{
	return calloc(1, sizeof(Node));
}

void	Print(List *list)
{
	list->cur = list->head->next;
	while (list->cur->next != NULL)
	{
		printf("%c", list->cur->data);
		if (list->cur->next != NULL)
			list->cur = list->cur->next;
	}
}

void	Initialize(List *list)
{
	list->head = AllocNode();
	list->tail = AllocNode();
	list->head->next = list->tail;
	list->head->prev = NULL;
	list->tail->next = NULL;
	list->tail->prev = list->head;
	list->cur = list->tail;
}

void	LMove(List *list)
{
	if (list->cur->prev->prev != NULL)
		list->cur = list->cur->prev;
}

void	RMove(List *list)
{
	if (list->cur->next != NULL)
		list->cur = list->cur->next;
}

void	LRemove(List *list)
{
	if (list->cur->prev->prev != NULL)
	{
		Node *remove = list->cur->prev;
		list->cur->prev->prev->next = list->cur;
		list->cur->prev = list->cur->prev->prev;
		free(remove);
	}
}

void	LInsert(List *list, char c)
{
	Node	*newNode;
	newNode = AllocNode();
	newNode->data = c;
	newNode->prev = list->cur->prev;
	newNode->next = list->cur;
	list->cur->prev->next = newNode;
	list->cur->prev = newNode;
}

int	main(void)
{
	List	list;
	int		N;
	char	c;

	scanf("%d ", &N);
	while (N--)
	{
		Initialize(&list);
		while ((c=getchar()) != '\n')
		{
			switch(c)
			{
				case '<':
					LMove(&list);
					break;
				case '>':
					RMove(&list);
					break;
				case '-':
					LRemove(&list);
					break;
				default:
					LInsert(&list, c);
					break;
			}
		}
		Print(&list);
		printf("\n");
	}
	return (0);
}
