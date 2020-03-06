#task1

class Tribonachi:
    def __init__(self):
        self.l = [0,0,1]
    def __iter__(self):
        for i in range(0, 36):
            if i < 3:
                yield self.l[i]
            else:
                self.l.append((self.l[i - 1] + self.l[i - 2] + self.l[i - 3]))
                yield self.l[i]

list = Tribonachi()
for i in list:
    print(i)


#task2

'''class Leibnic:
    def __init__(self):
        self.end = 0.75
        self.sum=0
        self.i=0

    def __iter__(self):
        while round(self.sum, 2) != self.end:
            value = ((-1) ** self.i) / (2 * self.i + 1)
            self.sum += value
            self.i += 1
            yield value


Leibnic = Leibnic()
for i in Leibnic:
    print(i)'''
