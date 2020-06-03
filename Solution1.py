t = int(input())
for i in range(t):
	n, b = list(map(int, input().split()))
	a = list(map(int, input().split()))
	print(a)
	a.sort()
	houses = 0;
	for p in a:
		if b < p:
			break
		b = b - p
		houses+=1
	print('Case #{}: {}'.format(i + 1, houses))
