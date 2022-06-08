// https://www.acmicpc.net/problem/1406

#include <stdio.h>
#define MX 1000001

char		dat[MX];
int			pre[MX] = { -1, };
int			nxt[MX] = { -1, };
int			unused = 1;

void	insert(int addr, int num)
{
	dat[unused] = num;
	pre[unused] = addr;
	nxt[unused] = nxt[addr];
	if (nxt[addr] != -1)
		pre[nxt[addr]] = unused;
	nxt[addr] = unused;
	unused++;
}

void	erase(int addr)
{
	nxt[pre[addr]] = nxt[addr];
	if (nxt[addr] != -1)
		pre[nxt[addr]] = pre[addr];
}

void	traversal(void)
{
	int	cur;

	cur = nxt[0];
	while (cur != -1)
	{
		printf("%c", dat[cur]);
		cur = nxt[cur];
	}
}

int	main(void)
{
	char	str[1000001];
	int		M;
	char	op, ch;
	int		i;
	int		cursor;

	scanf("%s", str);
	i = 0;
	cursor = 0;
	while (str[i] != '\0')
	{
		insert(cursor, str[i]);
		cursor++;
		i++;
	}
	scanf("%d", &M);
	while (M--)
	{
		scanf(" %c", &op);
		if (op == 'P')
		{
			scanf(" %c", &ch);
			insert(cursor, ch);
			cursor = nxt[cursor];
		}
		else if (op == 'L')
		{
			if (pre[cursor] != -1)
				cursor = pre[cursor];
		}
		else if (op == 'D')
		{
			if (nxt[cursor] != -1)
				cursor = nxt[cursor];
		}
		else
		{
			if (pre[cursor] != -1)
			{
				erase(cursor);
				cursor = pre[cursor];
			}
		}
	}
	traversal();
}
