
class Node:
	def __init__(self,item):
		self.item = item
		self.next = None

class Queue:

	def __init__(self):
		self.head = None
		self.tail = None

	def is_empty(self):
		return self.head == None


	def enqueue(self, item):
		if self.is_empty():
			self.head = self.tail = Node(item)
		else:
			self.tail.next = self.tail = Node(item)


	def dequeue(self):
		if self.is_empty():
			raise IndexError
		else:
			temp = self.head
			self.head = self.head.next
			return temp.item

	def peek(self):
		return self.head.item


	def size(self):
		return size_helper(self.head)

def size_helper(node):
	if node == None:
		return 0
	return 1 + size_helper(node.next)
