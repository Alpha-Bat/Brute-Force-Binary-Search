N = list(map(int,input().split()))
M = list(map(int,input().split()))
answer = []
dic = {}
for i in N:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
N.sort()
for target in M:
    num = 0
    start = 0
    end = len(N)-1
    while start <= end:
        mid = (start + end) // 2
        if N[mid] < target:
            start = mid + 1
        elif N[mid] > target:
            end = mid - 1
        else:
            num = dic[target]
            break
    answer.append(num)
print(*answer)
