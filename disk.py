# cook your dish here
s='1850, 751, 2069, 212, 2296, 3800, 544, 1618, 356, 5135, 1523, 4965, 3681, 2756'

s=list(map(int,s.split(',')))
visited=[0 for i in range(len(s))]
def fcfs():
    curr=1850
    diff=0
    for i in range(1,len(s)):
        print(curr,' - ',s[i],', the sum is ',diff+abs(curr-s[i]),' diff is ',abs(curr-s[i]))
        x=abs(curr-s[i])
        diff+=x
        curr=s[i]


    print(s)
    print(diff)
    return diff

def findvisited(index):

    t=index
    x=123123123
    while(t>=0):
        if(visited[t]==0):
            x=abs(s[t]-s[index])
            break

        t=t-1


    f=index
    y=123123123
    while(f<len(s)):
        if(visited[f]==0):
            y=abs(s[f]-s[index])
            break

        f=f+1
    if(x<y):
        return t
    else:
        return f


def shortestjob():
    s.sort()

    for i in range(len(s)):
        if(s[i]==1850):
            index=i
            break

    visited[index]=1
    print(s)
    diff=0
    for i in range(len(s)-1):
        r=findvisited(index)
        x=abs(s[r]-s[index])
        diff+=x
        print(s[r],' - ',s[index],'the sum is ',diff+abs(s[index]-s[r]),' diff is ',diff)
        index=r
        visited[r]=1

    print(diff)
    return diff
fcfs()
if __name__=='__main__':
    fcfs()
    shortestjob()
