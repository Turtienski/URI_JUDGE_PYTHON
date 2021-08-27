N = int(input())

for case in range(N):
    n, k = [int(i) for i in input().split()]
    r = [0]*n
    for i in range(len(r)):
        r[i] = i+1
    j = 0
    while len(r) != 1:
        while j < len(r):
            j = j + k 

    print("Case {}: {}".format(case+1, r[0]))    
