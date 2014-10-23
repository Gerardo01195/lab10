##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# house and roof
square = drawpad.create_rectangle(200,200,400,400, fill ='red')
line1 = drawpad.create_line(200,200,300,100)
line2 = drawpad.create_line(300,100,400,200)
# square windows code
square1 = drawpad.create_rectangle(220,300,260,340, fill ='yellow')
square2 = drawpad.create_rectangle(340,300,380,340, fill ='black')
square3 = drawpad.create_rectangle(220,250,260,210, fill ='black')
square4 = drawpad.create_rectangle(340,250,380,210, fill ='yellow')
# Door Code
square = drawpad.create_rectangle(280,400,320,320, fill ='red')
# Door Handle
oval = drawpad.create_oval(310,350,320,360, fill='white')
# Chimney code!
line1 = drawpad.create_line(400,110,400,200)
line2 = drawpad.create_line(350,110,400,110)
line3 = drawpad.create_line(350,110,350,150)
root.mainloop()
