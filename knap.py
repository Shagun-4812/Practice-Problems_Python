class knapsack:
    def __init__(self,n,M,w,v):
        self.n = n
        self.M = M
        self.w = w
        self.v = v
        self.S = [[0 for _ in range(M+1)] for _ in range(n+1)]
    def solve(self):
        for i in range(1,self.n+1):
            for j in range(1,self.M+1):
                not_taking_item=self.S[i-1][j]
                taking_item=0
                if self.w[i]<=self.w:
                    taking_item=self.S[i-1][j-self.w[i]]+self.v[i]    
                self.S[i][j]=max(not_taking_item,taking_item)
    def show_result(self):
        print("The maximum value is ",self.S[self.n][self.M])
def main(): 
    
    k = knapsack(3,5,[4,2,3],[10,4,7])
    k.solve
    print(k.S)
if __name__ == '__main__':  
    main()