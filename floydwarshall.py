#O(V^3) dynamic programming with memoization approach
#all pair shortest path
# youtube video link : https://www.youtube.com/watch?v=t3mf2Vu9wA4&ab_channel=MrARULSUJUD
class Graph:
    def __init__(self,n,edges):
        self.n=n
        self.edge=[ [float("inf")]*n for i in range(n)]  #we use adjacency matrix
        for x,y,dist in edges:
            self.edge[x][y]=dist
        #print(self.edge)
    def floydwarshall(self):
        for i in range(self.n):
            print(f"d{i} matrix:")
            print(self.edge)
            for x in range(self.n):
                if(x==i):# i th row, shld not be touched
                    continue
                for y in range(self.n):
                    if(y==i or x==y): # i th ,column should not be touch,same for diagonal elements
                        continue
                    self.edge[x][y]=min(self.edge[x][y],self.edge[x][i]+self.edge[i][y])
        print(f"final result: (d{i+1} matrix)")
        print(self.edge)


myedges=[[0,2,3],[2,3,1],[2,1,7],[3,0,6],[1,0,2]] # [from,to,dist]

obj=Graph(4,myedges)
obj.floydwarshall()
