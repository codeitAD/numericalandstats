
def f(x):
    return x^4-x-10
    def secant_method(x0,x1,tol=1e-6,max_iter=100):
        iter_count=0
        while iter_count<max_iter:
            x2=x1-f(x1)*(x1-x0)/f(x1)-f(x0))
            if abs(x2-x1)<tol:
                return x2
                x0,x1=x1,x2
                iter_count+=1
                print("Max iterations reached")
                return x2
                x0=1
                x1=2
                root=secant_method(x0,x1)
                printf("The root is:{root}")   