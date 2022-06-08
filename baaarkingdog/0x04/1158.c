// https://www.acmicpc.net/problem/1158

#include <stdio.h>
#include <stdlib.h>

typedef struct _node
{
	struct _node	*next;
	struct _node	*prev;
	int				data;
}	Node;

typedef struct
{
	Node	*head;
	Node	*tail;
}	List;

void	Initialization(List *list)
{
	list->head = NULL;
	list->tail = NULL;
}

void	Insert(List *list, int i)
{
	Node	*newNode;

	newNode = (Node *)malloc(sizeof(Node));
	if (list->head == NULL)
	{
		list->head = newNode;
		list->tail = newNode;
		newNode->data = i;
		newNode->next = list->tail;
		newNode->prev = list->head;
	}
	else
	{
		list->head->prev = newNode;
		list->tail->next = newNode;
		newNode->data = i;
		newNode->next = list->head;
		newNode->prev = list->tail;
		list->tail = newNode;
	}
}

void	Delete(List *list, int M)
{
	Node	*cur;

	cur = list->head;
	while (--M)
		cur = cur->next;
	list->head = cur->next;
	cur->prev->next = cur->next;
	cur->next->prev = cur->prev;
	printf("%d", cur->data);
	free(cur);
}

int	main(void)
{
	int		N;
	int		M;
	int		i;
	List	list;

	Initialization(&list);
	scanf("%d %d", &N, &M);
	i = 1;
	while (i <= N)
	{
		Insert(&list, i);
		i++;
	}
	printf("<");
	i = 1;
	while (i <= N)
	{
		Delete(&list, M);
		if (i < N)
			printf(", ");
		i++;
	}
	printf(">");
	return (0);
}
