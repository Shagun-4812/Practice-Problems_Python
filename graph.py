from matplotlib import pyplot as plt

class undirectedgraph:
    def __init__(self,nodes=None):
        self.nodes=nodes
        self.adjacent={}
        if isinstance(nodes, int)==True:
            for i in range(self.nodes):
                self.adjacent[i+1]=[]

        self.noedges=0

def addNodes(self,a):
    self.a=a
    if self.nodes==None:
        self.nodes=self.a
        for i in range(1,self.nodes+1):
            self.adjacent[i+1]=[]

    elif self.a>self.nodes:
        raise  Exception("The number of nodes cannot be greater than the number of nodes in the graph")
    else:
        se



    def __str__(self):
        output="Graph with{node} nodes and {n} edges. Neighbpours of the nodes are below\n".format(node=len(self.adjacent), n=self.noedges, )
        for i in self.adjacent.items:
