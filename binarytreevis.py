from turtle import *
from binary_search_tree import *
import tkinter
import sys


class BTNode(RawTurtle):
	def __init__(self, val, canvas = None):
		self.val = val
		if canvas != None:
			self.col = None
			super().__init__(canvas)
			self.ht()
			self.shape("circle")
			self.penup()
			self.speed(5)
			self.goto(-100,-100)

class Grid:
	def __init__(self, rows, cols, screen=None):
		self.screen = screen
		self.rows = rows
		self.cols = cols
		self.items = []
		for i in range(rows):
			self.items.append([None] * cols)

	def __getitem__(self, index):
		return self.items[index]

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
		#screen.tracer(100000)

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
				item = int(nodevalue.get())
			except:
				return
			if item in tree:
				pass
			else:
				tree.insert(item)
				knuth_layout(tree.root, 0)
				global i
				i = 0
				grid = Grid(tree.tree_height() + 1, tree.numItems())
				for n in tree.inorder():
					node = contains_helper(tree.root, n)
					print('x:', node.x, 'y:', node.y, 'value', node.item)
					grid[node.y][node.x] = node
				print('------')


		def removeHandler():
			try:
				item = int(nodevalue.get())
			except:
				return
			if item in tree:
				tree.delete(item)
				print(tree.inorder())
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
