class Range:
    def __getitem__(self, cnt):
        pos = self.start + self.step * cnt
        if self.step >= 0:
            if pos >= self.finish:
                raise IndexError
        if self.step < 0:
            if pos <= self.finish:
                raise IndexError
        return pos

    def __contains__(self, element):
        if self.step >= 0:
            if element >= self.start and element < self.finish and (element - self.start) % self.step == 0:
                return True
        else:
            if element > self.finish and element <= self.start and (self.start - element) % self.step == 0:
                return True
        return False
    
    def __len__(self):
        a = (self.finish - self.start) // self.step 
        if (self.finish - self.start) % self.step != 0:
            a += 1
        return a
    
    def __init__(self, *args):
        if len(args) == 1:
            self.start = 0
            self.step = 1
            self.finish = args[0]
        if len(args) == 2:
            self.start = args[0]
            self.finish = args[1]
            self.step = 1
        if len(args) == 3:
            self.start = args[0]
            self.finish = args[1]
            self.step = args[2]
    
    def __repr__(self):
        return range(self.start, self.finish, self.step).__repr__()

