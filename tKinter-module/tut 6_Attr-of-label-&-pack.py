# Attributes of label and pack.

from tkinter import *

root = Tk()
root.geometry("1400x666")
root.title("GUI Window v2.5.8")

# Important Label Options
"""
text - adds the text.
bg - background.
fg - foreground.

font - sets the font.
# font can be given by two types.
1 - by passing a tupple.
font = ("Comicsanms", 19, "bold")
2 - by passing a string.
font = "Comicsanms 19 bold"

padx - x padding.
pady - y padding.
borderwidth = 3
relief - border styling = SUNKEN, GROOVE, RAISED, RIDGE.
"""

# Important Pack Options
"""
anchor - nw, ne, sw, se
side - TOP(default), BOTTOM, LEFT, RIGHT.
fill - X, Y
padx - 
pady -
"""

l = Label(text="""Machine learning (ML) is a field of study in artificial intelligence concerned with the development and study of statistical algorithms 
\nthat can learn from data and generalise to unseen data, and thus perform tasks without explicit instructions.[1] Within a subdiscipline in machine learning,
\nadvances in the field of deep learning have allowed neural networks, a class of statistical algorithms, to surpass many previous machine learning
\napproaches in performance.[2]. ML finds application in many fields, including natural language processing, computer vision, speech recognition, 
\nemail filtering, agriculture, and medicine.[3][4] The application of ML to business problems is known as predictive analytics.
\ndata analysis (EDA) via unsupervised learning.[6][7]
\nFrom a theoretical viewpoint, probably approximately correct learning provides a framework for describing machine learning.
""",
          bg="red", fg="yellow", padx=20, pady=120, font="Comicsanms 11 bold", borderwidth=3, relief=SUNKEN)

# l.pack(anchor="ne")
# l.pack(side=BOTTOM)
# l.pack(side=BOTTOM, anchor="se")
# l.pack(side=LEFT, fill=Y)
l.pack(side=LEFT, fill=Y, padx=20, pady=24)

# label ki padding andar sai lagti hai.
# pack ki padding bahar sai lagti hai.

root.mainloop()

# TASK - Create a GUI in which
