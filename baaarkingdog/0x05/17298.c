// https://www.acmicpc.net/problem/17298

#include <stdio.h>
#define MX 1000001

int	A[MX];
int	S[MX];
int	L[MX];

int	main(void)
{
	int	N;
	int	idx, i;

	scanf("%d", &N);
	i = 0;
	while (i < N)
	{
		scanf("%d", &L[i]);
		A[i] = -1;
		i++;
	}
	i = 0;
	idx = 0;
	while (i < N)
	{
		while (idx && L[S[idx - 1]] < L[i])
		{
			A[S[idx - 1]] = L[i];
			idx--;
		}
		S[idx] = i;
		idx++;
		i++;
	}
	i = 0;
	while (i < N)
		printf("%d ", A[i++]);
}

// 전역 변수로 설정하니 세그폴트 문제 해결됨.
// 사실 위 코드는 스택이 아니라 배열이기 때문. 진정한 스택은 인덱스를 움직이지 않는다.
// 지역변수는 스택 메모리에 할당되고, 전역변수는 힙메모리에 할당되기 때문.
// 전역배열이 동적 할당에 비해 약간 빠르기도 하다고...
// 따라서 배열이 스택에 잡히지 않게 조심해야 한다.
// https://www.acmicpc.net/board/view/5437
// 그리고 파이썬보다 채점 속도 1.5배 빠른듯
