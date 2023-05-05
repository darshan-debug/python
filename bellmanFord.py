# O(VE) time complexity
class Graph:
    def __init__(self,n,graphEdges):
        self.n=n
        self.edge={}
        for i,j,k in graphEdges:
            if(i not in self.edge):
                self.edge[i]={}
                self.edge[i][j]=k
            else:
                self.edge[i][j]=k
        print("edges in graph:",self.edge)
        self.d={} #upper bound on weight of shortest path from source to "any v"
        self.pre={} # predecessor node, for each node "v"
        
    def bellmanford(self,s): #can deal with -ve edge weights
        #will tell if a "-ve weight cycle" exists,in that case ,shortest path is not defined
        def initialise(s): #for each vertex, set the value of "d","pre"
            for fromm,x in self.edge.items():
                self.d[fromm]=float("inf")
                self.pre[fromm]=None
                for to,dist in x.items():
                    self.d[to]=float("inf")
                    self.pre[to]=None
            self.d[s]=0
        def relax(fromm,to):
            if(self.d[to]>self.d[fromm]+self.edge[fromm][to]):
                self.d[to]=self.d[fromm]+self.edge[fromm][to]
                self.pre[to]=fromm
        #algo starts
        initialise(s)        
        for i in range(self.n-1): #for n nodes,min (n-1) edges r required, to connect any 2 nodes
            #relax each edge
            for fromm,to in self.edge.items():
                for x,y in to.items():
                    relax(fromm,x)
        #by now, we relaxed each edge n-1 times
        
        #if still in any edge a relaxation is possible,
        # then there is a -ve weight cycle
        for fromm,x in self.edge.items():
                for to,dist in x.items():
                    if(self.d[to]>self.d[fromm]+dist):
                        print("-ve weight cycle,reachable from source ")
                        return False
        print("given source node: ",s)
        print("shortest dist from given source:",self.d)
        print("predessor node for each node:",self.pre)
        return True
if(__name__=="__main__"):
    print("dig on book p no 659")
    graphedges=[

    ["s","t",10],["s","y",5],["t","y",2],["y","t",3],["y","z",2],["y","x",9],
    ["t","x",1],["x","z",4],["z","x",6],["z","s",7]  
    
    ]
    obj=Graph(5,graphedges)
    obj.bellmanford("s")

    ######################
    print("######dig on book p no 646")
    graphedges=[

    ["s","e",2],["e","f",3],["f","e",-6],["f","g",7]  
    
    ]
    obj1=Graph(4,graphedges)
    obj1.bellmanford("s")
                
        
        
                
                