import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()

def gugudan(dan):
    dan = int(input("단을 입력하시오: "))

dan = int(simpledialog.askstring(title = '구구단', prompt= '단을 입력하시오.'))

for i in range(1, 10):
        print('{} * {} = {}'.format(dan, i, dan * i))
