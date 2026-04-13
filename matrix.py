r1=int(input("Enter no. of rows of Matrix A:"))
c1=int(input("Enter no. of columns of Matrix A:"))
r2=int(input("Enter no. of rows of matrix B:"))
c2=int(input("Enter no. of columns of matrix B:"))
if c1!=r2:
    print("Matrix multiplication not possible")
else:
    print("Matrix A:")
    A=[list(map(int,input().split()))for i in range(r1)]
    print("Matrix B:")
    B=[list(map(int,input().split()))for i in range(r2)]
    result=[]
    for i in range(r1):
        rows=[]
        for j in range(c2):
            rows.append(0)
        result.append(rows)
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j]+=A[i][k]*B[k][j]
    print("Result matrix:")
    for row in result:
        print(row)
