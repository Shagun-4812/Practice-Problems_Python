class rod(object):
    def __init__(self, n, p):
        self.p = p
        self.n = n
        self.S = [[0] * (n + 1) for _ in range(len(p) + 1)]

    def solve(self):
        for i in range(1, len(self.p) + 1):  # Fix range to include all prices
            for j in range(self.n + 1):  # Iterate over rod lengths
                if i <= j:
                    self.S[i][j] = max(self.S[i - 1][j], self.p[i - 1] + self.S[i][j - i])
                else:
                    self.S[i][j] = self.S[i - 1][j]

    def show_result(self):
        print("The maximum value is", self.S[len(self.p)][self.n])

def main():
    r = rod(5, [2, 5, 7, 3, 9])
    r.solve()
    r.show_result()

if __name__ == '__main__':
    main()
