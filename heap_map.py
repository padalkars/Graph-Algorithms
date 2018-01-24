
class BinHeap:
	def __init__(self):
		self.heapList = [0]
		self.currentSize = 0
	
	def heapify(self, smallest, i):
		if(i==0):
			return
		parent = int((i-1)/2)
		if(self.heapList[i]< self.heapList[parent]):
			self.heapList[parent] = self.heapList[i] + self.heapList[parent]
			self.heapList[i] = self.heapList[parent] - self.heapList[i]
			self.heapList[parent] = self.heapList[parent] - self.heapList[i]
			smallest = self.heapList[parent]
		self.heapify(smallest, parent)

	def insert(self, ele):
		self.heapList.append(ele)
		l = len(self.heapList)
		self.heapify(ele, l-1)
		print(self.heapList)
	
	def buildHeap(self,alist):
		
		for ele in (alist):
			self.insert(ele)
	
bH = BinHeap()
bH.buildHeap([5,9,11,14,18,19,21,33,17,27])
bH.insert(9)
bH.insert(1)
bH.insert(3)

		
