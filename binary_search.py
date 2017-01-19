class BinarySearch(list):
  
  def __init__(self, a, b):
    self.a = a
    self.b = b    
    for i in range(1,a+1):
      # print("i: %s and b: %s" %(i,b))
      self.append(i*b)

    self.length = len(self)

    
  """
  Given an array A of n elements with values or records A0 ... An−1,
  sorted such that A0 ≤ ... ≤ An−1, and target value T, the following
  subroutine uses binary search to find the index of T in A.
  
  1. Set L to 0 and R to n − 1.
  2. If L > R, the search terminates as unsuccessful.
  3. Set m (the position of the middle element) to the floor (the largest previous integer) of (L + R)/2.
  4. If Am < T, set L to m + 1 and go to step 2.
  5. If Am > T, set R to m – 1 and go to step 2.
  6. Now Am = T, the search is done; return m.
  """
  def search(self, val):
    self.sort() # sort the list first
    left = 0
    right = self.length - 1
    
    count = 0
    while 1:
      count+=1
      # print("count ",count)

      if left > right:
        # print("%d > %d"%(left, right))
        print("404 %s Not found" %val)
        return {'count':count, 'index':-1}
      
      middle = (left + right) // 2
      # print("left: %s middle: %s right: %s " %(left,middle,right))
      # print("middle val: ",self[middle])
      # print("val: ",val)
      if self[middle] < val:
        left = middle + 1
      elif self[middle] > val:
        right = middle - 1
      elif self[middle] == val:
        return {'count':count, 'index':self.index(val)}

# one_to_twenty = BinarySearch(20, 1)
ten_to_thousand = BinarySearch(100, 10)
# print(one_to_twenty)
# print(one_to_twenty.length)
print(ten_to_thousand)
print(ten_to_thousand.length)
print(ten_to_thousand.search(40))
print(ten_to_thousand.search(880))
print(ten_to_thousand.search(10000))

