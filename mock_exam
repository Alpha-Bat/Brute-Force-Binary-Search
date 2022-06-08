def solution(answers):
    answer = []
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    a_s = b_s = c_s = 0
    for i in range(len(answers)) :
        if answers[i] == a[i%5] :
            a_s += 1
        if answers[i] == b[i%8] :
            b_s += 1
        if answers[i] == c[i%10] :
            c_s += 1
    if max(a_s,b_s,c_s) == a_s :
        answer.append(1)
    if max(a_s,b_s,c_s) == b_s :
        answer.append(2)
    if max(a_s,b_s,c_s) == c_s :
        answer.append(3)
    return answer
