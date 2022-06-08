// https://www.acmicpc.net/problem/10773

#include <stdio.h>

void	push(int *D, int *pos, int v)
{
	D[(*pos)++] = v;
}

void	pop(int *pos)
{
	(*pos)--;
}

int	sum(int *D, int *pos)
{
	int	i;
	int	s;

	i = 0;
	s = 0;
	while (i < *pos)
	{
		s += D[i];
		i++;
	}
	return (s);
}

int	main(void)
{
	int	D[1000005];
	int	K;
	int	pos;
	int	v;

	scanf("%d ", &K);
	pos = 0;
	while (K--)
	{
		scanf(" %d", &v);
		if (v == 0)
			pop(&pos);
		else
			push(D, &pos, v);
	}
	printf("%d\n", sum(D, &pos));
	return (0);
}
