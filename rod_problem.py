class rod(object):
    def __init__(self, n, p):
        self.p = p
        self.n = n
        self.S = [[0] * (n + 1) for _ in range(len(p) + 1)]

    def solve(self):
        for i in range(1, len(self.p) + 1):  
            for j in range(self.n + 1):  
                if i <= j:
                    self.S[i][j] = max(self.S[i - 1][j], self.p[i - 1] + self.S[i][j - i])
                else:
                    self.S[i][j] = self.S[i - 1][j]

    def show_result(self):
        print("The maximum value is", self.S[len(self.p)][self.n])
        column_index=self.n;
        row_index=len(self.p)-1;
        while column_index>0 or row_index>0:
            if self.S[row_index][column_index]==self.S[row_index-1][column_index]:
                row_index=row_index-1
            else:
                print("We take piece of length",row_index+1,"m")
                column_index=column_index-row_index-1



def main():
    r = rod(6, [0,2, 5, 7, 3, 9])
    r.solve()
    r.show_result()

if __name__ == '__main__':
    main()
