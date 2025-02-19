cases = int(input().rstrip())
for i in range(cases):
    
    num = 0
    
    scores = input().strip().split(' ')
    scores = [int(val) for val in scores]
    
    for i in range(len(scores)):
        if scores[i] > scores[num]:
            num = i
    
    print(scores[num])
