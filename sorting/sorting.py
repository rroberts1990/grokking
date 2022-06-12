

class Sorting:
    def __init__(self, A):
        self.A = A
    def merge_sort(self, a=0, b=None):
        if b is None:
            b = len(self.A)

        if 1 < b - a:
            c = (b + a) // 2
            self.merge_sort(a, c)
            self.merge_sort(c, b)
            L, R = self.A[a:c], self.A[c:b]
            i, j = 0, 0
            while a < b:
                if (j >= len(R)) or (i < len(L) and L[i] < R[j]):
                    self.A[a] = L[i]
                    i += 1
                else:
                    self.A[a] = R[j]
                    j += 1
                a += 1