from turtle import *
from binary_search_tree import *
import tkinter
import sys

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

		label = tkinter.Label(frame,text="Node Value:", fg="black")
		label.pack()

		entry = tkinter.Entry(frame, width=25)
		entry.pack()

		insertButton = tkinter.Button(frame, text = "Insert") #add command=insertHander parameter
		insertButton.pack()

		removeButton = tkinter.Button(frame, text = "Remove") #add command=removeHandler parameter
		removeButton.pack()

		containsButton = tkinter.Button(frame, text = "Contains?") #add command=containsHandler parameter
		containsButton.pack()

def main():
	root = tkinter.Tk()
	root.title("Binary Tree Visualization")
	application = BinaryTreeVis(root)
	application.mainloop()

if __name__ == "__main__":
	main()
