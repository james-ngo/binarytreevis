import turtle
import tkinter
import sys

def main():

	root = tkinter.Tk()

	cv = tkinter.Canvas(root, width=800, height=600)

	cv.pack(side = tkinter.LEFT)

	root.title("Binary Tree Visualization")

	frame = tkinter.Frame(root)
	frame.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)

	sideBar = tkinter.Frame(frame,padx=5,pady=5)
	sideBar.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)

	def quitHandler():
		sys.exit(0)

	quitButton = tkinter.Button(frame, text='Quit', command=quitHandler)
	quitButton.pack()

	tkinter.mainloop()

if __name__ == '__main__':
	main()
