// https://www.acmicpc.net/problem/6198

#include <stdio.h>
#define MX 1000005

int	main(void)
{
	int			N;
	int			H;
	int			S[MX];
	int			idx;
	long long	sum;

	scanf("%d", &N);
	idx = 0;
	sum = 0;
	while (N--)
	{
		scanf("%d", &H);
		while(idx && S[idx - 1] <= H)
			idx--;
		sum += idx;
		S[idx] = H;
		idx++;
	}
	printf("%lld", sum);
}
