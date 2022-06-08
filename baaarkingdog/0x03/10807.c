// https://www.acmicpc.net/problem/10807

#include <stdio.h>

int	main(void)
{
	int			N;
	int			v;
	int			i;
	int			count;
	static int	arr[101];

	scanf("%d", &N);
	i = 0;
	while (i < N)
	{
		scanf("%d", &arr[i]);
		i++;
	}
	scanf("%d", &v);
	i = 0;
	count = 0;
	while (i < N)
	{
		if (arr[i] == v)
			count++;
		i++;
	}
	printf("%d", count);
	return (0);
}
