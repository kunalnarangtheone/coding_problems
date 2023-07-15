import random

class RandomSampling:
    def __init__(self, A):
        self.A = A
        self.B = dict()
        self.ele = list(A.keys())
        self.idx = dict()
        self.size = len(A)

        for i, key in enumerate(self.ele):
            self.idx[key] = i

    def sample_without_replacement(self):
        if not self.ele:
            return Exception("No elements for sampling!")

        rand = random.choice(self.ele)
        idd = self.idx[rand]
        last_id = self.size - 1

        self.ele[idd] = self.ele[last_id]
        self.idx[self.ele[idd]] = idd
        self.ele.pop()
        del self.idx[rand]
        self.size-=1

        return rand
    
    def random_sampling(self, k):
        samples = []
        if k > self.size:
            return Exception("Sample size is greater than size of data!")
        
        for i in range(k):
            samples.append(self.sample_without_replacement())

        return samples
    
r = RandomSampling({"a": 1, "b": 2, "c": 3})
print(r.random_sampling(2))
    



