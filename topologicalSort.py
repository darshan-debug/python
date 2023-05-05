#topological sort is a linear ordering, and is possible only if graph is  DAG(directed acyclic graph)
#for every directed edge uv, vertex u comes before v in the ordering
#its a application of dfs

class Graph:
    def __init__(self,n,givenEdges,unDirected):
        self.n=n
        self.edge={}
        if(unDirected):
            print(" topological sort is not possible!!")
        for x,y,z in givenEdges:
            if(x not in self.edge):
                self.edge[x]={}
            self.edge[x][y]=z
        print("edges in graph:",self.edge)
        self.f={} #finish  time of each node, ie when all child nodes r processed, then the parnt node reaches finishing time
    def topologicalSort(self): # O(V+E)
        def initialise():
            for fromm,x in self.edge.items():
                self.f[fromm]=float("inf")
                for to,dist in x.items():
                    self.f[to]=float("inf")
               
        def dfs(s): # t is time
            nonlocal visited,t
            visited.add(s)
            print("visited :",s,", t:",t)
            if(s not in self.edge):
                self.f[s]=t
                print("finishing time of ",s," is: ",t)                
                return
            for to,dist in self.edge[s].items():
                if(to not in visited):
                    t+=1
                    dfs(to)
                    t+=1
            self.f[s]=t
            print("finishing time of ",s," is: ",t)
        #algo begins
        initialise()
        visited=set()
        t=0
        
        for i in self.f.keys(): #go to each vertex, and if its not visited, start dfs from there
            
            if(i not in visited):
                print("start dfs for node: ",i)
                t+=1 #suppose dfs started with "c",then we come to "f", thus to ensure "f" has bigger
                #finishing time, I am doing t+=1
                dfs(i)
        
        linearOrdering=list(self.f.keys())
        linearOrdering.sort(key=lambda x:self.f[x],reverse=True)
        print("linearOrdering : ",linearOrdering)
        print("finish timings:",self.f)
if(__name__=="__main__"):
    graphedges=[
    ["c","d",10],["f","c",4],["f","a",8],["e","a",7],["e","b",9],
    ["d","b",2]
    
    ] # the dist between 2 nodes does not matter in topological sort
    print("see dig of graph saved near code folder")
    obj=Graph(6,graphedges,False) #graph must be directed
    obj.topologicalSort()
    ######################################################################
    graphedges=[
    ["t","y",4],["t","z",6],["t","x",8],["x","y",7],["y","z",9],
    ["s","x",2],["r","t",3],["x","z",1],["r","s",10],["s","t",4]
    
    ] # the dist between 2 nodes does not matter in topological sort
    print("\n\n\nsee dig of graph saved near code folder,named 'topological sort2'")
    obj2=Graph(6,graphedges,False) #graph must be directed
    obj2.topologicalSort()



        
            
        
            
            
            
        
            
        