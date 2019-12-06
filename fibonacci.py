######################## Recursive Approach ###########################

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

####################### Non Recursive Approach ########################

def iter_fib(n):
    n1 = 0
    n2 = 1

    if n == 0:
        return n1
    elif n == 1:
        return n2
    else:
        for i in range(2, n+1):
            nth = n1 + n2
            n1 = n2
            n2 = nth
        return nth

nterms = int(input("How many terms? "))
for i in range(nterms):
    #print(recur_fibo(i), end=",")
    print(iter_fib(i), end=",")
