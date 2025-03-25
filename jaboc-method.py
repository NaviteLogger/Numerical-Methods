import math

print("Jacobi")
x=[1,0,0]
xpom=[0,0,0]
xk=[0,0,0]
epsilon=0.005
norm=9.
b=[3000,5000,7000]
A=[[10.,1.,1.],[1.,11.,1.],[1.,1.,12.]]
while(True):
    norm = 0
    xpom=xk
    xk=[0,0,0]
    for i in range(len(xk)):
        for j in range(len(xk)):
            if i!=j:
                xk[i]=xk[i]-x[j]*A[i][j]
            if i==j:
                xk[i]=xk[i]+b[i]
        xk[i]=xk[i]/A[i][i]
    x=xpom
    for i in range(len(x)):
        norm=norm+(x[i]-xk[i])*(x[i]-xk[i])
    norm=math.sqrt(norm)
    if(norm<=epsilon):
        break
    print(xk)