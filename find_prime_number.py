from itertools import permutations

def solution(numbers):
    answer = []
    notans = []
    nums = []
    for i in range(1, len(numbers)+1):
        nums += [''.join(i) for i in permutations(numbers,i)]
    for num in nums:
        n = int(num)
        if n <= 13:
            if int(num) in [2,3,5,7,11,13] and int(num) not in answer:
                answer.append(int(num))
        if n > 13:
            if int(num[len(num)-1]) in [1,3,7,9]:
                if n not in answer and n not in notans:
                    check = 0
                    for i in range(2,n):
                        if n % i == 0:
                            check = 1
                    if check == 0:
                        answer.append(n)
                    else:
                        notans.append(n)
    return len(answer)
