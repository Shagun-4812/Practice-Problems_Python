from matplotlib import pyplot as plt
class undirectedgraph:                           #creating class undirectedgraph
    def __init__(self,nodes=None):
        self.nodes=nodes
        self.adjacent = {}                      #dictionary for storing nodes and neighbors
        if isinstance(nodes,int)==True:
            for i in range(self.nodes):         #addind list to each node for storing adjacent vertices
                self.adjacent[i+1]=[]
                
        self.noedges=0                     #setting it zero to count
        

        
    def addNodes(self,a):                      #add node funtion
        self.a=a
            
        if self.nodes==None:                   #if add have arguments we are setting value to it
            self.nodes=self.a
            self.adjacent[self.a]=[]
            for i in range(1,self.nodes+1):
                self.adjacent[i]=[]
            
        elif self.a>self.nodes:              #throughing exception if nodes is greater than existing nodes
            raise Exception('Node index cannot exceed number of nodes')    
            
        else:
            self.nodes=self.nodes+self.a           #adding extra nodes if condition is fulfil
            for i in range(1,self.nodes+1):
                self.adjacent[i]=[]
        
    def addEdges(self,b,c):                      #add edge function
        
        self.b=b
        self.c=c
        self.noedges+=1                           #adding edges for each call of function
        
        if self.nodes==None:                        #if no nodes are avail we are adding new nodes to graph
            self.adjacent[self.b]=[]
            self.adjacent[self.b].append(self.c)
            self.adjacent[self.c]=[]
            self.adjacent[self.c].append(self.b)
            
            
            self.nodes=len(self.adjacent.keys())
        else:                                     #else looking for existing nodes adding edges to them
            allkeys=self.adjacent.keys()
            if self.b in allkeys:
                self.adjacent[self.b].append(self.c)
            else:
                self.adjacent[self.b]=[]
                self.adjacent[self.b].append(self.c)
            if self.c in allkeys:
                self.adjacent[self.c].append(self.b)
            else:
                self.adjacent[self.c]=[]
                self.adjacent[self.c].append(self.b)   
                
            
        
        
    def __add__(self,others):                     # overiding addition 
        self.others=others
        
        if type(others)==int:                     #if passed argument is of type integer it will be a nodes
            allkeys=self.adjacent.keys()          #have all keys that is nodes
            if self.others in allkeys:            #checking whether it exist in nodes or not
                True
            else:
                self.adjacent[self.others]=[]
        elif type(others)==tuple:                  #if type is tuple then we are doing add edge things
            #self.others=others
            #listother=list(self.others)
            g.addEdges(others[0],others[1])
        else:
            raise Exception('entered value is not valid')      #else throughing exception 
            
        
    def __str__(self):   
                                                         #overriding class 
        output = "Graph with {node} nodes and {n} edges. Neighbours of the nodes are belows:\n".format(
            node=len(self.adjacent),
            n=self.noedges,
        )
        for i,j in self.adjacent.items():                  # printing key,value for each item using two variable loop
            output += "Node {n}: {neigh}\n".format(
                n=i, neigh=j
            )
        return output
    def plotDegDist(self):                                  #ploting part
        degnk=[]                                         #storing degree of nodes
        degdist=[]                                        # will store distribution of degree
        allkeys=self.adjacent.keys()                    #storing all keys
        for i in allkeys:                                 #for each key appending its degree to degnk
            
            degnk.append(len(self.adjacent[i]))
        avgdis=(sum(degnk))/len(degnk)                   #average of degree distribution
        for i in range(len(degnk)):
            h=0
            for j in degnk:                            #finding degree distribution of each degree
                if i==j:
                    h+=1/len(degnk)
            degdist.append(h)                          #append it in degdis
        y=degdist                                    #ploting part
        x=[i for i in range(len(degnk))]
        plt.xlabel('Node Degree')
        plt.ylabel('Fraction of Nodes')
        plt.axvline(x = avgdis, color = 'r',label='Avg. node degree')
        plt.scatter(x,y,label='Actual degree distribution')        #scattering
        plt.legend()
        plt.grid()
        plt.show()
                    
            
                  
g=undirectedgraph()
g.addNodes(4)
g+100
g+(1,2)
g+(1,100)
g+(100,3)
#g+(4,6)
g+20
p=g.plotDegDist()


print(g)