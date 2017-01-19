class BinarySearch(list):
	
	def __init__(self, a, b):
		self.a = a
		self.b = b    
		for i in range(1,a+1):
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
				# Not found
				return {'count':count, 'index':-1}
			

			if self[middle] == target:
				return {'count':count, 'index':middle}
			elif self[right] == target:
				return {'count':count, 'index':right}
			elif self[left] == target:
				return {'count':count, 'index':left}
			elif self[middle] < target:
				left = middle + 1
			elif self[middle] > target:
				right = middle - 1

			if middle==left or middle==right:
				# not found
				return {'count':count, 'index':-1}
			count+=1


if __name__ == '__main__':
	# one_to_twenty = BinarySearch(20, 1)
	ten_to_thousand = BinarySearch(100, 10)
	two_to_forty = BinarySearch(20, 2)
	# print(one_to_twenty)
	# print(one_to_twenty.length)
	# print(ten_to_thousand)
	# print(ten_to_thousand.length)
	print(two_to_forty)
	# print(two_to_forty.search(16))
	# print(two_to_forty.search(40))
	print(two_to_forty.search(33))
	# print(ten_to_thousand.search(40))
	# print(ten_to_thousand.search(880))
	# print(ten_to_thousand.search(10000))

