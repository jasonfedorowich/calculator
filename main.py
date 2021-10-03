# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import tkinter
from tkinter import *

from tkinter import *

root = Tk()


def get_number(s, i):
    result = ''
    while i < len(s) and (s[i].isdigit() or s[i] == '.'):
        result += s[i]
        i += 1

    return i - 1, float(result)


def evaluate(s):
    try:
        stack = []
        i = 0
        neg = False
        while i < len(s):
            ch = s[i]
            if ch == '*':
                if len(stack) == 0:
                    raise Exception('Invalid')
                else:
                    b = stack.pop()
                    i, n = get_number(s, i + 1)
                    stack.append(b * n)
            elif ch == '/':
                if len(stack) == 0:
                    raise Exception('Invalid')
                else:
                    b = stack.pop()
                    i, n = get_number(s, i + 1)
                    stack.append(b / n)

            elif ch == '-':
                neg = True
            elif ch == '+':
                neg = False
            elif not ch.isdigit():
                raise Exception("Invalid")
            else:
                i, num = get_number(s, i)
                if neg:
                    num *= -1
                    neg = False
                stack.append(num)

            i += 1

        num = 0
        for n in stack:
            num += n
        return num
    except Exception as e:
        raise Exception(e)



class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.entry = Entry(root, width=40, text='0', textvariable="StringVars")
        self.entry.grid(row=0, column=0)
        self.entry.insert(0, '0')
        self.entry.bind("<Key>", self.key_pressed_field)

        for i in range(10):
            tkinter.Button(root, text=str(i), command=lambda temp=str(i): self.number_button(temp)).grid(row=2,
                                                                                                         column=i + 1)

        symbols = ['+', '-', '*', '/', '=', '.']
        col = 1
        for symbol in symbols:
            tkinter.Button(root, text=symbol, command=lambda temp=symbol: self.number_button(temp)).grid(row=3, column=col)
            col += 1

        tkinter.Button(root, text="C", command=self.clear_button).grid(row=1, column=1)

    def number_button(self, n):
        if self.entry.get() == '0':
            self.entry.delete(0, END)
            self.entry.insert(0, n)
        else:
            if n == '=':
                s = self.entry.get()
                try:
                    s = evaluate(s)
                except Exception as e:
                    s = 'Error'
                self.entry.delete(0, END)
                self.entry.insert(0, s)
                return
            prev = self.entry.get()
            prev = prev + n
            self.entry.delete(0, END)
            self.entry.insert(0, prev)



    def clear_button(self):
        self.entry.delete(0, END)
        self.entry.insert(0, '0')

    def key_pressed_field(self, event):
        if event.keysym == 'Return':
            s = self.entry.get()
            try:
                s = evaluate(s)
            except Exception as e:
                s = 'Error'
            self.entry.delete(0, END)
            self.entry.insert(0, s)



# initialize tkinter
app = Window(root)

# set window title
root.wm_title("Calculator")


# show window
root.mainloop()
