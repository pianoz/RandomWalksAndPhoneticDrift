import tkinter as tk



class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class InitPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self,
                         text=("linguistics and random walks, \n evaluating phonetics as a biological system in the context of random walks."),
                         font=("Arial Bold", 15))
        label.pack(side="top", expand=True)


class DatasetHandler(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        label = tk.Label(self, text="TBI.")

        label.pack(side="top", expand=True)


class RandomWalkTest (Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        label = tk.Label(self, text="TBI.")

        label.pack(side="top", expand=True)


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        ip = InitPage(self)
        I_L_T = DatasetHandler(self)
        rwtest =RandomWalkTest(self)


        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        ip.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        I_L_T.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        rwtest.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        # Label = tk.Label(buttonframe, text="SelectedSchema", command=I_L_T.lift)

        b1 = tk.Button(buttonframe, text="Import Language Tree", command=I_L_T.lift)
        b4 = tk.Button(buttonframe, text="Random Walk Test", command=rwtest.lift)
        b5 = tk.Button(buttonframe, text="home", command=ip.lift)

        b5.pack(side="left")
        b1.pack(side="right")
        b4.pack(side="right")


        ip.show()


if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1000x700")
    root.mainloop()