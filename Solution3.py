# T: test cases
# N K: N sessions, max additional sessions K
# N integers M_i: number of minutes to exercise in i-th session
# Output: Case #x: y : x starts from 1
# T <= 10: 2 <= N <= 10^5
# o/w: 2 <= N <= 300
# 1 <= M_i <= 10^9
# M_i < M_{i+1} for all i
import math

def difficulty(N, M):
	dif = 0
	index = 0
	for i in range(N-1):
		if dif < (M[i+1] - M[i]):
			dif = M[i+1] - M[i]
			index = i
	#print(dif)
	return dif, index

def opt(low, high, K, d, prev):
	if high <= low:
		if prev != 0:
			return(prev)
		return 0
	mid = math.floor((high+low)/2)
	sum = 0
	for i in range(N - 1):
		sum += math.ceil(d[i]/mid) - 1
	if sum == K:
		return(mid)
	elif sum < K:
		return opt(1, mid, K, d, mid)
	else:
		if prev != 0:
			#print('prev: {}'.format(prev))
			return(prev)
		return(opt(mid, high, K, d, 0))
	


def set2(N, M, K):
	dif, index = difficulty(N, M)
	d = []
	for i in range(N - 1):
		d.append(M[i+1] - M[i])
	return(opt(1, dif, K, d, 0))
	

T = int(input())
for i in range(T):
	N, K = list(map(int, input().split()))
	M = list(map(int, input().split()))
	
	print('Case #{}: {}'.format(i+1, set2(N, M, K)))
	#set2(N, M, K)
	#print(M)