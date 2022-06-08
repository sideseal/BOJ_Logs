// https://www.acmicpc.net/problem/13300

#include <stdio.h>

int	main(void)
{
	int			n, k;
	int			i, j;
	int			s, g;
	int			ans;
	static int	arr[2][7];

	scanf("%d %d", &n, &k);
	i = 0;
	while (i < n)
	{
		scanf("%d %d", &s, &g);
		arr[s][g]++;
		i++;
	}
	ans = 0;
	i = 0;
	while (i < 2)
	{
		j = 0;
		while (j < 7)
		{
			ans += arr[i][j] / k;
			if (arr[i][j] % k)
				ans++;;
			j++;
		}
		i++;
	}
	printf("%d", ans);
	return (0);
}
// 성별, 학년 별로 방을 배정해야 하기에, 이차원 배열로 성별과 학년 별 인원을 모두 모은다.
// 이후 모아진 인원을 k로 나눠 방을 배정한다. 훌륭한 접근이군...
