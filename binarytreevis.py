from turtle import *
import tkinter
import sys

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


class TreeNode:
	def __init__(self, item, left=None, right=None):
		self.item = item
		self.left = left
		self.right = right
		self.x = None
		self.y = None

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


class Grid:
	def __init__(self, rows, cols, screen=None, canvas=None):
		self.screen = screen
		self.canvas = canvas
		self.rows = rows
		self.cols = cols
		self.items = []
		for i in range(rows):
			self.items.append([None] * cols)


	def __getitem__(self, index):
		return self.items[index]

	def drawNodes(self):
		self.screen.tracer(0)
		x_spacing = 500 // self.cols
		y_spacing = 500 // self.rows
		for row in range(self.rows):
			for col in range(self.cols):
				if self[row][col] != None:
					bstnode = RawTurtle(self.canvas)
					bstnode.ht()
					bstnode.shape("circle")
					bstnode.shapesize(.25, .25)
					bstnode.penup()
					bstnode.speed(5)
					bstnode.goto(100+col*x_spacing,500-row*y_spacing)
					bstnode.st()
					bstnode.write(str(float(self[row][col].item)), False, align="center")
					if self[row][col].left != None:
						parent = self[row][col]
						left_child = self[row][col].left
						LineTurtle = RawTurtle(self.canvas)
						LineTurtle.ht()
						LineTurtle.penup()
						LineTurtle.goto(100+col*x_spacing,500-row*y_spacing)
						LineTurtle.pendown()
						LineTurtle.goto(100+left_child.x*x_spacing,500-left_child.y*y_spacing)
					if self[row][col].right != None:
						parent = self[row][col]
						right_child = self[row][col].right
						LineTurtle = RawTurtle(self.canvas)
						LineTurtle.ht()
						LineTurtle.penup()
						LineTurtle.goto(100+col*x_spacing,500-row*y_spacing)
						LineTurtle.pendown()
						LineTurtle.goto(100+right_child.x*x_spacing,500-right_child.y*y_spacing)
		self.screen.update()

class BinaryTreeApplication(tkinter.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.pack()
		self.buildWindow()

	def buildWindow(self):

		cv = ScrolledCanvas(self,600,600,600,600)
		cv.pack(side = tkinter.LEFT)
		t = RawTurtle(cv)
		screen = t.getscreen()
		screen.tracer(100000)

		screen.setworldcoordinates(0,0,600,600)
		screen.bgcolor("white")
		t.ht()

		frame = tkinter.Frame(self)
		frame.pack(side = tkinter.RIGHT,fill=tkinter.BOTH)


		def quitHandler():
			self.master.quit()

		quitButton = tkinter.Button(frame, text = "Quit", command=quitHandler)
		quitButton.pack()

		label = tkinter.Label(frame,text="Node Value:")
		label.pack()

		nodevalue = tkinter.StringVar()

		entry = tkinter.Entry(frame, width=25, textvariable=nodevalue)
		entry.pack()

		tree = BinarySearchTree()

		def insertHandler():
			try:
				item = float(nodevalue.get())
			except:
				return
			if item in tree:
				pass
			else:
				tree.insert(item)
				knuth_layout(tree.root, 0)
				global i
				i = 0
				grid = Grid(tree.tree_height() + 1, tree.numItems(), screen, cv)
				screen.clear()
				for n in tree.inorder():
					node = contains_helper(tree.root, n)
					grid[node.y][node.x] = TreeNode(node.item, node.left, node.right)
				grid.drawNodes()

		def removeHandler():
			try:
				item = int(nodevalue.get())
			except:
				return
			if item in tree:
				tree.delete(item)
				knuth_layout(tree.root, 0)
				global i
				i = 0
				grid = Grid(tree.tree_height() + 1, tree.numItems(), screen, cv)
				screen.clear()
				for n in tree.inorder():
					node = contains_helper(tree.root, n)
					grid[node.y][node.x] = TreeNode(node.item,node.left,node.right)
				grid.drawNodes()
			else:
				pass

		def containsHandler():
			try:
				item = int(nodevalue.get())
			except:
				return
			if item in tree:
				tkinter.messagebox.showwarning("Search Result","Item is in tree!")
			else:
				tkinter.messagebox.showwarning("Search Result","Item is NOT in tree!")

		insertButton = tkinter.Button(frame, text = "Insert", command=insertHandler) #add command=insertHander parameter
		insertButton.pack()

		removeButton = tkinter.Button(frame, text = "Remove", command=removeHandler) #add command=removeHandler parameter
		removeButton.pack()

		containsButton = tkinter.Button(frame, text = "Contains?", command=containsHandler) #add command=containsHandler parameter
		containsButton.pack()

i = 0
def knuth_layout(root, depth):
	if root.left != None:
		knuth_layout(root.left, depth + 1)
	global i
	root.x = i
	root.y = depth; i += 1
	if root.right != None:
		knuth_layout(root.right, depth + 1)

def main():
	root = tkinter.Tk()
	root.title("Binary Tree Visualization")
	application = BinaryTreeApplication(root)
	application.mainloop()

if __name__ == "__main__":
	main()
