// https://www.acmicpc.net/problem/1874

#include <stdio.h>
#define MX 1000005

void	print(char *R)
{
	int	i;

	i = 0;
	while (R[i] != '\0')
	{
		printf("%c\n", R[i]);
		i++;
	}
}

int	main(void)
{
	char	R[MX];
	int		S[MX];
	int		n, m;
	int		i, idx, cnt;

	scanf("%d ", &n);
	cnt = 1;
	idx = 0;
	i = 0;
	while (n--)
	{
		scanf("%d ", &m);
		while (cnt <= m)
		{
			S[idx++] = cnt++;
			R[i++] = '+';
		}
		if (S[idx-1] != m)
		{
			printf("NO\n");
			return (0);
		}
		idx--;
		R[i++] = '-';
	}
	print(R);
}
