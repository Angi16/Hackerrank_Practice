edgelength=6

def BFS(arr,que,start):
    while len(que)>0:
        current=que.pop(0)
        for i in range(len(arr)):
            if visited[i]==False and arr[current][i]==1:
                distance[i]=distance[current]+edgelength
                que.append(i)
                visited[i]=True
    distance.pop(start-1)
    for i in range(len(distance)):
        if distance[i]==0:
            distance[i]=-1
    print(" ".join(str(e) for e in distance))

T=int(input())
for testcase in range(T):
    s=input().split()
    N=int(s[0])
    M=int(s[1])
    adj=[[0 for i in range(N)] for j in range(N)]
    visited=[False for i in range(N)]
    distance=[0 for i in range(N)]
    queue=[]
    for m in range(M):
        s=input().split()
        x=int(s[0])
        y=int(s[1])
        adj[x-1][y-1]=1
        adj[y-1][x-1]=1
    start=int(input())
    visited[start-1]=True
    queue.append(start-1)
    BFS(adj,queue,start)