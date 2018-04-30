import sys


class ExtendedList(list):

    def Reversed(self):
        return ExtendedList(self[::-1])

    def First(self):
        return self[0]

    def Last(self):
        return self[-1]

    def Size(self):
        return len(self)

    def __getattr__(self, name):
        if (name == "first" or name == "F"):
            return self.First()
        elif (name == "last" or name == "L"):
            return self.Last()
        elif (name == "reversed" or name == "R"):
            return self.Reversed()
        elif (name == "size" or name == "S"):
            return self.Size()
        else:
            raise AttributeError

    def __setattr__(self, name, value):
        if (name == "first" or name == "F"):
            self[0] = value
        elif (name == "last" or name == "L"):
            self[len(self) - 1] = value
        elif (name == "size" or name == "S"):
            while (len(self) > value):
                self.pop()
            while (len(self) < value):
                self.append(None)
        else:
            raise AttributeError

exec(sys.stdin.read())
