# O(ElogV) time complexity
class Graph:
    def __init__(self,n,givenEdge):
        self.v=n #no of nodes
        self.edge={} #edge weights
        for x,y,z in givenEdge:
            if(x not in self.edge):
                self.edge[x]={}
                self.edge[x][y]=z
            else:
                self.edge[x][y]=z
        print(self.edge)
        #the below 2 will change based on source
        self.d={} #upper bound on weight of shortest path from source to "any v"
        self.pre={} # predecessor node, for each node "v"
    def dijkstra(self,s): #single source shortest path from node s, to all nodes
        # all edge weights MUST BE +ve
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
        #algo begins
        initialise(s) # s is starting node
        queue=list(self.d.keys()) # I will sort it after every loop, thus it behaves like a priority queue
        # queue has list oof all nodes present in graph
        visited=set() # to mark nodes, already processed(taken out from queue)
        
        while(queue):
            queue.sort(key=lambda x:self.d[x])
            bestNode=queue[0]
            queue=queue[1:] #poping from queue
            visited.add(bestNode) #its not needed actually, just given in algo so i did
            for x in self.edge[bestNode].keys():
                relax(bestNode,x)
            #remember each edge is relaxed, only once.....not so in bellman ford
        print("given source node: ",s)
        print("shortest dist from given source:",self.d)
        print("predessor node for each node:",self.pre)

############################################################################################################3
if(__name__=="__main__"):
    graphedges=[

    ["s","t",10],["s","y",5],["t","y",2],["y","t",3],["y","z",2],["y","x",9],
    ["t","x",1],["x","z",4],["z","x",6],["z","s",7]  
    
    ]
    obj=Graph(5,graphedges)
    obj.dijkstra("s")
    #obj.dijkstra("x")
        
            
            
            
            
        
                
            
        
            
        