// https://www.acmicpc.net/problem/1919

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
	char 	s1[1000];
	char 	s2[1000];
	int		i, j;
	int		count;

	scanf("%s", s1);
	scanf("%s", s2);
	i = 0;
	count = 0;
	while (i < ft_strlen(s1))
	{
		j = 0;
		while (j < ft_strlen(s2))
		{
			if (s1[i] == s2[j])
			{
				s2[j] = '0';
				count++;
				break;
			}
			j++;
		}
		i++;
	}
	printf("%d\n", (ft_strlen(s1) - count) + (ft_strlen(s2) - count));
	return (0);
}
