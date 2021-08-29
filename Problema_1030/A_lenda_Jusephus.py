N = int(input())

for case in range(N):
    n, k = [int(i) for i in input().split()]
    r = [1]*n
    proximo = k - 1
    print(r)
    for i in range(n-1):
        r[proximo] = 0 
        print(r)
        for j in range(k):
            print(j, proximo)
            proximo = proximo + 1
            if proximo >= n:
                proximo = proximo - n 
            try:
                while r[proximo] == 0:
                    proximo = proximo + 1  
            except:
                print("Case {}: {}".format(case+1, r.index(1)+1))
