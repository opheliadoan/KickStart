# calculate sum[i][x]: sum of first x plates from stack i
def sum(v, r, c):
	if r == 0 or c == 0:
		return 0
	return v[r-1][c-1] + sum(v, r, c-1)

def dp(v, n, k, p):
	tmp = [[0 for c in range(p+1)] for r in range(n+1)]
	#print(tmp)
	for i in range(1, n+1):
		for j in range(0, p+1):
			for x in range(0, min(j, k)+1):
				tmp[i][j] = max(tmp[i][j], sum(v, i, x) + tmp[i - 1][j - x])
	return tmp[n][p]
	
t = int(input())
for i in range(t):
	n, k, p = list(map(int, input().split()))
	v = []
	for j in range(n):
		tmp = list(map(int, input().split()))
		v.append(tmp)
	print('Case #{}: {}'.format(i+1, dp(v, n, k, p)))
	
	
	



