from queue_linked import *
from turtle import *


class TreeNode(RawTurtle):
	def __init__(self, item, left=None, right=None, canvas=None):
		self.item = item
		self.left = left
		self.right = right
		self.x = None
		self.y = None
		if canvas != None:
			super().__init__(canvas)
			self.ht()
			self.shape("circle")
			self.penup()
			self.speed(5)
			self.goto(-100,-100)

class BinarySearchTree:

	def __init__(self, contents=[]):
		self.root = None

		for e in contents:
			self.insert(e)

	def __contains__(self, item):
		if contains_helper(self.root, item) == False:
			return False
		return True

	def is_empty(self):
		return self.root == None

	def insert(self, item):
		insert_helper(self, self.root, item)

	def find_min(self):
		return min_helper(self.root)

	def find_max(self):
		return max_helper(self.root)

	def numItems(self):
		return numItems_helper(self.root)

	def tree_height(self):
		if self.is_empty():
			return None
		else:
			leaves = height_helper(self.root, [])
			heights = []
			for item in leaves:
				node = self.root
				height = 0
				while node.item != item:
					if item < node.item:
						node = node.left
					elif item > node.item:
						node = node.right
					height += 1
				heights.append(height)
			return max(heights)


	def inorder(self):
		if self.is_empty():
			return []
		return inorder_helper(self.root, [])

	def preorder(self):
		if self.is_empty():
			return []
		return preorder_helper(self.root, [])

	def postorder(self):
		if self.is_empty():
			return []
		return postorder_helper(self.root, [])

	def levelorder(self):
		lst = []
		if self.is_empty():
			return lst
		q = Queue()
		q.enqueue(self.root)
		while not q.is_empty():
			node = q.dequeue()
			lst.append(node.item)
			if node.left != None:
				q.enqueue(node.left)
			if node.right != None:
				q.enqueue(node.right)
		return lst

	def delete(self, item):
		if not item in self:
			return False
		elif self.root.item == item:
			if self.root.left == None and self.root.right == None:
				self.root = None
			elif self.root.right == None:
				self.root = self.root.left
			elif self.root.left == None:
				self.root = self.root.right
			else:
				min_item = max_helper(self.root.left)
				self.delete(min_item)
				self.root = TreeNode(min_item, self.root.left, self.root.right)
			return True
		node = delete_helper(self.root, item)
		if node.left != None and node.left.item == item:
			if node.left.left == None and node.left.right == None:
				node.left = None
			elif node.left.right == None:
				node.left = node.left.left
			elif node.left.left == None:
				node.left = node.left.right
			else:
				min_item = max_helper(node.left.left)
				self.delete(min_item)
				node.left = TreeNode(min_item, node.left.left, node.left.right)
		elif node.right != None and node.right.item == item:
			if node.right.left == None and node.right.right == None:
				node.right = None
			elif node.right.right == None:
				node.right = node.right.left
			elif node.right.left == None:
				node.right = node.right.right
			else:
				min_item = max_helper(node.right.left)
				self.delete(min_item)
				node.right = TreeNode(min_item, node.right.left, node.right.right)
		return True



def delete_helper(node, item):
	if (node.right != None and node.right.item == item) or (node.left != None and node.left.item == item):
		return node
	elif item < node.item:
		return delete_helper(node.left, item)
	else:
		return delete_helper(node.right, item)

def numItems_helper(node):
	if node == None:
		return 0
	return 1 + numItems_helper(node.left) + numItems_helper(node.right)

def max_helper(node):
	if node.right == None:
		return node.item
	return max_helper(node.right)

def min_helper(node):
	if node.left == None:
		return node.item
	return min_helper(node.left)

def postorder_helper(node, postorderlst):
	if node.left != None:
		postorderlst = postorder_helper(node.left, postorderlst)
	if node.right != None:
		postorderlst = postorder_helper(node.right, postorderlst)
	postorderlst.append(node.item)
	return postorderlst

def preorder_helper(node, preorderlst):
	preorderlst.append(node.item)
	if node.left != None:
		preorderlst = preorder_helper(node.left, preorderlst)
	if node.right != None:
		preorderlst = preorder_helper(node.right, preorderlst)
	return preorderlst

def inorder_helper(node, inorderlst):
	if node.left != None:
		inorderlst = inorder_helper(node.left, inorderlst)
	inorderlst.append(node.item)
	if node.right != None:
		inorderlst = inorder_helper(node.right, inorderlst)
	return inorderlst

def height_helper(node, leaves_list):
	if node == None:
		return []
	elif node.left == None and node.right == None:
		return [node.item]
	else:
		return leaves_list + height_helper(node.left, leaves_list) + height_helper(node.right, leaves_list)

def insert_helper(tree, node, item):
	if tree.is_empty():
		tree.root = TreeNode(item)
	elif item > node.item:
		if node.right == None:
			node.right = TreeNode(item)
		else:
			return insert_helper(tree, node.right, item)
	elif item < node.item:
		if node.left == None:
			node.left = TreeNode(item)
		else:
			return insert_helper(tree, node.left, item)


def contains_helper(node,item):
	if node == None:
		return False
	elif node.item == item:
		return node
	elif item > node.item:
		return contains_helper(node.right, item)
	elif item < node.item:
		return contains_helper(node.left, item)
