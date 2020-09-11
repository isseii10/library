
# 一点更新区間取得
class segmentTree:
    def __init__(self, init_val, operator, identity):
        """
        :param init_val: 操作したい配列
        :param operator: 演算子(minはそのままでok。sumはlistを引数にとるからエラー->add関数を自作)
        :param identity: 演算子に対応する単位元(minならinf,sumなら0)
        """
        self.identity = identity
        self.operator = operator

        n = len(init_val)
        n_bin = bin(n)[2:]
        bc = sum([int(digit) for digit in n_bin])
        if bc == 1:  # 2のべき乗ならすっぽり入る
            self.num_end_leaves = 2**(len(n_bin)-1)
        else:  # 2のべき乗でないなら、はみ出すからー１しない
            self.num_end_leaves = 2**len(n_bin)

        self.tree = [identity for _ in range(self.num_end_leaves * 2)]
        # 葉に要素をセット
        for i in range(n):
            self.tree[i + self.num_end_leaves] = init_val[i]
        # segtree構築
        for i in range(self.num_end_leaves)[::-1]:
            self.tree[i] = self.operator(self.tree[2*i], self.tree[2*i+1])

            
    def update(self, x, val):
        """
        :param x: 更新するidx
        :param val: 更新する値
        """
        leaf_x = x + self.num_end_leaves
        self.tree[leaf_x] = val
        while leaf_x > 0:
            leaf_x //= 2
            self.tree[leaf_x] = self.operator(self.tree[leaf_x*2], self.tree[leaf_x*2+1])
            # operaterがminだったりsumだったりする
    
    
    def query(self, left, right):
        """
        :param left: queryの左
        :param right: queryの右
        """
        left += self.num_end_leaves
        right += self.num_end_leaves
        val_l = val_r = self.identity
        while right - left > 0:
            if left & 1:
                val_l = self.operator(val_l, self.tree[left])
                left += 1
            if right & 1:
                right -= 1
                val_r = self.operator(self.tree[right], val_r)
            left >>= 1
            right >>= 1
        return self.operator(val_l, val_r)
