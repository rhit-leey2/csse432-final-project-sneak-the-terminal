import os
import subprocess

from tkinter import *
from tkinter import ttk

class TerminalWindow(Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.current_dir = os.getcwd()
        self.prompt = " >> " + self.current_dir 
        
        self.create_widgets()
        self.grid()

    def create_widgets(self):
        self.terminal_output = Text(self, bg='black', fg='white', insertbackground='black', font='Courier',  height=40,width=90, highlightcolor='green')
        self.terminal_output.grid(row=0, column=0)

        self.terminal_input = Entry(self, bg='black', fg='white')
        self.terminal_input.grid(row=1, column=0)
        self.terminal_input.bind('<Return>', self.execute_command)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.terminal_input.focus()

    def execute_command(self, event):
        command = self.terminal_input.get()
        self.terminal_input.delete(0, END)
        self.terminal_output.insert(END, self.prompt + " " + command + '\n')

        if command == 'exit':
            self.quit()
            return

        try:
            if command.startswith('cd'):
                path = command.split(' ')[1]
                if path == '..':
                    self.current_dir = os.path.abspath(os.path.join(self.current_dir, os.pardir))
                else:
                    self.current_dir = os.path.abspath(os.path.join(self.current_dir, path))
                os.chdir(self.current_dir)
                #self.terminal_output.insert(END, ' >> ' + self.current_dir + '\n')
            else:
                process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate()
                if stdout:
                    self.terminal_output.insert(END, stdout.decode('utf-8'))
                if stderr:
                    self.terminal_output.insert(END, stderr.decode('utf-8'))
                #self.terminal_output.insert(END + '\n')
                
        except Exception as e:
            self.terminal_output.insert(END, str(e) + '\n')

        #self.prompt = ' >> '
        self.prompt = ' >> ' + self.current_dir + '\n'
        self.terminal_output.insert(END, self.prompt + '\n')
        #self.terminal_output.insert(END + " " + '\n')

root = Tk()
root.title("Sneak in the Terminal")
root.geometry("730x560")
app = TerminalWindow(master=root)
app.mainloop()
