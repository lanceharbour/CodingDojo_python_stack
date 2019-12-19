class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        for n in nums:
            self.result += n
        print("add",self.result)
        return self
    def subtract(self, num, *nums):
        self.result -= num
        for n in nums:
            self.result -= n
        print("subtract",self.result)
        return self
# create an instance:
md = MathDojo()
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)

