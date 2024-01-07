from tkinter import *
# tkinter does not read jpg files???

x = r"C:\Users\Quakeguy\Desktop\test.gif"


root = Tk()
root.title("Example")
root.maxsize(200, 300)
root.state("zoomed")

f = Frame(root, bg='grey').grid(row=0, column=1)

Button(f, text="MC").grid(row=0, column=0)
Button(f, text="MC").grid(row=0, column=1)
Button(f, text="MC").grid(row=0, column=2)
Button(f, text="MC").grid(row=0, column=3)



# image = PhotoImage(file=x)
# o = image.subsample(2,2)
# Label(root, image=o).grid(row=0, column=0, rowspan=6, padx=20)

# Label(root, text="Please enter your information", bg="green").grid(padx=5, pady=5,row=0, column=1, sticky="e", columnspan=2)
# Label(root, text="Name").grid(row=1, column=1, padx=5, pady=5)
# Entry(root, bd=3).grid(row=1, column=2)

# g = Menubutton(root, text="Gender")
# g.grid(row=2, column=2, sticky="W")
# g.menu = Menu(g, tearoff=0)
# g["menu"] = g.menu

# g.menu.add_cascade(label="Male")
# g.menu.add_cascade(label="Female")
# g.menu.add_cascade(label="Other")
# g.grid()

# Label(root, text="Eye Color").grid(row=3, column=1 ,sticky="W")
# Entry(root, bd=3).grid(row=3, column=2, padx=5, pady=5)

# Label(root, text="Height").grid(row=4, column=1 ,sticky="W")
# Entry(root, bd=3).grid(row=4, column=2, padx=5, pady=5)
# Label(root, text="Inches").grid(row=4, column=3, padx=3, pady=5)

# Label(root, text="Weight").grid(row=5, column=1 ,sticky="W")
# Entry(root, bd=3).grid(row=5, column=2, padx=5, pady=5)
# Label(root, text="lbs").grid(row=5, column=3, padx=3, pady=5, sticky="W")

# # left_frame = Frame(root, width=200, height=400, bg="grey")
# # left_frame.grid(row=0, column=0, padx=10, pady=5)

# # right_frame = Frame(root, width=650, height=400, bg="purple")
# # right_frame.grid(row=0, column=1, padx=10, pady=5)

# # Label(left_frame, text="Original Image").grid(row=0, column=0, pady=5, padx=5)

# # image = PhotoImage(file=x)
# # original = image.subsample(3, 3)
# # Label(left_frame, image=original).grid(row=1, column=0, padx=5, pady=5)

# # Label(right_frame, image=image).grid(row=0, column=0, padx=5, pady=5)

# # toolbar = Frame(left_frame, width=180, height=185)
# # toolbar.grid(row=2, column=0, padx=5, pady=5)

# # Label(toolbar, text="Tools", relief=RAISED).grid(row=0, column=0, padx=5, pady=3, ipadx=10)
# # Label(toolbar, text="Filters", relief=RAISED).grid(row=0, column=1, padx=5, pady=3, ipadx=10)

# # Label(toolbar, text="Select").grid(row=1, column=0, padx=5, pady=5)
# # Label(toolbar, text="Crop").grid(row=2, column=0, padx=5, pady=5)
# # Label(toolbar, text="Rotate & Flip").grid(row=3, column=0, padx=5, pady=5)
# # Label(toolbar, text="Resize").grid(row=4, column=0, padx=5, pady=5)
# # Label(toolbar, text="Exposure").grid(row=5, column=0, padx=5, pady=5)

root.mainloop()
# import random
# import sys
# grid = list()
# for n in range(0, 4):
#       grid.append([0] * 4)

# for n in range(1, 9):
#         for _ in range(2):
#             i = random.randint(0 ,(4 - 1))
#             j = random.randint(0 ,(4 - 1))
#             print(grid)
#             while grid[i][j] != 0:
#                 i = random.randint(0 ,(4 - 1))
#                 j = random.randint(0 ,(4 - 1))
#             grid[i][j] = n


# print(grid)