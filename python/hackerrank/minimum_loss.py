# https://www.hackerrank.com/challenges/minimum-loss?utm_source=medium-challenge&amp;utm_medium=email&amp;utm_campaign=featured-challenge-may-2017

n_str = input()
n = int(n_str)
i = 0
p = []
for x in input().split():
    p.extend([(int(x),i)])
    i += 1
    
p.sort()

min_los = -10**16

j = 1
k = 0
while j < n and k < n-1:
    if p[j][1] < p[k][1]: diff = p[k][0] - p[j][0] #j-bay k-sell
    else: diff = p[j][0] - p[k][0]
    if diff < 0 and diff > min_los:  min_los = diff # loss!
    if k == j-1: j += 1
    else: k += 1
print(-min_los)  