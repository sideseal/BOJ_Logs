// https://www.acmicpc.net/problem/11328

#include <stdio.h>

int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
		i++;
	return (i);
}

int	main(void)
{
	int	N;

	scanf("%d", &N);
	while (N--)
	{
		char		S[2][1001];
		int	arr1[26] = { 0, };
		int	arr2[26] = { 0, };
		int			i;
		int			count;

		i = 0;
		count = 0;
		while (i < 2)
		{
			scanf("%s", S[i]);
			i++;
		}
		if (ft_strlen(S[0]) == ft_strlen(S[1]))
		{
			i = 0;
			while (i < ft_strlen(S[0]))
			{
				arr1[S[0][i] - 97]++;
				arr2[S[1][i] - 97]++;
				i++;
			}
			i = 0;
			while (i < 26)
			{
				if (arr1[i] == arr2[i])
					count++;
				i++;
			}
		}
		if (count == 26)
			printf("Possible\n");
		else
			printf("Impossible\n");
	}
	return (0);
}
