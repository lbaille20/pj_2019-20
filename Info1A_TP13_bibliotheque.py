from copy import deepcopy

#Matrices du TP13
A1=[[3,-1,2],[5,0,0],[1,2,4]]
A2=[[1,2],[3,4]]
A30=[[1,2,3],[4,5,6],[7,8,9]]
A31=[[1,2,3],[-4,5,-6],[7,8,9]]
A32=[[1,2,3],[4444,5,6],[7,8,9]]

A3=[[1.,1.,1.],[2.,2.,2.],[3.,3.,3.]]
A4=[[3.,2.,1.],[5.,5.,5.],[7.,8.,9.]]
A5=[[1.,2.,3.],[4.,5.,6.],[7.,8.,9.]]

A6=[[3.,-1.,2.],[5.,2.,0.],[1.,2.,4.]]
B6=[[0.,2.,-2.],[1.,-1.,1.],[2.,1.,3.]]
C1=[[3.,-1.,222.],[5.,2.,0.],[1.,2000.,4.]]
C2=[[0.01,1.,1.],[1.,1.,2.],[0.,1.,2.]]
C3=[[1e-16,1.,1.],[1.,1.,2.],[0.,1.,2.]]

A9=[[2,1,-1],[1,1,1],[1,0,-1]]
B9=[3,-1,2]
A9aug=[[2,1,-1,3],[1,1,1,-1],[1,0,-1,2]]

A10=[[1.,2.,3.,4.],[0.,1.,2.,3.],[0.,0.,1.,2.],[0.,0.,0.,1.]]

A11a=[[2.,1.,-1.,3.],[1.,1.,1.,-1.],[1.,0.,-1.,2.]]
A11b=[[1e-16,1.,1.],[1.,1.,2.]]

A12c=[[2.,1.,-1.],[1.,1.,1.],[1.,0.,-1.]]
A12c_aug=[[2.,1.,-1.,1.,0.,0.],[1.,1.,1.,0.,1.,0.],[1.,0.,-1.,0.,0.,1.]]



#Fonctions du TP13
def matf(A):
    n,p=len(A),len(A[0])
    #ne pas faire
    Af=[['']*p]*n
    #mais
    Af=[['' for j in range(p)] for i in range(n)] 
    for i in range(n):
        for j in range(p):
            Af[i][j]=float(A[i][j])
    return Af
#ou bien
def matf(A):
    n,p=len(A),len(A[0])
    Af=[] 
    for i in range(n):
        Af.append([])
        for j in range(p):
            Af[i].append(float(A[i][j]))
    return Af

def mat_print(A):
    for line in A:
        print(line)

def mprint(A, decoration = (True, '*')):
    lg_max=1
    for ligne in A:
        for coefficient in ligne:
            if len(str(coefficient))>lg_max:
                lg_max= len(str(coefficient))
    for ligne in A:
        print ("|",end=' ')
        for coefficient in ligne:
            print(" "*(lg_max-len(str(coefficient)))+str(coefficient)+" ",end='')
        print ("|")
    if decoration[0]:
        print(decoration[1]*((1 + lg_max) * len(A[0]) + 3))

def cprint(A, decoration = (True, '*')):
    lg_max=1
    for ligne in A:
        for coefficient in ligne:
            if len(str(coefficient))>lg_max:
                lg_max= len(str(coefficient))
    for ligne in A:
        print ("|",end=' ')
        for coefficient in ligne:
            espaces=(lg_max-len(str(coefficient)))
            avant,après=espaces-espaces//2,espaces//2
            print(" "*avant+str(coefficient)+" "*après+" ",end='')
        print ("|")
    if decoration[0]:
        print(decoration[1]*((1 + lg_max) * len(A[0]) + 3))

def permut(A,i,j):
    for k in range(len(A[0])):
        tmp=A[i][k]
        A[i][k]=A[j][k]
        A[i][k]=tmp
#ou
def permut(A,i,j):
    for k in range(len(A[0])):
        A[i][k],A[j][k]=A[j][k],A[i][k]

def permut(A,i1,i2):
    temp=A[i1]
    A[i1]=A[i2]
    A[i2]=temp

def permut(A,i1,i2):
    A[i1],A[i2]=A[i2],A[i1]
    

def dilat(A,i,mu):
    ncols=len(A[0])
    for j in range(ncols):
        A[i][j]=mu*A[i][j]

def transvect(A,i,j,mu):
    ncols=len(A[0])
    for k in range(ncols):
        A[i][k]=A[i][k]+mu*A[j][k]
