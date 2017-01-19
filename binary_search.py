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
	def search(self, target):
		self.sort() # sort the list first
		
		left = 0
		right = self.length - 1
		
		count = 0
		while 1:
			# print("count ",count)

			middle = ((left + right) // 2) 
			if left > right or middle > right:
				return {'count':count, 'index':-1}
			
			if self[middle] == target:
				return {'count':count, 'index':middle}
			elif self[right] == target:
				return {'count':count, 'index':right}
			elif self[left] == target:
				return {'count':count, 'index':left}
			elif middle==left or middle==right:
				return {'count':count, 'index':-1}			
			elif self[middle] < target:
				# middle = ((left + right) // 2) + 1
				left = middle + 1
			elif self[middle] > target:
				# middle = ((left + right) // 2)
				right = middle - 1
			count+=1

