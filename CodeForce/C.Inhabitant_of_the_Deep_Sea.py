# Caution 
# Constraint is n <= 2 * 10^5
# k <= 10^15
# Point: 1. Brute Force cannot be solved
# Point: 2. Calculation is necessary
# Point: 3. Front can be removed by the half of K, Because when front value is less than K even kraken has to come back to front
# Point: 4. Divide even and odd, cause kraken can come back to front and attack front one more than end
# Point: 5. It is available to solve by the half of K because another for loop traverse ships from the end with the half of K.
ts = int(input())
while ts:
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    ans, sm = 0, sum(lst)
    if k >= sm:
        print(n)
        ts -= 1
        continue
    rem = k // 2
    if k % 2 == 0:
        pp = rem
    else:
        pp = rem + 1
    for i in range(n):
        if lst[i] <= pp:
            pp -= lst[i]
            ans += 1
        else:
            break
    pp = rem
    for i in range(n - 1, -1, -1):
        if lst[i] <= pp:
            pp -= lst[i]
            ans += 1
        else:
            break
    print(ans)        
    ts -= 1