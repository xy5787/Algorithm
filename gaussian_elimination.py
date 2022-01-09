import numpy as np

row_size=eval(input("행렬의 열 개수를 입력하세요 >> "))
column_size=eval(input("행렬의 칼럼 수를 입력하세요 >> "))

O=np.zeros((row_size,column_size))
O=np.mat(O)
for i in range(row_size):
  O[i]=np.asarray(eval(input("%d 번째 열의 식의 계수를 차례대로 입력하세요 >> " %(i+1))))
    
n=len(O)
for i in range(n-1):
  for k in range(i+1,n):
    O[k]=O[k]-O[k,i]/O[i,i]*O[i]
    
x=np.zeros((n,1))

A=np.hstack(tuple([O[:,k] for k in range(n)]))
b=np.hstack((O[:,n]))
b=b.T

x[n-1]=b[n-1]/A[n-1,n-1]
for i in range(n-2,-1,-1):
  sum=0
  for k in range(i+1,n):
    sum+=A[i,k]*x[k]
  x[i]=(b[i]-sum)/A[i,i]

print("=================")
for i in range(0, len(x), 1):
  print("x", (i+1), ">> ", x[i])
print("=================")