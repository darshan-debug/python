# prims algorithm for min spanning tree
class Graph:
    def __init__(self,n,givenEdges,unDirected):
        self.n=n #no of vertices
        self.edge={}
        for x,y,z in givenEdges:
            if(x not in self.edge):
                self.edge[x]={}
                self.edge[x][y]=z
            else:
                self.edge[x][y]=z
            if(unDirected): #reverse edge possible for each edge
                if(y not in self.edge):
                    self.edge[y]={}
                    self.edge[y][x]=z
                else:
                    self.edge[y][x]=z
                
        print("edges in graph:",self.edge)
        self.d={} # this is totally different from what it used to be in dijkstra,bellmanford
        # "d" in this case represents, distance from (nearest node,which is a part of spanning tree)
        self.pre={}  # predecessor node, for each node "v"

    def prim(self,s): #to generate min spaning tree, with root s
        # assumes all edge weights are +ve
        def initialise(s):  #for each vertex, set the value of "d","pre"
            for fromm,x in self.edge.items():
                self.d[fromm]=float("inf")
                self.pre[fromm]=None
                for to,dist in x.items():
                    self.d[to]=float("inf")
                    self.pre[to]=None
            self.d[s]=0
        #algo begins
        initialise(s)
        queue=list(self.d.keys()) #all nodes present in graph
        visited=set()  # nodes which r visited,  removed from queue
        stl=0 #spanning tree length
        while(queue):
            queue.sort(key=lambda x:self.d[x])
            nearestNode=queue[0]
            visited.add(nearestNode)
            stl+=self.d[nearestNode]
            queue=queue[1:] #pop operation
            
            for to,dist in self.edge[nearestNode].items():
                if(to not in visited and self.d[to]>dist):  #already visited node, will not be visited again,to avoid cycles in spanning tree
                    self.d[to]=dist
                    self.pre[to]=nearestNode
        print("given source node: ",s)
        print("Total length of minimum spanning Tree:",stl)
        print("predessor node for each node:",self.pre)
        
if(__name__=="__main__"):
    graphedges=[
    ["a","b",4],["b","c",8],["c","d",7],["d","e",9],["e","f",10],
    ["f","g",2],["g","h",1],["h","a",8],["b","h",11],["h","i",7],
    ["i","c",2],["i","g",6],["c","f",4],["d","f",14]
    
    ] #undirected graph,thus in a edge, we can travel either direction
    print("see dig of graph ,in page no 635")
    obj=Graph(9,graphedges,True) 
    obj.prim("a")
    obj.prim("e")
    print("\ntry from any node as source-> spanning tree,min length, remains same!!")

        
                    
                
                    
                
        