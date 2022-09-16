class TinyStatistician():
    def __init__(self):
        pass

    def mean(self, x):
        if (len(x) == 0):
            return None
        return float(sum(x) / len(x))
    
    def median(self, x):
        x.sort()
        if (len(x) % 2 == 0):
            return (float(x[int(len(x) / 2)] + x[int(len(x) / 2) - 1]) / 2)
        return float(x[int(len(x) / 2)])

    def quartile(self, x):
        x.sort()
        return ([self.median(x[1:len(x) // 2]), self.median(x[len(x) // 2:])])
    
    def var(self, x):
        if (len(x) == 0):
            return None
        mean = self.mean(x)
        return sum([(i - mean) ** 2 for i in x]) / len(x)

    def std(self, x):
        if (len(x) == 0):
            return None
        return self.var(x) ** 0.5