class UnionFind:
    def __init__(self, n):
        self.par = [-1]*(n+1)  # 頂点番号とindexをそろえるためにn+1。idx0は使わない
        self.rank = [0]*(n+1)

    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])  # 再帰で根までたどる.その過程で根とつなぎかえる
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        else:
            if self.rank[x] < self.rank[y]:
                self.par[y] += self.par[x]
                self.par[x] = y
            else:
                self.par[x] += self.par[y]
                self.par[y] = x
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1

    def same_check(self, x, y):
        return self.find(x) == self.find(y)  # 根同じならTrue違うならFalseを返す

    def size(self, x):
        return -self.par[self.find(x)]
