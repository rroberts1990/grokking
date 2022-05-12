

class Subsets:

    def subsets(self, input):
        subsets = [[]]
        for i in input:
            n = len(subsets)
            for j in range(n):
                set1 = list(subsets[j])
                set1.append(i)
                subsets.append(set1)
        return subsets


