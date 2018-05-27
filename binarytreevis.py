from turtle import *
from binary_search_tree import *
import tkinter
import sys


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
		x_spacing = 600 // self.cols
		y_spacing = 600 // self.rows
		for row in range(self.rows):
			for col in range(self.cols):
				if self[row][col] != None:
					self[row][col].st()
					self[row][col].goto(25+col*x_spacing,575-row*y_spacing)
					self[row][col].write(str(float(self[row][col].item)), False, align="center")
					if self[row][col].left != None:
						parent = self[row][col]
						left_child = self[row][col].left
						LineTurtle = RawTurtle(self.canvas)
						LineTurtle.ht()
						LineTurtle.penup()
						LineTurtle.goto(25+col*x_spacing,575-row*y_spacing)
						LineTurtle.pendown()
						LineTurtle.goto(25+left_child.x*x_spacing,575-left_child.y*y_spacing)
					if self[row][col].right != None:
						parent = self[row][col]
						right_child = self[row][col].right
						LineTurtle = RawTurtle(self.canvas)
						LineTurtle.ht()
						LineTurtle.penup()
						LineTurtle.goto(25+col*x_spacing,575-row*y_spacing)
						LineTurtle.pendown()
						LineTurtle.goto(25+right_child.x*x_spacing,575-right_child.y*y_spacing)
		self.screen.update()

	# def addRow(self):
	# 	self.items.append([None] * self.cols)
	# 	self.rows += 1
	#
	# def addCol(self):
	# 	for row in self.items:
	# 		row.append(None)
	# 	self.cols += 1

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
		#grid = Grid(screen)

		def insertHandler():
			try:
				item = int(nodevalue.get())
			except:
				return
			if item in tree:
				pass
			else:
				screen.clear()
				tree.insert(item)
				knuth_layout(tree.root, 0)
				global i
				i = 0
				grid = Grid(tree.tree_height() + 1, tree.numItems(), screen, cv)
				for n in tree.inorder():
					node = contains_helper(tree.root, n)
					grid[node.y][node.x] = TreeNode(node.item, node.left, node.right, cv)
				grid.drawNodes()

		def removeHandler():
			try:
				item = int(nodevalue.get())
			except:
				return
			if item in tree:
				screen.clear()
				tree.delete(item)
				knuth_layout(tree.root, 0)
				global i
				i = 0
				grid = Grid(tree.tree_height() + 1, tree.numItems(), screen, cv)
				for n in tree.inorder():
					node = contains_helper(tree.root, n)
					grid[node.y][node.x] = TreeNode(node.item,node.left,node.right,cv)
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
