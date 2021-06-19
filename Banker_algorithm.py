import numpy as np
def banker(maxn,alloc,avail,N,M):
    f = [0,0,0,0,0]
    need = np.zeros((N,M))
    ans = np.zeros((5))
    for i in range(0,N):
        for j in range(0,M):
            need[i,j]= need[i,j]+(maxn[i,j]-alloc[i,j])
    count=0
    while(count<N):

        for i in range(0,N):
            if(f[i]==0):
                flag = 0
                
                sd = need[i,:]
                if(np.any(sd > avail)):
                    flag = 1
                if(flag == 0):
                    avail = avail + alloc[i]
                    f[i] = f[i]+1
                    ans[count] = ans[count] + i
                    count = count + 1
                    
                    
    flag = 0
    print('\n')
    print('The Need Matrix is:\n')
    print(' R0 R1 R2 \n')
    print(need)
    for i in range(0,N):
        if(f[i]==0):
            flag = 1
            break;
    if(flag==0):
        print('\n')
        print('Following is the safe sequence:',end = ' ')
        for i in range(0,N):
            print('p->'+str(ans[i]),end = ' ')
    return flag
N = int(input('ENTER THE NO OF PROCESS:'))
M = int(input('Enter the no of resources:'))
r_array = list()
max_need0 = list()
max_need = list()
alloc0 = list()
alloc = list()
need = list()
s=np.zeros((1,3))
s1=np.zeros((1,3))
avail0 = list()
for i in range(0,M):
    print('Enter The No. Of Instances Of Resource R'+str(i)+':')
    n = int(input())
    r_array.append(n)
for i in range(0,N):
    print('\n\nEnter the Max for P'+str(i)+':')
    for j in range(0,M):
        print('Enter the Max need for R'+str(j)+' Resource:')
        num = int(input())
        max_need0.append(num)
l = np.array(max_need0)
max_need = l.reshape(N,M)
for i in range(0,N):
    print('\n\nEnter the Alocation for P'+str(i)+':')
    for j in range(0,M):
        print('Enter the Alocation for R'+str(j)+' Resource:')
        num1 = int(input())
        alloc0.append(num1)
q = np.array(alloc0)
alloc = q.reshape(N,M)
for i in range(0,N):
    s= s+alloc[i,0:M]
avail0 = r_array - s
avail = np.array(avail0)
print('\nThe avail Matrix is:\n')
print(' R0 R1 R2 \n')
print(avail)
flag = banker(max_need,alloc,avail,N,M)
if(flag == 1):
    print('Not in the safe state!!')
else:
    re = list()
    num = int(input('\nEnter the prosses no. that request for resource:\n'))
    for j in range(0,M):
        print('\nEnter the request for resource R'+str(j)+':')
        new = int(input())
        re.append(new)
    request = np.array(re)
    need = max_need[num,:] - alloc[num,:]
    if(np.any(request>need)):
        print('\nDeny Request'+''+str(num))
    else:
        if(np.any(request>avail)):
            print('\nDeny Request'+''+str(num))
        else:
            print('\nGrant Request'+''+str(num))
            alloc[num,:] = alloc[num,:] + request
            availM = avail - request
            print('\nThe avail Matrix is:\n')
            print(' R0 R1 R2 \n')
            print(availM)
            banker(max_need,alloc,availM,N,M)
                
    
    
    
    
