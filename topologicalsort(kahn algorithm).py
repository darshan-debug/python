# it can identify presence of cycles, in graphs,and will give topological order, only is they are absent
class Graph:
    def __init__(self,n,givenEdges,unDirected):
        self.n=n
        self.edge={}
        if(unDirected):
            print("topological sort, not possible for un-directed graph!!")
        # actually speaking, we dont need dist between edges, for topological sort
        for fromm,to,dist in givenEdges:
            if(fromm not in self.edge):
                self.edge[fromm]={}
            self.edge[fromm][to]=dist
        #print(self.edge)
        self.indegree={}   # indegree of all nodes
        #self.pre={} #not needed
    def topologicalsort(self):
        def initialise():
            for fromm,x in self.edge.items():
                if(fromm not in self.indegree):
                    self.indegree[fromm]=0
                for to,dist in x.items():
                    if(to not in self.indegree):
                        self.indegree[to]=1
                    else:
                        self.indegree[to]+=1
        #algo
        initialise()
        countt=0 #number of nodes removed from queue
        queue=[i for i,j in self.indegree.items() if j==0] #it will have only those nodes, whose indegree has become/is 0
        linearOrdering=[] # the topological sorted order
        
        while(queue):
            nextnode=queue[0]
            queue=queue[1:] #pop
            if(nextnode  in self.edge):
                for to in self.edge[nextnode].keys(): #reducing inorder of all those nodes, with which it has a edge
                    self.indegree[to]-=1
                    if(self.indegree[to]==0):
                        queue.append(to)
            countt+=1
            linearOrdering.append(nextnode)
        if(countt<len(self.indegree.keys())):
            print("cycle exists!!")
            print("topological sort not possible")
        else:
            print("topological sorted order:")
            print(linearOrdering)
        
#test data

graphedges=[
    ["c","d",10],["f","c",4],["f","a",8],["e","a",7],["e","b",9],
    ["d","b",2]
    
    ] # the dist between 2 nodes does not matter in topological sort
print("see dig of graph saved near code folder")
obj=Graph(6,graphedges,False) #graph must be directed
obj.topologicalsort()
####################################################################
graphedges=[
    ["t","y",4],["t","z",6],["t","x",8],["x","y",7],["y","z",9],
    ["s","x",2],["r","t",3],["r","s",10],["s","t",4],

    ["x","z",1] 
    
    ] # the dist between 2 nodes does not matter in topological sort
print("\n\n\nsee dig of graph saved near code folder,named 'topological sort2'")
obj2=Graph(6,graphedges,False) #graph must be directed
obj2.topologicalsort()
######################################################################
graphedges=[
    ["t","y",4],["t","z",6],["t","x",8],["x","y",7],["y","z",9],
    ["s","x",2],["r","t",3],["r","s",10],["s","t",4],

    ["z","x",1]  # this last edge, i have modified, to create  a cycle
    
    ] # the dist between 2 nodes does not matter in topological sort
print("\n\n\nsee dig of graph saved near code folder,named 'topological sort2'")
obj3=Graph(6,graphedges,False) #graph must be directed
obj3.topologicalsort()

