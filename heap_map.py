
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
		
	
	def buildHeap(self,alist):
		
		for ele in (alist):
			self.insert(ele)
	
	def perDown(self,i):
		if(2*i+1 > len(self.heapList)):
			return

		smallest = self.heapList[i]
		
		if(self.heapList[2*i+1]<smallest):
			ind = 2*i + 1
			smallest = self.heapList[2*i + 1]
		elif(self.heapList[2*i + 2]<smallest):
			ind = 2*i + 2
			smallest = self.heapList[2*i + 2]

		if(smallest != self.heapList[i]):
			self.heapList[i] = self.heapList[i] + self.heapList[ind]
			self.heapList[ind] = self.heapList[i] - self.heapList[ind]
			self.heapList[i] = self.heapList[i] - self.heapList[ind]
			self.perDown(ind)			

	def delMin(self):
		m = self.heapList[0]
		self.heapList[0] = self.heapList[len(self.heapList)-1]
		(self.heapList).pop(len(self.heapList)-1)
		self.perDown(0)
		return m

bH = BinHeap()
bH.buildHeap([5,9,11,14,18,19,21,33,17,27])
bH.insert(9)
bH.insert(1)
bH.insert(3)
print(bH.heapList)
print("Deleting the minimum element")
print(bH.delMin())
print("The updated list")
print(bH.heapList)


