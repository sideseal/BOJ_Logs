// https://www.acmicpc.net/problem/2493

#include <stdio.h>
#define MX 1000005

typedef	struct
{
	int	tower;
	int	index;
}	Tower;

int	main(void)
{
	int		N, t;
	int		i, idx;
	Tower	S[MX];

	scanf("%d ", &N);
	i = 0;
	idx = 0;
	while (i < N)
	{
		scanf("%d ", &t);
		while (idx && S[idx - 1].tower < t)
			idx--;
		if (!idx)
		{
			printf("0");
			S[idx].tower = t;
			S[idx].index = i;
			idx++;
		}
		else if (S[idx - 1].tower >= t)
		{
			printf("%d", S[idx - 1].index + 1);
			S[idx].tower = t;
			S[idx].index = i;
			idx++;
		}
		if (i < N)
			printf(" ");
		i++;
	}
}
