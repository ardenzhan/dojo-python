## without OOP
# def add1(num):
#   num = num + 1
#   return num

# myNum = add1(5)
# print myNum

## with OOP
class MyNumber(object):
  def __init__(self, num=10):
    self.num = num
    print "hi"

  def add1(self):
  	self.num +=1
  	print "i am normal add1"

myNum = MyNumber(5)
myNum.add1() 
print myNum.num
print myNum

# ## inheritance
# class MySuperNumber(MyNumber):
#   def __init__(self, num):
#     super(MySuperNumber, self).__init__(num)
#     print "I am super init"

#   def add1(self):
#     print "I am super add"
#     self.num +=3

# mySuperNum = MySuperNumber(5)
# mySuperNum.add1()
# print mySuperNum
