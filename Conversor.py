from tkinter import*
from tkinter import ttk

class Conversor:
    
    def __init__(self, raiz):
        raiz.title("Pies a metros")

        self.pies = StringVar()
        self.metros = StringVar()
        
        mainFrame = ttk.Frame(raiz, padding="16")
        mainFrame.grid(column=0, row=0)

        piesEntry = ttk.Entry(mainFrame, textvariable=self.pies)
        piesEntry.grid(column=1, row=0)

        ttk.Label(mainFrame, text="Pies").grid(column=2, row=0, sticky=W)
        ttk.Label(mainFrame, text="Son equivalentes").grid(column=0, row=1)
        ttk.Label(mainFrame, textvariable=self.metros).grid(column=1, row=1)
        ttk.Label(mainFrame, text="Metros", padding="16").grid(column=2, row=1)
        ttk.Button(mainFrame, text='Calcular', command=self.calcular).grid(column=2, row=2, pady=20)

        piesEntry.focus()

        raiz.bind("<Return>", self.calcular)

    def calcular(self, *args):
        valorPies = float(self.pies.get())
        print("Pies: ", valorPies)
        valorMetros = valorPies * 0.3048
        print("Metros: ", valorMetros)
        self.metros.set(valorMetros)
        


if __name__ == "__main__":
    print(("Hola soy el modulo principal"))
    print("Name conversor: ", __name__)