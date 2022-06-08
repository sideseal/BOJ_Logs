// https://www.acmicpc.net/problem/10828

#include <stdio.h>
#include <string.h>

void	push(int *D, int *pos, int n)
{
	D[(*pos)++] = n;
}

int	pop(int *D, int *pos)
{
	if (*pos > 0)
	{
		return (D[--(*pos)]);
	}
	else
		return (-1);
}

int	top(int *D, int *pos)
{
	if (*pos > 0)
		return (D[(*pos)-1]);
	else
		return (-1);
}

int	size(int *pos)
{
	return (*pos);
}

int	empty(int *pos)
{
	if (*pos > 0)
		return (0);
	else
		return (1);
}

int	main(void)
{
	int		D[1000005];
	int		pos;
	int		N;
	int		v;
	char	OP[10];

	scanf("%d ", &N);
	pos = 0;
	while (N--)
	{
		scanf("%s ", OP);
		if (strcmp(OP, "push") == 0)
		{
			scanf(" %d", &v);
			push(D, &pos, v);
		}
		else if (strcmp(OP, "top") == 0)
		{
			printf("%d\n", top(D, &pos));
		}
		else if (strcmp(OP, "size") == 0)
		{
			printf("%d\n", size(&pos));
		}
		else if (strcmp(OP, "pop") == 0)
		{
			printf("%d\n", pop(D, &pos));
		}
		else
		{
			printf("%d\n", empty(&pos));
		}
	}
}
