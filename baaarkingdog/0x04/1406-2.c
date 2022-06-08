// https://www.acmicpc.net/problem/1406

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

static Node *AllocNode(void)
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
		free (remove);
	}
}

void	LInsert(List *list)
{
	char	input;
	scanf(" %c", &input);
	Node *newNode = AllocNode();
	newNode->data = input;
	newNode->next = list->cur;
	newNode->prev = list->cur->prev;
	list->cur->prev->next = newNode;
	list->cur->prev = newNode;
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

int	main(void)
{
	List	list;
	int		n;
	char	t;

	Initialize(&list);
	while ((t=getchar()) != '\n')
	{
		Node	*newNode = AllocNode();
		newNode->data = t;
		newNode->prev = list.cur->prev;
		newNode->next = list.cur;
		list.cur->prev->next = newNode;
		list.cur->prev = newNode;
	}
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		char	c;
		scanf(" %c", &c);
		switch(c)
		{
			case 'L':
				LMove(&list);
				break;
			case 'D':
				RMove(&list);
				break;
			case 'B':
				LRemove(&list);
				break;
			case 'P':
				LInsert(&list);
				break;
		}
	}
	Print(&list);
	return (0);
}
