############################################ FIBONACCI FUNCTION + SUPER FIBONACCI
def Fibonacci(n):
    if n<=0:
        print "None"
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


def super_fibonacci(n, m):
	my_list=[]
	while m != 0:
		my_list.append(1)
		m=m-1
	second_list=len(my_list)-1
	while len(my_list) < n:
		my_list.append(sum(my_list[-1-second_list:]))
	return(my_list[-1])





def super_fibonacci(n, m):
    if n <= m:
        return 1
    else:
        summa=0
        for i in range(1, m+1):
            previous=super_fibonacci(n-i,m)
            summa=summa+previous
        return summa