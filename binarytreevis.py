from turtle import *
from binary_search_tree import *
import tkinter
import sys

class BTNode(RawTurtle):
	def __init__(self, canvas = None):
		if canvas != None:
			super().__init__(canvas)
			self.ht()
			self.shape("circle")
			self.penup()
			self.speed(5)
			self.goto(-100,-100)

class BinaryTreeVis(tkinter.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.pack()
		self.buildWindow()

	def buildWindow(self):

		cv = ScrolledCanvas(self,600,600,600,600)
		cv.pack(side = tkinter.LEFT)

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
				node = int(nodevalue.get())
			except:
				return
			if node in tree:
				pass
			else:
				tree.insert(node)
				print(tree.inorder())

		def removeHandler():
			try:
				node = int(nodevalue.get())
			except:
				return
			if node in tree:
				tree.delete(node)
				print(tree.inorder())
			else:
				pass

		def containsHandler():
			try:
				node = int(nodevalue.get())
			except:
				return
			if node in tree:
				tkinter.messagebox.showwarning("Search Result","Item is in tree!")
			else:
				tkinter.messagebox.showwarning("Search Resuly","Item is NOT in tree!")

		insertButton = tkinter.Button(frame, text = "Insert", command=insertHandler) #add command=insertHander parameter
		insertButton.pack()

		removeButton = tkinter.Button(frame, text = "Remove", command=removeHandler) #add command=removeHandler parameter
		removeButton.pack()

		containsButton = tkinter.Button(frame, text = "Contains?", command=containsHandler) #add command=containsHandler parameter
		containsButton.pack()


def main():
	root = tkinter.Tk()
	root.title("Binary Tree Visualization")
	application = BinaryTreeVis(root)
	application.mainloop()

if __name__ == "__main__":
	main()
